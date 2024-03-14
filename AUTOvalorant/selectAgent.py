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
"""  """
""" better account variables manage: in game name, ac, pw """
"""  """
class v:
    def system_preference(self):
        self.preference = {
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
        self.preference = {
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
        self.preference = {
            'breeze':['neon','phoenix','breach'],
            'ascent':['yoru','phoenix','breach'],
            'sunset':['yoru','phoenix','breach'],
            'haven': ['yoru','phoenix','breach'], 
            'lotus': ['yoru','phoenix','breach'],
            'split': ['yoru','phoenix','breach' ],
            'bind': ['yoru','phoenix','breach'],
            'icebox': ['omen','phoenix','breach'], 
            'pearl': ['harbor','phoenix','breach'],
            'fracture': ['omen','breach','omen']
        }
        """  """
        self.preference = ['chamber', 'omen', 'phoenix']
        self.preference = ['raze', 'reyna', 'phoenix']
        self.preference = ['brimstone', 'sage', 'phoenix']
        self.preference = ['gekko', 'phoenix', 'jett']  
        self.preference = ['jett', 'reyna', 'phoenix']
        self.preference = ['omen', 'sage', 'jett']
        self.preference = ['skye', 'jett', 'phoenix']
        self.preference = ['reyna', 'jett', 'phoenix']
        self.preference = ['iso', 'yoru', 'omen']
        self.preference = ['yoru', 'gekko', 'omen']
        self.preference = ['gekko', 'yoru', 'omen']
        self.preference = ['phoenix', 'jett', 'sage'] #basic
        """  """
        self.account = self.wonna6
        self.account = self.wonna7
        self.account = self.wonna
        self.account = self.wonna5
        self.account = self.wonna3
        self.account = self.wonna4
        """  """
        self.game_mode = 'swiftplay'
        self.game_mode = 'spike_rush' 
        self.game_mode = 'unrated' 
        self.game_mode = 'competitive'
        """"""
        """  """
        """  """
        """  """
    def __init__(self):
        self.debugging = 0
        self.agentSelected = [] 
        self.currentPath = os.path.dirname(os.path.abspath(__file__))
        self.currentPath += '\\'
        self.screenshotPath = self.currentPath+'source\\'
        self.others_path = self.currentPath+'others\\'
        self.accounts_info_path = self.currentPath+'accounts_info\\'
        self.lockX, self.lockY = 1268, 968
        self.columns_position = [835,954,1058,1176,1272,1388,1499,1615,1731]
        self.rows_position = [1121,1228,1340]
        # FaiDeLah
        self.wonna = 'FatherSun'
        self.wonna3 = 'LaVanTor'
        self.wonna4 = 'yodasgini'
        self.wonna6 = 'LatdaWn'
        self.wonna7 = 'Dear Curi'
        self.wonna5 = 'xav1er'
        self.accountCredentials = {
            self.wonna: ['wonnacha','Pleasetellme3'],
            self.wonna3: ['wonnacha3','Pleasetellme3'],
            self.wonna4: ['wonnacha4','Pleasetellme3'],
            self.wonna5: ['wonnacha5','Pleasetellme3'],
            self.wonna6: ['wonnacha6','Pleasetellme3'],
            self.wonna7: ['wonnacha7','Pleasetellme3']
        }
        self.available_modes = ['unrated','competitive','swiftplay','spike_rush']
        self.available_agents = ['harbor','deadlock','iso','astra','breach','brimstone','chamber',
                    'cypher','gekko','jett','kayo','killjoy',
                    'neon','omen','phoenix','raze','reyna','sage',
                    'skye','sova','viper','yoru']
        self.account_list = [self.wonna,self.wonna3,self.wonna4,self.wonna5,self.wonna6,self.wonna7]
        self.system_preference()
    def agentXYpositionOLD(self,account):
        csv_filename = self.currentPath+ 'agentXYposition.csv'
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
    def getAgentList(self,account):
        # Read Excel file
        df = pd.read_excel(self.currentPath+'\\availableAgents.xlsx')
        # Display the DataFrame
        # print(df)
        filtered_values = df.loc[df[account].notnull(), 'Agent'].tolist()
        # Display the list of values
        # print(filtered_values)
        return filtered_values
    def agentXYposition(self,account):
        agentList = self.getAgentList(account)
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
            Xposition = self.columns_position[column]
            Yposition = self.rows_position[row]
            selectedAgent.append({'Agent': agentName, 'Xposition':Xposition,'Yposition':Yposition})
        return selectedAgent    
    """ example {'Date': '20230709', 'Account': wonna, 'Agent': 'astra', 'Xposition': '710', 'Yposition': '1233'}"""
    """ OLD METHOD"""
    #if even number= either select agent/ re queuing
    # saving each account's agent's XY position
    def agentXYpositionOLD(self,account):
        csv_filename = self.currentPath+ 'agentXYposition.csv'
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
    @staticmethod
    def writerows(self,csvFile, lines):
        with open(csvFile, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(lines)
            f.close()
    @staticmethod
    def format_time(elapsed_time):
        m, s = divmod(int(elapsed_time), 60)
        time_format = "{:02d}:{:02d}".format(m, s)
        return time_format
    def searchAndClick(self,target, needClick=True, confidence=0.8):
        while True:
            try:
                x, y = pyautogui.locateCenterOnScreen(self.screenshotPath+target, region = (0,0,2500,1440), confidence=confidence)
                if (x, y) is not None:
                    if needClick is True:
                        v.returnPreviousPosition(x,y)
                    return x,y
                else:
                    print('nope')
            except:
                pass
    def tryAndSearch(self,target, withoutClick=True, withoutMove=True):
        try:
            x, y = pyautogui.locateCenterOnScreen(self.screenshotPath+target, region = (0,0,2500,1440), confidence=0.85)
            if (x, y) is not None:
                if withoutMove is not True:
                    pyautogui.moveTo(x, y)
                if withoutClick is not True:
                    click()
                return x,y
        except:
            # print('no msg found')
            return
    def getStatus(self,agentXYposition, secondRun=False):
        AllFiles = os.listdir(self.screenshotPath)
        venueList = []
        for i in AllFiles:
            if re.match(r"venue_*", i):
                # print(i)
                 venueList.append(i)
        self.stateReport(0,f'queuing',send_dc=0)
        self.cpp_select_agent(999,999)
        while True: 
            if self.tryAndSearch('matchFound.png'):
                self.stateReport(1,f'match found',send_dc=False)
                self.getVenue(venueList, agentXYposition)
            pos = self.tryAndSearch('inGame.png')
            if pos is not None:
                self.stateReport(6, 'loading in game, have fun.',send_dc=0)
                self.current_gaming_section_screenshot()
                try:
                    self.afk_status
                    for i in range(3):
                        click(pos) 
                        sleep(1)
                except:
                    pass
                self.searchAndClick('buy_phase.png', needClick=False, confidence=0.6)
                self.stateReport(7, 'buying phase',send_dc=0)
                return
            else:
                pass
    def getVenue(self,venueList, agentXYposition=False):
        a = pyautogui.position()
        count = 0
        while True:
            searchingVenue = venueList[count%len(venueList)]
            try:
                x, y = pyautogui.locateCenterOnScreen(self.screenshotPath+searchingVenue, region = (715,0,1100,1440), confidence=0.8)
                if x is not None:
                    venue = searchingVenue.replace("venue_", "")
                    venue = venue[:int(venue.find('.'))]
                    self.stateReport(2,f'map: {venue}',send_dc=False)
                    # click(x, y)                                                                   
                    if agentXYposition is False:
                        break
                    self.selectAgent(self.preference, venue, agentXYposition)
                    break
            except:
                count+=1
        # """ alt tab here """
        # pyautogui.keyDown('alt')
        # pyautogui.press('tab')
        # pyautogui.moveTo(a)
        # pyautogui.keyUp('alt')
        # """ alt tab here """
    def stateReport(self,tick, msg,send_dc=True):
        total = 7
        cross = total - tick
        print("   ="* 20)
        msg = '✅'*tick+'❌'*cross+' '+msg
        print(msg)
        if type(send_dc) == int:
            self.send_to_discord(msg,send_dc)
        return
    def cpp_select_agent(self,xaxis,yaxis):
        if xaxis == 999 and yaxis == 999:
            # os.remove(f"{self.others_path}selectagent.exe")
            compile_cmd = ["g++", f"{self.others_path}selectagent.cpp", "-o", "selectagent"]
            subprocess.run(compile_cmd, shell=True, check=True)
        # Run the compiled executable with the x and y coordinates as arguments
        run_cmd = [f"{self.others_path}selectagent.exe", str(xaxis), str(yaxis), str(self.lockX), str(self.lockY)]
        subprocess.run(run_cmd, shell=True, check=True)
    def selectAgent(self,preference, venue, agentXYposition, order=0, repickAgent=False):
        if self.random:
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
            self.agentSelected.append(agent)
            for i in agentXYposition:
                if i['Agent'] == agent:
                    # agnetPosition = i2
                    xaxis = int(i['Xposition'])
                    yaxis = int(i['Yposition'])
                    break
        if repickAgent is False:
            # time.sleep(1)
            self.checkIfLoadingPageDone()
            # time.sleep(1)
        cursorPos = pyautogui.position()
        if self.random:
            self.stateReport(4,f'🍭🍭RANDOM🍭🍭 agent selecting: 🍭  {agent} 🍭',send_dc=False)
        else:
            self.stateReport(4,f'agent selecting: 🕵️  {agent} 🕵️',send_dc=False)
            self.debugger('after agent sel')
        """  """
        self.cpp_select_agent(xaxis,yaxis)
        if self.checkIfAgentLocked(agentXYposition): 
            order +=1
            self.alert_msg(f'agent {order} cant be selected')
            self.selectAgent(preference, venue, agentXYposition, order, repickAgent=True)
        else:
            self.stateReport(5,f'agent selected',send_dc=False)
            pyautogui.FAILSAFE = False
            """ alt tab here """
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.moveTo(cursorPos)
            pyautogui.keyUp('alt')
            """ alt tab here """
    def checkIfAgentLocked(self,agentXYposition):
        self.debugger('agentXYposition:\n')
        self.debugger(agentXYposition)
        new_items = [d for d in agentXYposition if 'Agent' not in d or d['Agent'] not in self.agentSelected]
        agentXYposition = new_items

        shuffleList = random.sample(agentXYposition, len(agentXYposition))
        # end_time = time.perf_counter()

        # elapsed_time = end_time - start_time

        # print(f'Time elapsed: {elapsed_time:.6f} seconds')
        self.debugger('  =   =   =')
        self.debugger('shuffleList:\n')
        self.debugger(shuffleList)
        for i in shuffleList[:6]:
            xaxis = int(i['Xposition'])
            yaxis = int(i['Yposition'])
            pyautogui.click(xaxis,yaxis)
            if self.tryAndSearch('availableAgent.png', withoutClick=True):
                return 'notSelected'
    def checkIfLoadingPageDone(self):
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
                self.stateReport(3, 'select agent page',send_dc=False)
                return
    @staticmethod
    def returnPreviousPosition(x,y):
        a = pyautogui.position()
        pyautogui.click(x, y)
        pyautogui.moveTo(a)
    @staticmethod
    def slow_click(x,y):
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(x,y)
        pyautogui.click()
    @staticmethod
    def reportPlayer_first_move():
        print('fuction: reportPlayer is running...')
        pyautogui.click()
        pyautogui.click()
        pyautogui.click(button='right')
        pyautogui.click()
        return True, pyautogui.position()
    def inner_function(self,a):
        pyautogui.mouseDown(1282, 1033, duration=0.2)
        pyautogui.mouseUp(1282, 1033)
        time.sleep(0.5)
        self.slow_click(1263, 828)
        pyautogui.moveTo(a)
    def reportPlayer(self):
        self.print_instructions(['toxic','sabotaging','afk','submit','breakLoop', 'F1: requeue'])
        a = pyautogui.position()
        first_move_already = False
        while True:
            if keyboard.is_pressed('1'):
                if first_move_already is False:
                    first_move_already, a = self.reportPlayer_first_move()
                    # time.sleep(0.25)
                for x,y in [(523, 547), (521, 587), (525, 684), (528, 721),(1068, 641),(1600, 546),(648, 935)]:
                    self.slow_click(x,y)
            elif keyboard.is_pressed('2'):
                self.slow_click(1068, 641)
            elif keyboard.is_pressed('3'):
                self.slow_click(1600, 546)
            elif keyboard.is_pressed('4'):
                first_move_already = False
                self.inner_function(a)
            elif keyboard.is_pressed('5'):
                self.inner_function(a)
                break
            elif keyboard.is_pressed('F1'):
                return 1
        return
    def check_if_val_message_sent(self,loginUsername):
        #check if the message sent
        result_pos = self.tryAndSearch(f'ok_button.png',withoutClick=True, withoutMove=True)
        result_poss = self.tryAndSearch(f'understand.png',withoutClick=True, withoutMove=True)
        if result_pos is not None or result_poss is not None:
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%Y%m%d_%H%M%S")+f"_{loginUsername}"
            screenshot_path = self.currentPath+f'auto_sc\\{formatted_datetime}.png'
            self.screenshot(screenshot_path)
            self.alert_msg('check message at: '+screenshot_path)
            try:
                click(result_poss)
                click(result_poss)
                click(result_poss)
            except:
                pass
            try:
                click(result_pos)
                click(result_pos)
                click(result_pos)
            except:
                pass
            for i in range(3):
                click(1280, 450)
            time.sleep(1)
            self.check_if_val_message_sent(loginUsername)
        return
    @staticmethod
    def full_path_name_to_three_parts(fileName):
        dir_path, full_name = os.path.split(fileName)
        file_name, file_ext = os.path.splitext(full_name)
        return dir_path,file_name,file_ext
    def screenshot(self,screenshot_path,previous_file='',loop_times=0,compare_size=0):
        dir_path,file_name,file_ext = self.full_path_name_to_three_parts(screenshot_path)
        tmp_screenshot_path = dir_path+'\\'+file_name+'_1'+file_ext       
        # Take a screenshot of the entire screen
        screenshot = ImageGrab.grab()
        # Save the screenshot to a file
        screenshot.save(screenshot_path)
        current_size = self.wait_for_file_found(screenshot_path) 
        while True:
            # Take a screenshot of the entire screen
            screenshot = ImageGrab.grab()
            # Save the screenshot to a file
            screenshot.save(tmp_screenshot_path)
            tmp_size = self.wait_for_file_found(tmp_screenshot_path)
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
    def errorChecking(self,agentXYposition):
        availableAgent = []
        possibleAgent = []
        for i in agentXYposition:
            availableAgent.append(i['Agent'])
        if type(self.preference) is dict:
            print(''+'map'+'')
            mySet = set()
            tmp = self.preference.values()
            for iList in tmp:
                for i in iList:
                    mySet.add(i)
            possibleAgent = list(mySet)
        elif type(self.preference) is list:
            print('🕵️  '+str(self.preference)+ ' 🕵️')
            possibleAgent = self.preference
        else:
            exit('UNKNOWN DATA TYPE')
        for a in possibleAgent:
            if a not in availableAgent:
                print('possibleAgent:   ')
                print(possibleAgent)
                print('availableAgent:  ')
                print(availableAgent)
                print(f'{a} is not available in this account!!!')
                exit()
    def debugger(self,msg):
        if self.debugging == 1:
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%H-%M-%S")
            print(f'debug-[{formatted_datetime}]: {msg}')
    def MainFlow(self, skipStart=False, random=False, reQ=False,launchAndLogin=False):
        self.random = random
        agentXYposition = self.agentXYposition(self.account)
        if launchAndLogin:
            self.login()
        if reQ:
            self.requeue_game()
        if self.random:
            self.stateReport(0,f'autoSelect initiated: {self.account}'+ '\n'+self.random,send_dc=0)
        else:
            self.stateReport(0, f'autoSelect initiated: {self.account}',send_dc=False)
        if skipStart is False:  
            self.searchAndClick('start.png')
        self.getStatus(agentXYposition)
        return
    def next_match(self,hard_loop,withoutClick=True, withoutMove=True):
        while True:
            respond = self.tryAndSearch('play_again.png', withoutClick, withoutMove)
            if respond is not None:
                return respond
            respondd = self.tryAndSearch('play_after_one_game.png', withoutClick, withoutMove)
            if respondd is not None:
                return respondd
            if hard_loop is False:
                return None
    def requeue_game(self):
        bb = pyautogui.position()
        while True:
            a = self.tryAndSearch('play_in_lobby.png', withoutClick=False, withoutMove=False)
            if a is not None:
                break
            self.tryAndSearch('play_after_one_game.png', withoutClick=False, withoutMove=False)
        #GAME MODE
        game_mode_image = [f"{self.game_mode}1.png", f"{self.game_mode}2.png"]
        break_loop = False
        while not break_loop:
            for i in game_mode_image:
                x = self.tryAndSearch(i,withoutClick=False, withoutMove=False)
                if x is not None:
                    break_loop = True
                    break
        #start queuing
        self.tryAndSearch('start.png', withoutClick=False, withoutMove=False)
        # click(x=1240, y=1296)
        pyautogui.FAILSAFE = False
        """ alt tab here """
        pyautogui.keyDown('alt')
        pyautogui.press('tab')
        pyautogui.moveTo(bb)
        pyautogui.keyUp('alt')
        """ alt tab here """
    """ in window 10, old home pc"""
    def login(self,loginUsername=False,loginPassword=False,direct_launch=False):
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
                x,y = pyautogui.locateCenterOnScreen(self.screenshotPath+'username.png', region = (0,0,2560,1440), confidence=0.8)
                if x is not None:
                    break
            except:
                pass
            try:
                x,y = pyautogui.locateCenterOnScreen(self.screenshotPath+'usernamee.png', region = (0,0,2560,1440), confidence=0.8)
                if x is not None:
                    break
            except:
                pass
            """ handling: connection error """

        #retrieve login username and password
        if loginUsername is False and loginPassword is False:
             loginUsername, loginPassword = self.accountCredentials[self.account]
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
                play_x,play_y = pyautogui.locateCenterOnScreen(self.screenshotPath+'play.png', region = (0,0,2560,1440), confidence=0.7)
                if play_x is not None:
                    break
            except:
                pass
            # try:
            #     xx = pyautogui.locateCenterOnScreen(self.screenshotPath+'riot_client_valorant_icon.png', region = (0,0,2560,1440), confidence=0.7)
            #     if xx is not None:
            #         click(xx)
            # except:
            #     pass
            try:
                aa = pyautogui.locateCenterOnScreen(self.screenshotPath+'riot_client_play_icon.png', region = (0,0,2560,1440), confidence=0.7)
                if aa is not None:
                    click(aa)
            except:
                pass
            elapsed_time = time.time() - start_time
            allowed_time = 60
            if elapsed_time > allowed_time:
                self.debugger(f'OVER {allowed_time} SECONDS!!!!')
                self.debugger('restarting')
                self.exit_valorant()
                sleep(3)
                self.login(loginUsername,loginPassword,direct_launch=True)
                sleep(3)
                return
        time.sleep(1)
        pyautogui.FAILSAFE = False
        self.check_if_val_message_sent(loginUsername)
        click(play_x,play_y)
        self.debugger(f'click({play_x},{play_y})')
        return
    def wait_for_file_found(self,file):
        while True:
            if os.path.isfile(file):
                self.debugger('file found: '+ file)
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
    def check_all_account_available_agent(self,secondTime=False):
        for displayName, credential in self.accountCredentials.items():
            account_name = credential[0]
            password = credential[1]
            self.login(account_name,password,direct_launch=True)
            time.sleep(2)
            for fileName in [
                'rank_mission_lv'
                ]:
                self.searchAndClick('career.png', needClick=True, confidence=0.8)
                sleep(1)
                pyautogui.moveTo(2095, 32)
                current_datetime = datetime.now()
                formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
                screenshot_path = self.accounts_info_path+formatted_datetime+'_'+account_name+f"[{displayName}]"+'_'+fileName+'.png'
                self.screenshot(screenshot_path)
            self.go_to_custom_game_mode(account_name,password)
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_path = self.accounts_info_path+formatted_datetime+'_'+account_name+f"[{displayName}]"+'_available agents'+'.png'
            self.screenshot(screenshot_path)
            print('check screenshot at: ',screenshot_path)
            # v.getAgentsPosition(account_name,auto=True)
            self.exit_valorant()
            time.sleep(2)
    def go_to_custom_game_mode(self,account_name,password):
        click(x=1266, y=33)
        poss = [(1272, 22), (2044, 115), (1211, 1319),(1056, 1000),(1056, 1000),(1056, 1000),(1056, 827),(1056, 827),(1056, 827)]
        for each_pos in poss:
            click(each_pos)
            click(each_pos)
            click(each_pos)
            time.sleep(1)
        start_time = time.time()
        for i in ['agent_sage.png','agent_phoenix.png','agent_brimstone.png']:
            self.debugger('looking for: '+i)
            while True:
                try:
                    target = self.screenshotPath+i
                    x,y = pyautogui.locateCenterOnScreen(target, region = (0,0,2500,1440), confidence=0.9)
                    moveTo(x,y)
                    self.debugger(i + ' found')
                    break
                except:
                    pass
                elapsed_time = time.time() - start_time
                allowed_time = 30
                if elapsed_time > allowed_time:
                    self.debugger(f'OVER {allowed_time} SECONDS!!!!')
                    self.debugger('restarting')
                    self.exit_valorant()
                    sleep(3)
                    self.login(account_name,password,direct_launch=True)
                    sleep(3)
                    self.go_to_custom_game_mode(account_name,password)
                    return
    @staticmethod
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
    @staticmethod
    def send_to_discord(msg,channel=0):
        d.send("Val", msg,channel)
        return
    def dc_notification(self):
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
            if self.tryAndSearch('buy_phase.png', withoutClick=True, withoutMove=True):
                v.send_to_discord('buying_phase')
                time.sleep(50)
    @staticmethod
    def alert_msg(msg):
        print('❗❗❗'* 10 +'\n'+ msg +'\n'+'❗❗❗'* 10 )
    def afk_boss(self,MainFlow,withpartyRank,loginUsername):
        self.afk_status = True
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
            process = self.core_afk(print_parameters,drop,shield,abilties,abilties1,abilties2,abilties3,abilties4)
            print_parameters+=1
            respond_pos = self.next_match(hard_loop=False,withoutClick=True, withoutMove=True)
            self.debugger(respond_pos)
            if respond_pos:
                print(f'round: {count} done')
                self.check_if_val_message_sent(loginUsername)
                self.requeue_game()
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
    def spammer(self):
        # Compile the C++ file
        compile_cmd = ["g++", f"{self.others_path}spammer.cpp", "-o", "spammer"]
        subprocess.run(compile_cmd, shell=True, check=True)
        # Run the compiled executable with the x and y coordinates as arguments
        """ drop,shield,abilties """
        run_cmd = [f"{self.others_path}spammer"]
        """ drop,shield,abilties """
        subprocess.run(run_cmd, shell=True, check=True)
        return
    def core_afk(self,print_parameters=0,drop=0,shield=0,abilties=0,abilties1=1,abilties2=1,abilties3=1,abilties4=1):
        # Compile the C++ file
        compile_cmd = ["g++", f"{self.others_path}afk.cpp", "-o", "afk"]
        subprocess.run(compile_cmd, shell=True, check=True)
        # Run the compiled executable with the x and y coordinates as arguments
        """ drop,shield,abilties """
        run_cmd = [f"{self.others_path}afk", str(print_parameters), str(drop),str(shield),str(abilties),str(abilties1),str(abilties2),str(abilties3),str(abilties4)]
        """ drop,shield,abilties """
        subprocess.run(run_cmd, shell=True, check=True)
        return
    def afk(self,drop=0,shield=0,abilties=0):
        print_parameters = 0
        while True:
            self.core_afk(print_parameters,drop,shield,abilties)
            print_parameters+=1
    @staticmethod
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
    def current_gaming_section_screenshot(self):
        pyautogui.screenshot(f"current_session.png")
        return
    def starting(self):
        choice = ["self-define","default"]
        self.print_instructions(choice,4)
        ans = input()
        if ans == "1":
            self.account, self.game_mode, self.preference = self.get_parameters()
        elif ans == "2":
            return
    def insert_agent(self,input_value):
        self.preference.insert(0, input_value)
        self.alert_msg('new preference: '+str(self.preference))
        return
    def print_instructions_main(self,choices):
        print("  #"*10)
        print('🎅 '+ self.account+' 🎅')
        print('🧠 '+ self.game_mode+' 🧠')
        agentXYposition = self.agentXYposition(self.account)
        self.errorChecking(agentXYposition)
        for i,choice in enumerate(choices):
            i +=1
            print(f"{i}: {choice}")
        input_value = input("\nPlease input:")
        return input_value
    def get_parameters(self):
        #account
        self.print_instructions(self.account_list,2)
        account = input()
        print("  ^"*15)
        self.account = self.account_list[int(account)-1]
        #game mode
        self.print_instructions(self.available_modes,2)
        game_mode = input()
        print("  ^"*15)
        self.game_mode = self.available_modes[int(game_mode)-1]
        #agent
        agentXYposition = self.agentXYposition(account)
        availableAgent = []
        for i in agentXYposition:
            availableAgent.append(i['Agent'])
        self.print_instructions(availableAgent,4)
        self.preference = list()
        while True:
            agent = input()
            if agent in availableAgent:
                self.preference.append(agent)
            else:
                try:
                    self.preference.append(availableAgent[int(agent)-1])
                except:
                    print(f'Enter again, current: {str(self.preference)}')
            print("  ^"*15)
            if len(self.preference) >=2:
                break
        return
    def hold(self):
        MainFlow = "self.MainFlow(skipStart='y', reQ='y')"
        withpartyRank = "self.MainFlow(skipStart='y')"
        launchAndLogin = "self.MainFlow(skipStart='y', reQ='y', launchAndLogin=True)"
        # starting()
        while True:
            input_value = self.print_instructions_main(['main program','report player','requeue','login & queue','afk','check_all_account_available_agent','afk_boss','spammer','dc_notification'])
            if input_value == "1":
                eval(withpartyRank)
            elif input_value == "2":
                if self.reportPlayer() == 1:
                    print('exiting and requeuing')
                    time.sleep(1)
                    eval(MainFlow)
                    break
            elif input_value == "3":
                eval(MainFlow)
            elif input_value == "4":
                eval(launchAndLogin)
            elif input_value == "5":
                self.afk(drop=1,shield=0,abilties=0)
            elif input_value == "6":
                self.check_all_account_available_agent()
            elif input_value == "7":
                self.afk_boss(MainFlow,withpartyRank,self.account)
            elif input_value == "8":
                self.spammer()
            elif input_value == "9":
                self.dc_notification()
            # elif input_value == "0":
            #     v.getAgentsPosition(account=v.account)
            elif input_value in self.available_agents:
                self.insert_agent(input_value)
            else:
                for mode in self.available_modes:
                    if re.match(mode, input_value):
                        self.game_mode = input_value
                        self.alert_msg('mode changed: ' + self.game_mode)
"""  """
"""  """
"""  """
"""  """
""" here  """
"""  """
"""  """
"""  """
#descr: checking X Y position of agents
def testing():
    thelist = v.agentXYposition("FatherSun")
    for i in thelist:
        print(i["Agent"])
        xaxis = int(i['Xposition'])
        yaxis = int(i['Yposition'])
        pyautogui.moveTo(xaxis,yaxis)
if __name__ == "__main__":
    v = v()
    # afk(drop=0,shield=0,abilties=1)
    # testing()
    v.hold()   
    # v.MainFlow(wonna, random='random is on', reQ='y')

# """ 0;P;c;1;o;1;d;1;z;1;0t;1;0a;1;1b;0 """
# 0;P;c;5;h;0;0l;1;0o;1;0a;1;0f;0;1b;0