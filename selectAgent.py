from pyautogui import *
import pyautogui
import time
import keyboard
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
    lockX, lockY = 1213,1084
    #if even number= either select agent/ re queuing
    def agentXYposition(account):
        csv_filename = v.currentPath+ 'agentXYposition.csv'
        agentXYposition = []
        with open(csv_filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['Account'] == account:
                    agentXYposition.append(row)
        if len(agentXYposition) < 4:
            exit('SOMETIME IS NOT RIGHT')
        return agentXYposition
    def getAgentsPosition(account):
        today = datetime.today().strftime(f'%Y%m%d')
        column = ['Date','Account','Agent', 'Xposition', 'Yposition']
        csvFile = f'{v.currentPath}\\agentXYposition.csv'
        lines = list()
        with open(csvFile, 'r', newline='') as f:
            writer = csv.writer(f)
            for line in csv.reader(f):
                if account in line:
                    foundAccount = column.index('Account')
                    foundDate = column.index('Date')
                else:
                    lines.append(line)
            f.close()
        if foundAccount:
            print('  !'*10)
            print('previous record has found')
            print('  !'*10)
        with open(csvFile, 'a', newline='') as f:
            # create the csv writer
            # writer = csv.writer(f)
            # write a row to the csv file
            # writer.writerow(column)
            AllFiles = os.listdir(v.screenshotPath)
            for i in AllFiles:
                if re.match(r"agent_*", i):
                    agent = i.replace("agent_", "")
                    agent = agent[:int(agent.find('.'))]
                    # count =0
                    while True:
                        try:
                            x, y = pyautogui.locateCenterOnScreen(v.screenshotPath+i, region = (0,0,2500,1440), confidence=0.8)
                            if (x, y) is not None:
                                pyautogui.moveTo(x, y)
                                row  =[today,account,agent,x,y]
                                lines.append(row)
                                print(f"agent found: {agent}")
                                break
                            else:
                                print('nope')
                        except:
                        #     count+=1
                        # if count >2:
                            print(f"-   -   -   -   failed to locate: {agent}")
                            break
            f.close()
        with open(csvFile, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(lines)
            f.close()
        # exit()
        # csv_filename = v.currentPath+ 'agentXYposition.csv'
        # with open(csv_filename) as f:
        #     reader = csv.DictReader(f)
        #     for row in reader:
        #         print(row)
    def searchAndClick(target, needClick=True):
        while True:
            try:
                x, y = pyautogui.locateCenterOnScreen(v.screenshotPath+target, region = (0,0,2500,1440), confidence=0.8)
                if (x, y) is not None:
                    if needClick is True:
                        v.returnPreviousPosition(x,y)
                    return x,y
                else:
                    print('nope')
            except:
                pass
    def tryAndSearch(target, withoutClick=True, withoutMove=True):
        try:
            x, y = pyautogui.locateCenterOnScreen(v.screenshotPath+target, region = (0,0,2500,1440), confidence=0.85)
            if (x, y) is not None:
                if withoutMove is not True:
                    pyautogui.moveTo(x, y)
                if withoutClick is not True:
                    click()
                return x,y
        except:
            return
    def getStatus(agentXYposition, secondRun=False):
        AllFiles = os.listdir(v.screenshotPath)
        venueList = []
        for i in AllFiles:
            if re.match(r"venue_*", i):
                # print(i)
                venueList.append(i)
        if v.random:
            v.stateReport(0,f'queuing: {v.account}'+ '      '+v.random)
        else:
            v.stateReport(0,f'queuing: {v.account}')
        while True: 
            if v.tryAndSearch('matchFound.png'):
                v.stateReport(1,f'match found')
                v.getVenue(venueList, agentXYposition)
            if v.tryAndSearch('inGame.png'):
                v.stateReport(6, 'in game, have fun.')
                return
            else:
                pass
    def getVenue(venueList, agentXYposition):
        a = pyautogui.position()
        count = 0
        while True:
            searchingVenue = venueList[count%len(venueList)]
            try:
                x, y = pyautogui.locateCenterOnScreen(v.screenshotPath+searchingVenue, region = (715,0,1100,1440), confidence=0.8)
                if x is not None:
                    venue = searchingVenue.replace("venue_", "")
                    venue = venue[:int(venue.find('.'))]
                    v.stateReport(2,f'map: {venue}')
                    v.selectAgent(preference, venue, agentXYposition)
                    break
            except:
                count+=1
        # """ alt tab here """
        # pyautogui.keyDown('alt')
        # pyautogui.press('tab')
        # pyautogui.moveTo(a)
        # pyautogui.keyUp('alt')
        # """ alt tab here """
    def stateReport(tick, msg):
        total = 6
        cross = total - tick
        print("   ="* 20)
        print('✅'*tick+'❌'*cross+' '+msg)
    def selectAgent(preference, venue, agentXYposition, order=0, repickAgent=False):
        if v.random:
            systemChoice = random.choice(agentXYposition)
            agent=systemChoice['Agent']
            xaxis = int(systemChoice['Xposition'])
            yaxis = int(systemChoice['Yposition'])
        else:
            if type(preference) is dict:
                try:
                    agent = preference[venue][order]
                except:
                    print('out of order la')
                    return
            else:
                agent = preference[order]
            for i in agentXYposition:
                if i['Agent'] == agent:
                    # agnetPosition = i
                    xaxis = int(i['Xposition'])
                    yaxis = int(i['Yposition'])
                    break
        count =0
        if repickAgent is False:
            v.checkIfLoadingPageDone()
        cursorPos = pyautogui.position()
        if v.random:
            v.stateReport(4,f'🍭🍭RANDOM🍭🍭 agent selecting: 🍭  {agent} 🍭')
        else:
            v.stateReport(4,f'agent selecting: 🕵️  {agent} 🕵️')
        for i in range(10):
            pyautogui.click(xaxis, yaxis)
            pyautogui.click(v.lockX, v.lockY)
        if v.checkIfAgentLocked(agentXYposition): 
            print(f'❗❗❗❗ agent {order+1} cant be selected')
            v.selectAgent(preference, venue, agentXYposition, order, repickAgent=True)
        else:
            v.stateReport(5,f'agent selected')
            pyautogui.FAILSAFE = False
            """ alt tab here """
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.moveTo(cursorPos)
            pyautogui.keyUp('alt')
            """ alt tab here """
    def checkIfAgentLocked(agentXYposition):
        shuffleList = random.sample(agentXYposition, len(agentXYposition))
        # print(shuffleList)
        for i in shuffleList[:8]:
            xaxis = int(i['Xposition'])
            yaxis = int(i['Yposition'])
            pyautogui.click(xaxis,yaxis)
            if v.tryAndSearch('availableAgent.png'):
                return 'notSelected'
    def checkIfLoadingPageDone():
        pixelx,pixelY = 1550,712
        pixellx,pixellY = 300,300
        pixelllx,pixelllY = 1280,720
        # pyautogui.moveTo(pixelllx,pixelllY)
        b = pyautogui.pixel(pixelx,pixelY)
        b2 = pyautogui.pixel(pixellx,pixellY)
        b3 = pyautogui.pixel(pixelllx,pixelllY)
        count = 0
        count2 = 0
        count3 = 0
        tolerance = 35
        while True:
            if pyautogui.pixelMatchesColor(pixelx, pixelY, b, tolerance=tolerance):
                count = 0
            else:
                count +=1
            if pyautogui.pixelMatchesColor(pixellx, pixellY, b2, tolerance=tolerance):
                count2 = 0
            else:
                count2 +=1
            if pyautogui.pixelMatchesColor(pixelllx, pixelllY, b3, tolerance=tolerance):
                count3 = 0
            else:
                count3 +=1
            if count >5 and count2 >5 and count3 >5:
                v.stateReport(3, 'select agent page')
                return
    def afk():
        while True:
            pyautogui.press('space')
            time.sleep(5)

    def returnPreviousPosition(x,y):
        a = pyautogui.position()
        pyautogui.click(x, y)
        pyautogui.moveTo(a)
    def reportPlayer():
        print('fuction: reportPlayer is running...')
        while True:
            if keyboard.is_pressed('1'):
                v.reportAction()
            if keyboard.is_pressed('2'):
                return
    def reportAction():
        pyautogui.click()
        pyautogui.click()
        pyautogui.click(button='right')
        pyautogui.click()
        a = pyautogui.position()
        reportPos = [Point(x=949, y=368), Point(x=952, y=439), Point(x=939, y=730), Point(x=949, y=825), Point(x=945, y=894), Point(x=1239, y=1133)]
        for i in reportPos:
            pyautogui.click(i)
        time.sleep(0.4)
        pyautogui.click(x=1244, y=974)
        pyautogui.moveTo(a)
    def errorChecking(agentXYposition):
        availableAgent = []
        possibleAgent = []
        for i in agentXYposition:
            availableAgent.append(i['Agent'])
        if type(preference) is dict:
            mySet = set()
            tmp = preference.values()
            for iList in tmp:
                for i in iList:
                    mySet.add(i)
            possibleAgent = list(mySet)
        elif type(preference) is list:
            possibleAgent = preference
        else:
            exit('UNKNOWN DATA TYPE')
        for a in possibleAgent:
            if a not in availableAgent:
                print('possibleAgent:   ')
                print(possibleAgent)
                print('availableAgent:  ')
                print(availableAgent)
                exit(f'{a} is not available in this account!!!')
    def MainFlow(account, skipStart=False, random=False):
        v.stateReport(0, 'initiated')
        v.random = random
        v.account = account
        agentXYposition = v.agentXYposition(account)
        v.errorChecking(agentXYposition)
        if skipStart is False:
            v.searchAndClick('start.png')
        v.getStatus(agentXYposition)
"""
astra, breach, brimstone, chamber, cypher, gekko,jett, 
kayo, killjoy, neon, omen, phoenix, raze, 
reyna, sage, skye, sova, viper, yoru
"""
preference = {
    # 'ascent':['omen','phoenix','breach'],
    # 'haven': ['omen','phoenix','breach'],
    # 'icebox': ['omen','phoenix','breach'], 
    # 'lotus': ['omen','phoenix','breach'],
    # 'pearl': ['habor','phoenix','breach'],
    # 'split': ['omen','phoenix','breach'],
    # 'fracture': ['phoenix','breach','omen'],
    # 'bind': ['omen','phoenix','breach'],
    # 'breeze':['habor','phoenix','breach']


    'ascent':['jett','phoenix','breach'],
    'haven': ['breach','phoenix','breach'], 
    'icebox': ['breach','phoenix','breach'], 
    'lotus': ['omen','phoenix','breach'],
    'pearl': ['habor','phoenix','breach'],
    'split': ['gekko','phoenix','breach'],
    'fracture': ['phoenix','breach','omen'],
    'bind': ['omen','phoenix','breach'],
    'breeze':['habor','phoenix','breach']
}
# preference = ['jett', 'phoenix', 'yoru']
# preference = ['gekko', 'chamber', 'breach'] 
""" 
MainFlow(account, skipStart=False, random=False)
FatherSun, LaVanTor, speakEngInVal
"""
if __name__ == "__main__":
    # v.reportPlayer()
    v.MainFlow('speakEngInVal')
    # v.MainFlow('FatherSun', random='random is on')


    # v.getAgentsPosition(account='speakEngInVal')