from pyautogui import *
import pyautogui
import time
import keyboard
import random
import os
from datetime import datetime, timedelta, timezone
import os
import os
import csv
import re
import math
import subprocess
import psutil
from PIL import ImageGrab
import pandas as pd
currentPath = os.path.dirname(os.path.abspath(__file__))
dc_path = currentPath +r'\..\..\kmjAUTO\core'
sys.path.insert(0, dc_path)
import discord_send_msg as d
print("initiating...")
class v:
    debugging = 0
    agentSelected = [] 
    currentPath = os.path.dirname(os.path.abspath(__file__))
    currentPath += '\\'
    screenshotPath = currentPath+'source\\'
    others_path = currentPath+'others\\'
    accounts_info_path = currentPath+'accounts_info\\'
    lockX, lockY = 1268, 968
    columns_position = [835,954,1058,1176,1272,1388,1499,1615,1731]
    rows_position = [1121,1228,1340]
    accountCredentials = {
        'FatherSun': ['wonnacha','Pleasetellme3'],
        'LaVanTor': ['wonnacha3','Pleasetellme3'],
        'speakEngInVal': ['wonnacha4','Pleasetellme3'],
        'xav1er': ['wonnacha5','Pleasetellme3'],
        'oOoOoOo': ['wonnacha6','Pleasetellme3'],
        'Dear Curi': ['wonnacha7','Pleasetellme3']
    }
    """ OLD METHOD"""
    #if even number= either select agent/ re queuing
    # saving each account's agent's XY position
    def agentXYpositionOLD(account):
        csv_filename = v.currentPath+ 'agentXYposition.csv'
        agentXYposition = []
        with open(csv_filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['Account'] == account:
                    agentXYposition.append(row)
        if len(agentXYposition) < 4:
            exit('SOMETIME IS NOT RIGHT: len(agentXYposition) < 4')
        print(agentXYposition)
        return agentXYposition
    def getAgentList(account):
        # Read Excel file
        df = pd.read_excel(v.currentPath+'\\availableAgents.xlsx')
        # Display the DataFrame
        # print(df)
        filtered_values = df.loc[df['FatherSun'] == 'o', 'Agent'].tolist()
        # Display the list of values
        # print(filtered_values)
        return filtered_values
    def agentXYposition(account):
        agentList = v.getAgentList(account)
        rows = 3
        columns = 9
        agentList.sort()
        selectedAgent = list()
        for agentName in agentList:
            iIndex = agentList.index(agentName)
            # Calculate the row and column
            row = (iIndex) // columns
            column = (iIndex) % columns
            if (row > rows):
                print('something went wrong')
                exit()
            Xposition = v.columns_position[column]
            Yposition = v.rows_position[row]
            selectedAgent.append({'Agent': agentName, 'Xposition':Xposition,'Yposition':Yposition})
        return selectedAgent    
    """ example {'Date': '20230709', 'Account': 'FatherSun', 'Agent': 'astra', 'Xposition': '710', 'Yposition': '1233'}"""
    """ OLD METHOD"""
    #if even number= either select agent/ re queuing
    # saving each account's agent's XY position
    def agentXYpositionOLD(account):
        csv_filename = v.currentPath+ 'agentXYposition.csv'
        agentXYposition = []
        with open(csv_filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['Account'] == account:
                    agentXYposition.append(row)
        if len(agentXYposition) < 4:
            exit('SOMETIME IS NOT RIGHT: len(agentXYposition) < 4')
        print(agentXYposition)
        return agentXYposition
    def getAgentsPosition(account,auto=False):
        originalLength = 0
        today = datetime.today().strftime(f'%Y%m%d')
        column = ['Date','Account','Agent', 'Xposition', 'Yposition']
        csvFile = f'{v.currentPath}\\agentXYposition.csv'
        lines = list()
        """ get ALL ACCOUNTS' agents positions, except the target account """
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
        v.debugger('new len(lines): '+ str(len(lines)))
        if auto is True:
            v.writerows(csvFile, lines)
            return
        if originalLength < len(lines):
            v.writerows(csvFile, lines)
        else:
            print('  !'*10)
            print('nothing executed: originalLength < new length')
            print('  !'*10)
        print_instructions(["overwite", "pass"],1)
        inputt = input()
        if inputt == "1":
            v.writerows(csvFile, lines)
            print('overwritten')
        elif inputt == "2":
            print('passed')
            pass
    def writerows(csvFile, lines):
        with open(csvFile, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(lines)
                f.close()
    def format_time(elapsed_time):
        m, s = divmod(int(elapsed_time), 60)
        time_format = "{:02d}:{:02d}".format(m, s)
        return time_format
    def searchAndClick(target, needClick=True, confidence=0.8):
        while True:
            try:
                x, y = pyautogui.locateCenterOnScreen(v.screenshotPath+target, region = (0,0,2500,1440), confidence=confidence)
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
        v.stateReport(0,f'queuing',send_dc=0)
        v.cpp_select_agent(999,999)
        while True: 
            if v.tryAndSearch('matchFound.png'):                                                                    
                v.stateReport(1,f'match found',send_dc=False)
                v.getVenue(venueList, agentXYposition)
            pos = v.tryAndSearch('inGame.png')
            if pos is not None:
                v.stateReport(6, 'in game, have fun.',send_dc=0)
                try:
                    v.afk_status
                    for i in range(3):
                        click(pos) 
                        sleep(1)
                except:
                    pass
                v.searchAndClick('buy_phase.png', needClick=False, confidence=0.6)
                v.stateReport(7, 'buying phase',send_dc=0)
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
                    v.stateReport(2,f'map: {venue}',send_dc=False)
                    # click(x, y)                                                                   
                    if agentXYposition is False:
                        break
                    v.selectAgent(v.preference, venue, agentXYposition)
                    break
            except:
                count+=1
        # """ alt tab here """
        # pyautogui.keyDown('alt')
        # pyautogui.press('tab')
        # pyautogui.moveTo(a)
        # pyautogui.keyUp('alt')
        # """ alt tab here """
    def stateReport(tick, msg,send_dc=True):
        total = 7
        cross = total - tick
        print("   ="* 20)
        msg = '✅'*tick+'❌'*cross+' '+msg
        print(msg)
        if type(send_dc) == int:
            v.send_to_discord(msg,send_dc)
        return
    def cpp_select_agent(xaxis,yaxis):
        if xaxis == 999 and yaxis == 999:
            # os.remove(f"{v.others_path}selectagent.exe")
            compile_cmd = ["g++", f"{v.others_path}selectagent.cpp", "-o", "selectagent"]
            subprocess.run(compile_cmd, shell=True, check=True)
        # Run the compiled executable with the x and y coordinates as arguments
        run_cmd = [f"{v.others_path}selectagent.exe", str(xaxis), str(yaxis), str(v.lockX), str(v.lockY)]
        subprocess.run(run_cmd, shell=True, check=True)
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
                    # agnetPosition = i2
                    xaxis = int(i['Xposition'])
                    yaxis = int(i['Yposition'])
                    break
        count = 0
        if repickAgent is False:
            # time.sleep(1)
            v.checkIfLoadingPageDone()
            # time.sleep(1)
        cursorPos = pyautogui.position()
        if v.random:
            v.stateReport(4,f'🍭🍭RANDOM🍭🍭 agent selecting: 🍭  {agent} 🍭',send_dc=False)
        else:
            v.stateReport(4,f'agent selecting: 🕵️  {agent} 🕵️',send_dc=False)
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
        v.cpp_select_agent(xaxis,yaxis)
        if v.checkIfAgentLocked(agentXYposition): 
            order +=1
            alert_msg(f'agent {order} cant be selected')
            v.selectAgent(preference, venue, agentXYposition, order, repickAgent=True)
        else:
            v.stateReport(5,f'agent selected',send_dc=False)
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
        tolerance = 1
        while True:
            if pyautogui.pixelMatchesColor(pixelx, pixelY, (0,0,0), tolerance=tolerance):
                break
        while True:
            if not pyautogui.pixelMatchesColor(pixelx, pixelY, (0,0,0), tolerance=tolerance):
                v.stateReport(3, 'select agent page',send_dc=False)
                return
                count +=1
                print(count)
                if count >50:
                    v.stateReport(3, 'select agent page',send_dc=False)
                    return
            # else:
            #     count +=1
            # if pyautogui.pixelMatchesColor(pixellx, pixellY, (0,0,0), tolerance=tolerance):
            #     count2 = 0
            # else:
            #     count2 +=1
            # if pyautogui.pixelMatchesColor(pixelllx, pixelllY, (0,0,0), tolerance=tolerance):
            #     count3 = 0
            # else:
            #     count3 +=1
            # if count >1 and count2 >1 and count3 >1:
            #     v.stateReport(3, 'select agent page',send_dc=False)
            #     return

    def returnPreviousPosition(x,y):
        a = pyautogui.position()
        pyautogui.click(x, y)
        pyautogui.moveTo(a)
    def slow_click(x,y):
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(x,y)
        pyautogui.click()
    def reportPlayer_first_move():
        print('fuction: reportPlayer is running...')
        pyautogui.click()
        pyautogui.click()
        pyautogui.click(button='right')
        pyautogui.click()
        return True, pyautogui.position()
    def reportPlayer():
        print_instructions(['toxic','sabotaging','afk','submit','breakLoop', 'F1: requeue'])
        a = pyautogui.position()
        first_move_already = False
        while True:
            if keyboard.is_pressed('1'):
                if first_move_already is False:
                    first_move_already, a = v.reportPlayer_first_move()
                    # time.sleep(0.25)
                for x,y in [(523, 547), (521, 587), (525, 684), (528, 721)]:
                    v.slow_click(x,y)
            elif keyboard.is_pressed('2'):
                v.slow_click(1068, 641)
            elif keyboard.is_pressed('3'):
                v.slow_click(1600, 546)
            elif keyboard.is_pressed('4'):
                first_move_already = False
                pyautogui.mouseDown(1282, 1033, duration=0.2)
                pyautogui.mouseUp(1282, 1033)
                time.sleep(0.5)
                v.slow_click(1263, 828)
                pyautogui.moveTo(a)
            elif keyboard.is_pressed('5'):
                break
            elif keyboard.is_pressed('F1'):
                return 1
        return
    # def reportPlayer():
    #     a = pyautogui.position()
    #     first_move_already = False
    #     action_list = set()
    #     while True:
    #         if keyboard.is_pressed('1'):
    #             action_list.add(1)
    #         elif keyboard.is_pressed('2'):
    #             action_list.add(2)
    #         elif keyboard.is_pressed('3'):
    #             action_list.add(3)
    #         elif keyboard.is_pressed('4'):
    #             action_list.add(4)
    #             print(action_list)
    #             time.sleep(1)
    #             action_list = set()
    #         elif keyboard.is_pressed('5'):
    #             action_list.add(5)
    #     pyautogui.moveTo(a)
    def check_if_val_message_sent(loginUsername):
        #check if the message sent
        result_pos = v.tryAndSearch(f'ok_button.png',withoutClick=True, withoutMove=True)
        result_poss = v.tryAndSearch(f'understand.png',withoutClick=True, withoutMove=True)
        if result_pos is not None or result_poss is not None:
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%Y%m%d_%H%M%S")+f"_{loginUsername}"
            screenshot_path = v.currentPath+f'auto_sc\\{formatted_datetime}.png'
            v.screenshot(screenshot_path)
            alert_msg('check message at: '+screenshot_path)
            try:
                click(result_poss)
            except:
                pass
            try:
                click(result_pos)
            except:
                pass
            time.sleep(0.5)
            v.check_if_val_message_sent(loginUsername)
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
                    if loop_times > 1:
                        # print('  -  '*20)
                        return
            loop_times +=1
    def errorChecking(agentXYposition,preference):
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
            print('🕵️  '+str(preference)+ ' 🕵️')
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
            v.stateReport(0,f'autoSelect initiated: {v.account}'+ '\n'+v.random,send_dc=0)
        else:
            v.stateReport(0, f'autoSelect initiated: {v.account}',send_dc=False)
        if skipStart is False:  
            v.searchAndClick('start.png')
        v.getStatus(agentXYposition)
        return
    def next_match(hard_loop,withoutClick=True, withoutMove=True):
        while True:
            respond = v.tryAndSearch('play_again.png', withoutClick, withoutMove)
            if respond is not None:
                return respond
            respondd = v.tryAndSearch('play_after_one_game.png', withoutClick, withoutMove)
            if respondd is not None:
                return respondd
            if hard_loop is False:
                return None
    def requeueRank():
        bb = pyautogui.position()
        while True:
            a = v.tryAndSearch('play_in_lobby.png', withoutClick=False, withoutMove=False)
            if a is not None:
                break
            v.tryAndSearch('play_after_one_game.png', withoutClick=False, withoutMove=False)
        #GAME MODE
        game_mode_image = [f"{v.game_mode}1.png", f"{v.game_mode}2.png"]
        break_loop = False
        while not break_loop:
            for i in game_mode_image:
                x = v.tryAndSearch(i,withoutClick=False, withoutMove=False)
                if x is not None:
                    break_loop = True
                    break
        #start queuing
        v.tryAndSearch('start.png', withoutClick=False, withoutMove=False)
        # click(x=1240, y=1296)
        pyautogui.FAILSAFE = False
        """ alt tab here """
        pyautogui.keyDown('alt')
        pyautogui.press('tab')
        pyautogui.moveTo(bb)
        pyautogui.keyUp('alt')
        """ alt tab here """
    """ in window 10, old home pc"""
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
            """ handling: connection error """

        #retrieve login username and password
        if loginUsername is False and loginPassword is False:
            loginUsername, loginPassword = v.accountCredentials[v.account]
        time.sleep(0.5)
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
                return
        time.sleep(1)
        pyautogui.FAILSAFE = False
        v.check_if_val_message_sent(loginUsername)
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
        for displayName, credential in v.accountCredentials.items():
            account_name = credential[0]
            password = credential[1]
            v.login(account_name,password,direct_launch=True)
            time.sleep(2)
            for pos,fileName in [
                [[(1216, 38), 
                 (1488, 30)],'rank_mission_lv']
                ]:
                for each_pos in pos:
                    click(each_pos)
                    sleep(1)
                sleep(1)
                pyautogui.moveTo(2095, 32)
                current_datetime = datetime.now()
                formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
                screenshot_path = v.accounts_info_path+formatted_datetime+'_'+account_name+f"[{displayName}]"+'_'+fileName+'.png'
                v.screenshot(screenshot_path)
            v.go_to_custom_game_mode(account_name,password)
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_path = v.accounts_info_path+formatted_datetime+'_'+account_name+f"[{displayName}]"+'_available agents'+'.png'
            v.screenshot(screenshot_path)
            print('check screenshot at: ',screenshot_path)
            v.getAgentsPosition(account_name,auto=True)
            v.exit_valorant()
            time.sleep(2)
    def go_to_custom_game_mode(account_name,password):
        click(x=1266, y=33)
        poss = [(1272, 22), (2044, 115), (1211, 1319),(1056, 1000),(1056, 1000),(1056, 1000),(1056, 827),(1056, 827),(1056, 827)]
        for each_pos in poss:
            click(each_pos)
            click(each_pos)
            click(each_pos)
            time.sleep(1)
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
                continue
            if 'riot' in proc.info['name'].lower():
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
    def send_to_discord(msg,channel=0):
        d.send("Val", msg,channel)
        return
    def dc_notification():
        # print("waiting for next phase...")
        # x = 1307  # X-coordinate of the pixel
        # y = 258   # Y-coordinate of the pixel

        # # Get the RGB color value of the pixel at the specified coordinates
        # pixel_color = pyautogui.pixel(x, y)

        # # Check if the pixel color is red
        # if pixel_color == (255, 0, 0):
        #     print("The pixel color is red.")
        # else:
        #     print("The pixel color is not red.")
        while True:
            if v.tryAndSearch('buy_phase.png', withoutClick=True, withoutMove=True):
                v.send_to_discord('buying_phase')
                time.sleep(50)
def afk_boss(MainFlow,withpartyRank,loginUsername):
    v.afk_status = True
    drop = input('drop: ')
    shield = input('shield: ')
    abilties = input('abilties: ')
    if abilties == "1":
        print("1 = click, 2 = double tap key")
        abilties1 = input('abilties1: ')
        abilties2 = input('abilties2: ')
        abilties3 = input('abilties3: ')
        abilties4 = input('abilties4: ')
    else:
        abilties1 = 1
        abilties2 = 1
        abilties3 = 1
        abilties4 = 1
    count = 1
    eval(MainFlow)
    print_parameters = 0
    while True:
        process = core_afk(print_parameters,drop,shield,abilties,abilties1,abilties2,abilties3,abilties4)
        print_parameters+=1
        respond_pos = v.next_match(hard_loop=False,withoutClick=True, withoutMove=True)
        v.debugger(respond_pos)
        if respond_pos:
            print(f'round: {count} done')
            v.check_if_val_message_sent(loginUsername)
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
        
def spammer():
    # Compile the C++ file
    compile_cmd = ["g++", f"{v.others_path}spammer.cpp", "-o", "spammer"]
    subprocess.run(compile_cmd, shell=True, check=True)
    # Run the compiled executable with the x and y coordinates as arguments
    """ drop,shield,abilties """
    run_cmd = [f"{v.others_path}spammer"]
    """ drop,shield,abilties """
    subprocess.run(run_cmd, shell=True, check=True)
    return
def core_afk(print_parameters=0,drop=0,shield=0,abilties=0,abilties1=1,abilties2=1,abilties3=1,abilties4=1):
    # Compile the C++ file
    compile_cmd = ["g++", f"{v.others_path}afk.cpp", "-o", "afk"]
    subprocess.run(compile_cmd, shell=True, check=True)
    # Run the compiled executable with the x and y coordinates as arguments
    """ drop,shield,abilties """
    run_cmd = [f"{v.others_path}afk", str(print_parameters), str(drop),str(shield),str(abilties),str(abilties1),str(abilties2),str(abilties3),str(abilties4)]
    """ drop,shield,abilties """
    subprocess.run(run_cmd, shell=True, check=True)
    return
def afk(drop=0,shield=0,abilties=0):
    print_parameters = 0
    while True:
        core_afk(print_parameters,drop,shield,abilties)
        print_parameters+=1
def print_instructions(choices,each_line=0):
    for i, agent in enumerate(choices, start=1):
        if each_line == 0 :
            print(f"{i}: {agent}\n")
        else:
            if i % each_line == 0:
                print("{:<2}: {:<14}".format(i, agent))
            else:
                print("{:<2}: {:<14}".format(i, agent), end="")
                if len(choices) == i:
                    print("\n")
def starting():
    choice = ["self-define","default"]
    print_instructions(choice,4)
    ans = input()
    if ans == "1":
        v.account, v.game_mode, v.preference = get_parameters()
    elif ans == "2":
        return
def alert_msg(msg):
    print('❗❗❗'* 10 +'\n'+ msg +'\n'+'❗❗❗'* 10 )
def insert_agent(preference, input_value):
    preference.insert(0, input_value)
    alert_msg('new preference: '+str(preference))
def print_instructions_main(account,choices,game_mode,preference):
    print("  #"*10)
    print('🎅 '+ account+' 🎅')
    print('🧠 '+ game_mode+' 🧠')
    agentXYposition = v.agentXYposition(account)
    v.errorChecking(agentXYposition,preference)
    for i,choice in enumerate(choices):
        i +=1
        print(f"{i}: {choice}")
    input_value = input("\nPlease input:")
    return input_value
def get_parameters():
    print_instructions(account_list,2)
    account = input()
    print("  ^"*15)
    account = account_list[int(account)-1]
    print_instructions(available_modes,2)
    game_mode = input()
    print("  ^"*15)
    game_mode = available_modes[int(game_mode)-1]
    agentXYposition = v.agentXYposition(account)
    availableAgent = []
    for i in agentXYposition:
        availableAgent.append(i['Agent'])
    print_instructions(availableAgent,4)
    preference = list()
    while True:
        agent = input()
        if agent in availableAgent:
            preference.append(agent)
        else:
            try:
                preference.append(availableAgent[int(agent)-1])
            except:
                print(f'Enter again current: {str(preference)}')
        print("  ^"*15)
        if len(preference) >=2:
            break
    return account, game_mode, preference
available_modes = ['unrated','competitive','swiftplay','spike_rush']
available_agents = ['harbor','deadlock','iso','astra','breach','brimstone','chamber',
                    'cypher','gekko','jett','kayo','killjoy',
                    'neon','omen','phoenix','raze','reyna','sage',
                    'skye','sova','viper','yoru']
account_list = ['FatherSun','LaVanTor','speakEngInVal','Dear Curi','oOoOoOo']
v.preference = {
    'breeze':['neon','phoenix','breach'],
    'ascent':['raze','phoenix','breach'],
    'sunset':['pheonix','phoenix','breach'],
    'haven': ['pheonix','phoenix','breach'], 
    'lotus': ['pheonix','phoenix','breach'],
    'split': ['pheonix','phoenix','breach' ],
    'bind': ['pheonix','phoenix','breach'],
    'icebox': ['omen','phoenix','breach'], 
    'pearl': ['harbor','phoenix','breach'],
    'fracture': ['omen','breach','omen']
}
v.preference = {
    'pearl': ['harbor','phoenix','breach'],
    'breeze':['viper','phoenix','breach'],
    'ascent':['omen','phoenix','breach'],
    'sunset':['omen','phoenix','breach'],
    'haven': ['omen','phoenix','breach'], 
    'lotus': ['omen','phoenix','breach'],
    'split': ['omen','phoenix','breach' ],
    'bind': ['omen','phoenix','breach'],
    'icebox': ['omen','phoenix','breach'], 
    'fracture': ['omen','breach','omen']
}
v.game_mode = 'swiftplay'
v.game_mode = 'spike_rush' 
v.game_mode = 'unrated' 
v.game_mode = 'competitive'
"""
"""
v.preference = ['chamber', 'omen', 'phoenix']
v.preference = ['raze', 'reyna', 'phoenix']
v.preference = ['brimstone', 'sage', 'phoenix']
v.preference = ['gekko', 'phoenix', 'jett']  
v.preference = ['jett', 'reyna', 'phoenix']
v.preference = ['omen', 'sage', 'jett']
v.preference = ['skye', 'jett', 'phoenix']
v.preference = ['reyna', 'jett', 'phoenix']
v.preference = ['phoenix', 'jett', 'sage']
v.preference = ['yoru', 'chamber', 'raze']
""" """
v.account = 'oOoOoOo'
v.account = 'speakEngInVal'
v.account = 'xav1er'
v.account = 'FatherSun'
v.account = 'Dear Curi'
v.account = 'LaVanTor'
def hold(game_mode,available_modes):
    MainFlow = "v.MainFlow(v.account, skipStart='y', reQ='y')"
    withpartyRank = "v.MainFlow(v.account, skipStart='y')"
    launchAndLogin = "v.MainFlow(v.account, skipStart='y', reQ='y', launchAndLogin=True)"
    # starting()
    while True:
        input_value = print_instructions_main(v.account,['main program','report player','requeue','login & queue','afk','check_all_account_available_agent','afk_boss','spammer','dc_notification',"getAgentsPosition"],v.game_mode,v.preference)
        if input_value == "1":
            eval(withpartyRank)
        elif input_value == "2":
            if v.reportPlayer() == 1:
                print('exiting and requeuing')
                time.sleep(1)
                eval(MainFlow)
                break
        elif input_value == "3":
            eval(MainFlow)
        elif input_value == "4":
            eval(launchAndLogin)
        elif input_value == "5":
            afk(drop=1,shield=0,abilties=0)
        elif input_value == "6":
            v.check_all_account_available_agent()
        elif input_value == "7":
            afk_boss(MainFlow,withpartyRank,v.account)
        elif input_value == "8":
            spammer()
        elif input_value == "9":
            v.dc_notification()
        elif input_value == "0":
            v.getAgentsPosition(account=v.account)
        elif input_value in available_agents:
            insert_agent(v.preference, input_value)
        else:
            for mode in available_modes:
                if re.match(mode, input_value):
                    game_mode = input_value
                    alert_msg('mode changed: ' + game_mode)
def testing():
    thelist = v.agentXYposition("FatherSun")
    for i in thelist:
        print(i["Agent"])
        xaxis = int(i['Xposition'])
        yaxis = int(i['Yposition'])
        pyautogui.moveTo(xaxis,yaxis)
if __name__ == "__main__":
    # afk(drop=0,shield=0,abilties=1)
    # testing()
    hold(v.game_mode,available_modes)
    # v.getAgentsPosition(account=v.account)

    # v.MainFlow(v.account, skipStart='y')
    # v.MainFlow('speakEngInVal') #waiting for m tch found directly
    # v.MainFlow('FatherSun', random='random is on', reQ='y')

# """ 0;P;c;1;o;1;d;1;z;1;0t;1;0a;1;1b;0 """
# 0;P;c;5;h;0;0l;1;0o;1;0a;1;0f;0;1b;0