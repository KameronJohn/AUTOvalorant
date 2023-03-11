from pyautogui import *
import pyautogui
import time
# import keyboard
import random
# import win32api, win32con, win32gui
# import webbrowser
import os
# import pyperclip
# from openpyxl import Workbook, load_workbook
# from datetime import date
# from openpyxl.utils import get_column_letter
# import pandas as pd
# import numpy as np
# import sys
# import pygetwindow
from datetime import datetime, timedelta, timezone
# from PIL import Image
# from pytesseract import pytesseract
import os
import os
import csv
import re
class v:
    currentPath = os.path.dirname(os.path.abspath(__file__))
    currentPath += '\\'
    screenshotPath = currentPath+'\\source\\'
    #if even number= either select agent/ re queuing
    status = 1
    def agentXYposition(account):
        csv_filename = v.currentPath+ 'agentXYposition.csv'
        agentXYposition = []
        with open(csv_filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['Account'] == account:
                    agentXYposition.append(row)
        return agentXYposition
    def getAgentsPosition(account):
        today = datetime.today().strftime(f'%Y%m%d')
        column = ['Date','Account','Agent', 'Xposition', 'Yposition']
        with open(f'{v.currentPath}\\agentXYposition.csv', 'a') as f:
            # create the csv writer
            writer = csv.writer(f)
            # write a row to the csv file
            writer.writerow(column)
            AllFiles = os.listdir(v.screenshotPath)
            for i in AllFiles:
                if re.match(r"agent_*", i):
                    agent = i.replace("agent_", "")
                    agent = agent[:int(agent.find('.'))]
                    print(f"searching agent: {agent}")
                    count =0
                    while True:
                        try:
                            x, y = pyautogui.locateCenterOnScreen(v.screenshotPath+i, region = (0,0,2500,1440), confidence=0.8)
                            if (x, y) is not None:
                                pyautogui.moveTo(x, y)
                                row  =[today,account,agent,x,y]
                                writer.writerow(row)
                                break
                            else:
                                print('nope')
                        except:
                            count+=1
                        if count >4:
                            break
                    
        # csv_filename = v.currentPath+ 'agentXYposition.csv'
        # with open(csv_filename) as f:
        #     reader = csv.DictReader(f)
        #     for row in reader:
        #         print(row)
    def searchAndClick(target):
        while True:
            try:
                x, y = pyautogui.locateCenterOnScreen(v.screenshotPath+target, region = (0,0,2500,1440), confidence=0.8)
                if (x, y) is not None:
                    pyautogui.moveTo(x, y)
                    click()
                    return x,y
                else:
                    print('nope')
            except:
                pass
    def tryAndSearch(target):
        try:
            x, y = pyautogui.locateCenterOnScreen(v.screenshotPath+target, region = (0,0,2500,1440), confidence=0.8)
            if (x, y) is not None:
                pyautogui.moveTo(x, y)
                click()
                # print(x,y)
                return x,y
        except:
            return
    def getVenue(agentXYposition):
        AllFiles = os.listdir(v.screenshotPath)
        venueList = []
        for i in AllFiles:
            if re.match(r"venue_*", i):
                # print(i)
                venueList.append(i)
        count=0
        v.stateReport(0,f'queuing')
        while True:
            searchingVenue = venueList[count%len(venueList)]
            # print(searchingVenue)
            try:
                x, y = pyautogui.locateCenterOnScreen(v.screenshotPath+searchingVenue, region = (715,0,1100,1440), confidence=0.8)
                if x is not None:
                    venue = searchingVenue.replace("venue_", "")
                    venue = venue[:int(venue.find('.'))]
                    v.stateReport(1,f'found {venue}')
                    v.status+=1
                    if v.status%2 ==0:
                        v.selectAgent(preference, searchingVenue, venue, agentXYposition)
                    else:
                        v.stateReport(0,f'REqueuing')
            except:
                count+=1
            x= v.tryAndSearch('inGame.png')
            if x is not None:
                click()
                time.sleep(0.5)
                click()
                time.sleep(0.5)
                click()
                time.sleep(0.25)
                click()
                v.stateReport(4, 'in game, have fun.')
                return
            else:
                pass
    def stateReport(tick, msg):
        total = 4
        cross = total - tick
        print("   ="* 20)
        print('✅'*tick+'❌'*cross+' '+msg)
        print("   ="* 20)
    def selectAgent(preference, searchingVenue, venue, agentXYposition, order=0):
        if v.random:
            agent=random.choice(agentXYposition)['Agent']
        else:
            try:
                agent = preference[venue][order]
            except:
                print('out of order la')
                return
        for i in agentXYposition:
            if i['Agent'] == agent:
                agnetPosition = i
                xaxis = int(i['Xposition'])
                yaxis = int(i['Yposition'])
                break
        while True:
            try:
                x = pyautogui.locateCenterOnScreen(v.screenshotPath+searchingVenue, region = (0,0,2500,1440), confidence=0.65)
                if x is None:
                    v.stateReport(2, 'select agent page')
                    break
            except:
                pass
        lockx, locky= int(agentXYposition[0]['Xposition']), int(agentXYposition[0]['Yposition'])
        for i in range(3):
            pyautogui.click(xaxis, yaxis)
            pyautogui.click(lockx, locky)
        count = 0
        while True:
            # pyautogui.click(xaxis, yaxis)
            # pyautogui.click(lockx, locky)
            try:
                x, y = pyautogui.locateCenterOnScreen(v.screenshotPath+'agentNotSelected.png', region = (0,0,2500,1440), confidence=0.8)
            except:
                if v.random:
                    v.stateReport(3,f'🍭🍭RANDOM🍭🍭 agent selected: 🍭  {agent} 🍭')
                else:
                    v.stateReport(3,f'agent selected: 🕵️  {agent} 🕵️')
                return 'selected'
            count+=1
            if count >5:
                order+=1
                print(f'❗❗❗❗ agent {order+1} cant be selected')
                v.selectAgent(preference, venue, agentXYposition, order)
            x= v.tryAndSearch('inQueue.png')
            if x is not None:
                v.getVenue(agentXYposition)
            
    def checkState():
        pass
    def MainFlow(account, skipStart=False, random=False):
        v.random = random
        if skipStart is False:
            v.searchAndClick('start.png')
        agentXYposition = v.agentXYposition(account)
        v.getVenue(agentXYposition)
# Astra, Breach, Brimstone, Chamber, Cypher, Gekko, Jett, Kay/O, Killjoy, Neon, Omen, Phoenix, Raze, Reyna, Sage, Skye, Sova, Viper, Yoru
preference = {
    'ascent':['omen','phoenix','breach'],
    'bind': ['omen','phoenix','breach'],
    'breeze':['habor','phoenix','breach'],
    'haven': ['omen','phoenix','breach'],
    'icebox': ['omen','phoenix','breach'], 
    'lotus': ['omen','phoenix','breach'],
    'pearl': ['habor','phoenix','breach'],
    'split': ['omen','phoenix','breach'],
    'fracture': ['phoenix','breach','omen'],
}
if __name__ == "__main__":
    # v.MainFlow()
    v.MainFlow('FatherSun', random='1')
    # v.getAgentsPosition(account='FatherSun')
# venue = 'split'
# agentXYposition = [{'date': '20230311', 'Agent': 'agentNotSelected', 'Xposition': '1214', 'Yposition': '1083'}, {'date': '20230311', 'Agent': 'breach', 'Xposition': '833', 'Yposition': '1231'}, {'date': '20230311', 'Agent': 'brimstone', 'Xposition': '943', 'Yposition': '1230'}, {'date': '20230311', 'Agent': 'habor', 'Xposition': '1389', 'Yposition': '1232'}, {'date': '20230311', 'Agent': 'omen', 'Xposition': '717', 'Yposition': '1344'}, {'date': '20230311', 'Agent': 'phoenix', 'Xposition': '831', 'Yposition': '1344'}, {'date': '20230311', 'Agent': 'reyna', 'Xposition': '1056', 'Yposition': '1343'}]


# q->inselectpage->selected->🎲