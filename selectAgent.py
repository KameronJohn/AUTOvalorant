from pyautogui import *
import pyautogui
import time
import keyboard
import random
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
import math
import subprocess
import psutil
from PIL import ImageGrab
class v:
    agentSelected = [] 
    currentPath = os.path.dirname(os.path.abspath(__file__))
    currentPath += '\\'
    screenshotPath = currentPath+'source\\'
    others_path = currentPath+'others\\'
    accounts_info_path = currentPath+'accounts_info\\'
    lockX, lockY = 1213,1084
    accountCredentials = {
        'FatherSun': ['wonnacha','Pleasetellme3'],
        'LaVanTor': ['wonnacha3','Pleasetellme3'],
        'speakEngInVal': ['wonnacha4','Pleasetellme3'],
        'oOoOoOo': ['wonnacha6','Pleasetellme3'],
        'Dear Curi': ['wonnacha7','Pleasetellme3'],
    }
    debugging = 1
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
            exit('SOMETIME IS NOT RIGHT: len(agentXYposition) < 4')
        return agentXYposition
    def getAgentsPosition(account):
        originalLength = 0
        today = datetime.today().strftime(f'%Y%m%d')
        column = ['Date','Account','Agent', 'Xposition', 'Yposition']
        csvFile = f'{v.currentPath}\\agentXYposition.csv'
        lines = list()
        with open(csvFile, 'r', newline='') as f:
            writer = csv.writer(f)
            for line in csv.reader(f):
                originalLength +=1
                if account in line:
                    foundAccount = column.index('Account')
                    foundDate = column.index('Date')
                else:
                    lines.append(line)
            f.close()
        try:
            foundAccount
        except NameError:
            pass
        else:
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
                            print(f"   -   -   -   -   -   -   failed to locate: {agent}")
                            break
            f.close()
        v.debugger('originalLength: '+str(originalLength))
        v.debugger('len(lines): '+ str(len(lines)))
        if originalLength < len(lines):
            with open(csvFile, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(lines)
                f.close()
        else:
            print('  !'*10)
            print('nothing executed: originalLength < new length')
            print('  !'*10)
        # exit()
        # csv_filename = v.currentPath+ 'agentXYposition.csv'
        # with open(csv_filename) as f:BA
        #     reader = csv.DictReader(f)
        #     for row in reader:
        #         print(row)
    def format_time(elapsed_time):
        m, s = divmod(int(elapsed_time), 60)
        time_format = "{:02d}:{:02d}".format(m, s)
        return time_format
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
            # print('no msg found')
            return
    def getStatus(agentXYposition, secondRun=False):
        AllFiles = os.listdir(v.screenshotPath)
        venueList = []
        for i in AllFiles:
            if re.match(r"venue_*", i):
                # print(i)
                 venueList.append(i)
        v.stateReport(0,f'queuing')
        while True: 
            if v.tryAndSearch('matchFound.png'):
                v.stateReport(1,f'match found')
                v.getVenue(venueList, agentXYposition)
            pos = v.tryAndSearch('inGame.png')
            if pos is not None:
                v.stateReport(6, 'in game, have fun.')
                try:
                    v.afk_status
                    for i in range(3):
                        click(pos)
                        sleep(1)
                except:
                    pass
                return
            else:
                pass
    def getVenue(venueList, agentXYposition=False):
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
                    if agentXYposition is False:
                        break
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
        v.debugger('stateReport ends')
        return
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
            v.agentSelected.append(agent)
            for i in agentXYposition:
                if i['Agent'] == agent:
                    # agnetPosition = i
                    xaxis = int(i['Xposition'])
                    yaxis = int(i['Yposition'])
                    break
        count = 0
        
        # Compile the C++ file
        compile_cmd = ["g++", f"{v.others_path}selectagent.cpp", "-o", "selectagent"]
        subprocess.run(compile_cmd, check=True)

        if repickAgent is False:
            v.checkIfLoadingPageDone()
            # time.sleep(3.5)
        cursorPos = pyautogui.position()
        if v.random:
            v.stateReport(4,f'🍭🍭RANDOM🍭🍭 agent selecting: 🍭  {agent} 🍭')
        else:
            v.stateReport(4,f'agent selecting: 🕵️  {agent} 🕵️')
            v.debugger('after agent sel')
        """  """
        # pyautogui.FAILSAFE = False
        # try:
        #     for i in range(8):
        #         pyautogui.click(xaxis, yaxis)
        #         pyautogui.click(v.lockX, v.lockY)
        # except Exception as error:
        #     # handle the exception
        #     print("An exception occurred:", error) # An exception occurred: division by zero
        """  """
        # Run the compiled executable with the x and y coordinates as arguments
        run_cmd = [f"{v.others_path}selectagent", str(xaxis), str(yaxis), str(v.lockX), str(v.lockY)]
        subprocess.run(run_cmd, check=True)
        """  """
        if v.checkIfAgentLocked(agentXYposition): 
            order +=1
            alert_msg(f'agent {order} cant be selected')
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
        v.debugger('agentXYposition:\n')
        v.debugger(agentXYposition)
        new_items = [d for d in agentXYposition if 'Agent' not in d or d['Agent'] not in v.agentSelected]
        agentXYposition = new_items

        shuffleList = random.sample(agentXYposition, len(agentXYposition))
        # end_time = time.perf_counter()

        # elapsed_time = end_time - start_time

        # print(f'Time elapsed: {elapsed_time:.6f} seconds')
        v.debugger('  =   =   =')
        v.debugger('shuffleList:\n')
        v.debugger(shuffleList)
        for i in shuffleList[:6]:
            xaxis = int(i['Xposition'])
            yaxis = int(i['Yposition'])
            pyautogui.click(xaxis,yaxis)
            if v.tryAndSearch('availableAgent.png', withoutClick=True):
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

    def returnPreviousPosition(x,y):
        a = pyautogui.position()
        pyautogui.click(x, y)
        pyautogui.moveTo(a)
    def reportPlayer():
        print('fuction: reportPlayer is running...')
        pyautogui.click()
        pyautogui.click()
        pyautogui.click(button='right')
        pyautogui.click()
        a = pyautogui.position()
        reportPos = [Point(x=949, y=368), Point(x=952, y=439), Point(x=939, y=730), Point(x=949, y=825), Point(x=945, y=894), Point(x=1239, y=1133)]
        for i in reportPos:
            pyautogui.click(i)
        time.sleep(0.55)
        pyautogui.click(x=1244, y=974)
        pyautogui.moveTo(a)
    def check_if_val_message_sent():
        #check if the message sent
        result_pos = v.tryAndSearch(f'ok_button.png',withoutClick=True, withoutMove=True)
        if result_pos is not None:
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H:%M:%S")
            screenshot_path = v.screenshotPath+f'auto_sc\\{formatted_datetime}.png'
            v.screenshot(screenshot_path)
            alert_msg('check message at: '+screenshot_path)
            click(result_pos)
            v.check_if_val_message_sent()
        return
        # v.debugger("check_if_val_message_sent: "+ result_pos)
    def full_path_name_to_three_parts(fileName):
        dir_path, full_name = os.path.split(fileName)
        file_name, file_ext = os.path.splitext(full_name)
        return dir_path,file_name,file_ext
    # def screenshot(screenshot_path,previous_file='',loop_times=0,compare_size=0):
    #     # Take a screenshot of the entire screen
    #     screenshot = ImageGrab.grab()
    #     # Save the screenshot to a file
    #     screenshot.save(screenshot_path)
    #     current_size = v.wait_for_file_found(screenshot_path)
    #     if loop_times != 0:
    #         if current_size>compare_size:
    #             print("current_size>compare_size")
    #             os.remove(previous_file)
    #             os.rename(screenshot_path, previous_file)
    #             loop_times = 0
    #         else:
    #             print("normal")
    #             os.remove(screenshot_path)
    #             if loop_times > 2:
    #                 return
    #         screenshot_path = previous_file
    #     dir_path,file_name,file_ext = v.full_path_name_to_three_parts(screenshot_path)
    #     second_screenshot_path = dir_path+'\\'+file_name+'_1'+file_ext
    #     loop_times +=1
    #     v.screenshot(second_screenshot_path,screenshot_path,loop_times,current_size)
    def screenshot(screenshot_path,previous_file='',loop_times=0,compare_size=0):
        dir_path,file_name,file_ext = v.full_path_name_to_three_parts(screenshot_path)
        tmp_screenshot_path = dir_path+'\\'+file_name+'_1'+file_ext       
        # Take a screenshot of the entire screen
        screenshot = ImageGrab.grab()
        # Save the screenshot to a file
        screenshot.save(screenshot_path)
        current_size = v.wait_for_file_found(screenshot_path) 
        while True:
            # Take a screenshot of the entire screen
            screenshot = ImageGrab.grab()
            # Save the screenshot to a file
            screenshot.save(tmp_screenshot_path)
            tmp_size = v.wait_for_file_found(tmp_screenshot_path)
            if loop_times != 0:
                if tmp_size>current_size:
                    # print("tmp_size>compare_size")
                    os.remove(screenshot_path)
                    os.rename(tmp_screenshot_path, screenshot_path)
                    current_size = tmp_size
                    loop_times = 0
                else:
                    # print("normal")
                    os.remove(tmp_screenshot_path)
                    if loop_times > 2:
                        # print('  -  '*20)
                        return
            loop_times +=1
    def errorChecking(agentXYposition):
        availableAgent = []
        possibleAgent = []
        for i in agentXYposition:
            availableAgent.append(i['Agent'])
        if type(preference) is dict:
            print(''+'map'+'')
            mySet = set()
            tmp = preference.values()
            for iList in tmp:
                for i in iList:
                    mySet.add(i)
            possibleAgent = list(mySet)
        elif type(preference) is list:
            print('🕵️  '+str(preference[0])+ ' 🕵️')
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
    def debugger(msg):
        if v.debugging == 1:
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%H-%M-%S")
            print(f'debug-[{formatted_datetime}]: {msg}')
    def MainFlow(account, skipStart=False, random=False, reQ=False,launchAndLogin=False):
        v.random = random
        v.account = account
        agentXYposition = v.agentXYposition(account)
        if launchAndLogin:
            v.login()
        if reQ:
            v.requeueRank()
        if v.random:
            v.stateReport(0,f'autoSelect initiated: {v.account}'+ '\n'+v.random)
        else:
            v.stateReport(0, f'autoSelect initiated: {v.account}')
        if skipStart is False:  
            v.searchAndClick('start.png')
        v.getStatus(agentXYposition)
        return
    def requeueRank():
        a = pyautogui.position()
        reQ = [Point(x=1219, y=50), Point(x=1219, y=50), Point(x=1219, y=50), Point(x=1219, y=50)]
        for i in reQ:
            click(i)
            time.sleep(0.2)
        #GAME MODE
        game_mode_image = [f"{game_mode}1.png", f"{game_mode}2.png"]
        break_loop = False
        while not break_loop:
            for i in game_mode_image:
                x = v.tryAndSearch(i,withoutClick=False, withoutMove=False)
                if x is not None:
                    break_loop = True
                    break
        #start queuing
        click(x=1240, y=1296)
        pyautogui.FAILSAFE = False
        """ alt tab here """
        pyautogui.keyDown('alt')
        pyautogui.press('tab')
        pyautogui.moveTo(a)
        pyautogui.keyUp('alt')
        """ alt tab here """
    def login(loginUsername=False,loginPassword=False,direct_launch=False):
        if direct_launch:
            os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Riot Games\特戰英豪.lnk')
        else:
            pyautogui.press('win')
            time.sleep(1)
            pyautogui.write('riot')
            time.sleep(0.4)
            pyautogui.press('enter')

        while True:
            try:
                x,y = pyautogui.locateCenterOnScreen(v.screenshotPath+'username.png', region = (0,0,2560,1440), confidence=0.8)
                if x is not None:
                    break
            except:
                pass
            try:
                x,y = pyautogui.locateCenterOnScreen(v.screenshotPath+'usernamee.png', region = (0,0,2560,1440), confidence=0.8)
                if x is not None:
                    break
            except:
                pass
        #retrieve login username and password
        if loginUsername is False and loginPassword is False:
            loginUsername, loginPassword = v.accountCredentials[v.account]
        pyautogui.click(x,y)
        pyautogui.write(loginUsername)
        pyautogui.press('tab')
        pyautogui.write(loginPassword)
        pyautogui.press('enter')
        time.sleep(5)
        start_time = time.time()
        while True:
            try:
                play_x,play_y = pyautogui.locateCenterOnScreen(v.screenshotPath+'play.png', region = (0,0,2560,1440), confidence=0.8)
                if play_x is not None:
                    break
            except:
                pass
            #press start in game
            try:
                play_x,play_y = pyautogui.locateCenterOnScreen(v.screenshotPath+'play.png', region = (0,0,2560,1440), confidence=0.7)
                if play_x is not None:
                    break
            except:
                pass
            elapsed_time = time.time() - start_time
            allowed_time = 60
            if elapsed_time > allowed_time:
                v.debugger(f'OVER {allowed_time} SECONDS!!!!')
                v.debugger('restarting')
                v.exit_valorant()
                sleep(3)
                v.login(loginUsername,loginPassword,direct_launch=True)
                sleep(3)
        time.sleep(1)
        pyautogui.FAILSAFE = False
        v.check_if_val_message_sent()
        click(play_x,play_y)
        v.debugger(f'click({play_x},{play_y})')
    def wait_for_file_found(file):
        while True:
            if os.path.isfile(file):
                v.debugger('file found: '+ file)
                count = 0
                size = os.path.getsize(file)
                while True:
                    new_size = os.path.getsize(file)
                    if new_size == size:
                        count += 1
                    else:
                        size = new_size
                        count = 0
                    if count == 3:
                        return size
    def check_all_account_available_agent(secondTime=False):
        account = ['',3,4,5,6,7]
        for i in account:
            account_name = 'wonnacha'+str(i)
            password = 'Pleasetellme3'
            v.login(account_name,password,direct_launch=True)
            time.sleep(2)
            for pos,fileName in [
                [[Point(x=1004, y=46)],'current_contract'],
                [[Point(x=1486, y=44),Point(x=2225, y=34)],'career&mission']
                ]:
                for each_pos in pos:
                    click(each_pos)
                    sleep(2)
                current_datetime = datetime.now()
                formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
                screenshot_path = v.accounts_info_path+formatted_datetime+'_'+account_name+'_'+fileName+'.png'
                v.screenshot(screenshot_path)
            v.go_to_custom_game_mode(account_name,password)
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_path = v.accounts_info_path+formatted_datetime+'_'+account_name+'_available agents'+'.png'
            v.screenshot(screenshot_path)
            print('check screenshot at: ',screenshot_path)
            v.exit_valorant()
            time.sleep(2)
    def go_to_custom_game_mode(account_name,password):
        click(x=1266, y=33)
        poss = [Point(x=1855, y=139), Point(x=1225, y=1311), Point(x=1066, y=825)]
        for each_pos in poss:
            click(each_pos)
            time.sleep(0.75)
        start_time = time.time()
        for i in ['agent_sage.png','agent_phoenix.png','agent_brimstone.png']:
            v.debugger('looking for: '+i)
            while True:
                try:
                    target = v.screenshotPath+i
                    x,y = pyautogui.locateCenterOnScreen(target, region = (0,0,2500,1440), confidence=0.9)
                    moveTo(x,y)
                    v.debugger(i + ' found')
                    break
                except:
                    pass
                elapsed_time = time.time() - start_time
                allowed_time = 30
                if elapsed_time > allowed_time:
                    v.debugger(f'OVER {allowed_time} SECONDS!!!!')
                    v.debugger('restarting')
                    v.exit_valorant()
                    sleep(3)
                    v.login(account_name,password,direct_launch=True)
                    sleep(3)
                    v.go_to_custom_game_mode(account_name,password)
                    return
    def exit_valorant():
        for proc in psutil.process_iter(['pid', 'name']):
            if 'valorant' in proc.info['name'].lower():
                pid = proc.info['pid']
                process = psutil.Process(pid)
                process.terminate()
    def get_venue_simple(venueList):
        AllFiles = os.listdir(v.screenshotPath)
        venuList = []
        for i in AllFiles:
            if re.match(r"venue_*", i):
                # print(i)
                venueList.append(i)
        v.getVenue(venueList)
def afk_boss(MainFlow,withpartyRank):
    v.afk_status = True
    count = 1
    eval(MainFlow)
    while True:
        process = core_afk()
        respond = v.tryAndSearch('play_again.png', withoutClick=True, withoutMove=False)
        respondd = v.tryAndSearch('play_after_one_game.png', withoutClick=True, withoutMove=False)
        if respond or respondd:
            print(f'round: {count} done')
            v.check_if_val_message_sent()
            v.requeueRank()
            eval(withpartyRank)
            count +=1
            if count > 8:
                # Get the current time
                now = datetime.now()

                # Format the time as a string
                current_time = now.strftime("%H:%M:%S")

                # Open a file for writing
                with open("current_time.txt", "w") as file:
                    # Write the current time to the file
                    file.write(current_time)
                os.system("shutdown -a")
                os.system("shutdown /s /t 1")
def core_afk():
    # Compile the C++ file
    compile_cmd = ["g++", f"{v.others_path}afk.cpp", "-o", "afk"]
    subprocess.run(compile_cmd, check=True)
    # Run the compiled executable with the x and y coordinates as arguments
    """ drop,shield,abilties """
    run_cmd = [f"{v.others_path}afk", '0', '1', '0']
    """ drop,shield,abilties """
    subprocess.run(run_cmd, check=True)
    return
def afk(buy_shield=False):
    while True:
        core_afk()
def print_instructions(choices):
    for i,choice in enumerate(choices):
        i +=1
        print(f"{i}: {choice}")
def alert_msg(msg):
    print('❗❗❗'* 10 +'\n'+ msg +'\n'+'❗❗❗'* 10 )
def insert_agent(preference, input_value):
    preference.insert(0, input_value)
    alert_msg('new preference: ', str(preference))
def insert_agent(preference, input_value):
    preference.insert(0, input_value)
    alert_msg('new preference: '+ str(preference))
def print_instructions_main(account,choices,game_mode):
    print("  #"*10)
    print('🎅 '+ account+' 🎅')
    print('🧠 '+ game_mode+' 🧠')
    agentXYposition = v.agentXYposition(account)
    v.errorChecking(agentXYposition)
    for i,choice in enumerate(choices):
        i +=1
        print(f"{i}: {choice}")
    input_value = input("\nPlease input:")
    return input_value
available_modes = ['unrated','competitive','spike_rush','swiftplay']
available_agents = ['astra','breach','brimstone','chamber',
                    'cypher','gekko','jett','kayo','killjoy',
                    'neon','omen','phoenix','raze','reyna','sage',
                    'skye','sova','viper','yoru']
preference = {
    # 'ascent':['omen','phoenix','breach'],
    # 'haven': ['omen','phoenix','breach'],
    # 'icebox': ['omen','phoenix','breach'], 
    # 'lotus': ['omen','phoenix','breach'],
    # 'pearl': ['habor','phoenix','breach'],
    # 'split': ['omen','phoenix','breach'],`
    # 'fracture': ['phoenix','breach','omen'],`
    # 'bind': ['omen','phoenix','breach'],
    # 'breeze':['habor','phoenix','breach']


    'pearl': ['habor','phoenix','breach'],
    'ascent':['omen','phoenix','breach'],
    'haven': ['omen','phoenix','breach'], 
    'icebox': ['omen','phoenix','breach'], 
    'lotus': ['omen','phoenix','breach'],
    'split': ['omen','phoenix','breach' ],
    'fracture': ['omen','breach','omen'],
    """  """
    'bind': ['omen','phoenix','breach'],
    'breeze':['habor','phoenix','breach']
}
"""
MainFlow(account, skipStart=False, random=False)
"""
"""config
FatherSun, LaVanTor, speakEngInVal
unrated, competitive, swiftplay, spike_rush
"""
game_mode = 'unrated' 
game_mode = 'spike_rush' 
game_mode = 'competitive'
"""
"""
preference = ['phoenix', 'reyna', 'jett']  
preference = ['yoru', 'chamber', 'raze']
preference = ['reyna', 'jett', 'phoenix']
preference = ['raze', 'reyna', 'phoenix']
preference = ['jett', 'reyna', 'phoenix']  
preference = ['sage', 'brimstone', 'phoenix']
preference = ['omen', 'sage', 'jett']
preference = ['chamber', 'omen', 'phoenix']
""" """
account = 'LaVanTor'
account = 'Dear Curi'
account = 'speakEngInVal'
account = 'oOoOoOo'
account = 'FatherSun'
def hold(game_mode,available_modes):
    MainFlow = "v.MainFlow(account, skipStart='y', reQ='y')"
    withpartyRank = "v.MainFlow(account, skipStart='y')"
    launchAndLogin = "v.MainFlow(account, skipStart='y', reQ='y', launchAndLogin=True)"
    while True:
        input_value = print_instructions_main(account,['main program','report player','requeue','login & queue','afk','check_all_account_available_agent','afk_boss'],game_mode)
        if input_value == "1":
            eval(withpartyRank)
        elif input_value == "2":
            print_instructions(['report','exit','exit & requeuing'])
            time.sleep(1)
            while True:
                if keyboard.is_pressed('1'): 
                    v.reportPlayer()
                elif keyboard.is_pressed('2'):
                    print('exiting..')
                    time.sleep(0.5)
                    break
                elif keyboard.is_pressed('3'):
                    print('exiting and requeuing')
                    time.sleep(1)
                    eval(MainFlow)
                    break
        elif input_value == "3":
            eval(MainFlow)
        elif input_value == "4":
            eval(launchAndLogin)
        elif input_value == "5":
            afk()
        elif input_value == "6":
            v.check_all_account_available_agent()
        elif input_value == "7":
            afk_boss(MainFlow,withpartyRank)
        elif input_value in available_agents:
            insert_agent(preference, input_value)
        else:
            for mode in available_modes:
                if re.match(mode, input_value):
                    game_mode = input_value
                    alert_msg('mode changed: ' + game_mode)
if __name__ == "__main__":
    hold(game_mode,available_modes)
    # v.getAgentsPosition(account=account)
    # v.MainFlow('speakEngInVal') #waiting for m tch found directly
    # v.MainFlow('FatherSun', random='random is on', reQ='y')

# 0;P;c;1;o;1;d;1;z;1;0t;1;0a;1;1b;0