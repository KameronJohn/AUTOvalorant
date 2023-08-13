import pyautogui
import keyboard
import os
import sys
import csv
from datetime import datetime
import time
currentPath = os.path.dirname(os.path.abspath(__file__))
dc_path = currentPath +r'\..\..\kmjAUTO\core'
sys.path.insert(0, dc_path)
import discord_send_msg as d
class apex:
    def __init__(self):
        self.currentPath = os.path.dirname(os.path.abspath(__file__))
        self.currentPath += '\\'
        self.screenshotPath = self.currentPath+'apex_source\\'
        self.others_path = self.currentPath+'others\\'
        self.accounts_info_path = self.currentPath+'accounts_info\\'
        self.debugging = 1
        self.solo_agent = 'seer'
        self.d_message = {
            "in_apex_game.png":"loading in game",
            "in_dropship.png":"🚢 in drop ship 🚢",
            "in_dropshipp.png":"☄️ dropping ☄️",
            "squad_eliminated.png":"☠️ squad eliminated ☠️",
            "respawning.png":"🍀 respawning 🍀",
            "gameFound.png":f"🫡 game found 🫡",
            "you_are_jumpmaster.png":"❗️ you are jumpmaster ❗️",
            "assigned":"🤦‍♀️ you are jumpmaster 🤦‍♀️"
        }
    def searchAndClick(self,target, needClick=True):
        self.debugger(self.screenshotPath+target)
        while True:
            try:
                x, y = pyautogui.locateCenterOnScreen(self.screenshotPath+target, region = (0,0,2560,1440), confidence=0.8)
                if (x, y) is not None:
                    if needClick is True:
                        pyautogui.click(x,y)
                        self.debugger(f'clicked {x} {y}')
                    return x,y
                else:
                    print('nope')
            except:
                pass
    def tryAndSearch(self,target, withoutClick=True, withoutMove=True, confidence=0.85):
        self.debugger(f"try searching: {self.screenshotPath+target}")
        try:
            x, y = pyautogui.locateCenterOnScreen(self.screenshotPath+target, region = (0,0,2560,1440), confidence=confidence)
            if (x, y) is not None:
                if withoutMove is not True:
                    pyautogui.moveTo(x, y)
                if withoutClick is not True:
                    pyautogui.click()
                return x,y
        except:
            return
    def if_game_found(self):
        self.legends_preference()
        start_time = time.time()
        self.send_to_discord("\n⬇️️  ⬇️  ⬇️  ⬇️  queuing  ⬇️  ⬇️  ⬇️  ⬇️")
        while True:
            if self.tryAndSearch('gameFound.png', withoutClick=True, withoutMove=True):
                self.pick_order_count = time.time()
                break
            self.tryAndSearch('ready.png', withoutClick=False, withoutMove=False)
        self.queue_time = time.time() - start_time
        self.send_to_discord(self.d_message['gameFound.png']+f"({self.queue_time})")
        # self.send_to_discord(msg)
        self.select_legends()
        self.if_in_game()
        return
    def send_to_discord(self,msg,channel=0):
        d.send("APEX", msg,channel)
        return
    def debugger(self,msg):
        if self.debugging == 1:
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%H-%M-%S")
            print(f'debug-[{formatted_datetime}]: {msg}')
    def actual_pick(self,legend):
        x,y = self.searchAndClick("\\legends\\available\\"+legend+".png")
        start_time = time.time()
        while True:
            pyautogui.doubleClick(x,y)
            elapsed_time = time.time() - start_time
            if elapsed_time > 3:
                break
        msg = f"selected: {legend}"
        print(msg)
        # self.send_to_discord(msg)
        return
    def select_legends(self):
        self.searchAndClick("selecting_agent.png")
        pick_time = time.time() - self.pick_order_count
        if pick_time <= 8:
            self.pick_order = 1
        elif pick_time <= 15:
            self.pick_order = 2
        elif pick_time <= 26:
            self.pick_order = 3
        else:
            self.pick_order = 4
            self.send_to_discord(f"pick_order = 4, pick_time: {pick_time}")
        print('selecting agents')
        if self.pick_order <= 2:
            if self.tryAndSearch("not_3.png", confidence=0.9):
                msg = 'not a full team'
                self.send_to_discord(msg)
                self.screenshot(msg)
                self.actual_pick(self.solo_agent)
                return
        #preference by class
        if type(self.preferences) is dict:
            if self.class_based is True:
                for pclass,plegend in self.preferences.items():
                    for alegend in self.all_agents[pclass]:
                        if self.tryAndSearch("\\legends\\hard\\"+alegend+".png", withoutClick=True, withoutMove=False, confidence=0.96):
                            pass
                        else:
                            msg = f"{alegend}({pclass}) is 100% picked"
                            print(msg)
                            self.screenshot(msg)
                            break
                    else:
                        """ return to neutral position """
                        pyautogui.move(1200,350)
                        self.actual_pick(plegend)
                        return
            else:
                for pclass,plegend in self.preferences.items():
                    for alegend in self.all_agents[pclass]:
                        if self.tryAndSearch("\\legends\\soft\\"+alegend+".png", withoutClick=True, withoutMove=False, confidence=0.96):
                            pass
                        else:
                            msg = f"{alegend}({pclass}) might be picked"
                            print(msg)
                            self.screenshot(msg)
                            # break
                    else:
                        """ return to neutral position """
                        pyautogui.move(1200,350)
                        self.actual_pick(plegend)
                        if not self.tryAndSearch('agent_picked.png'):
                            self.debugger("pick failed")
                            return
    def screenshot(self,details):
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
        pyautogui.screenshot(self.screenshotPath+formatted_datetime+f"_{details}.png")
    def testing(self):
        AllFiles = os.listdir(self.screenshotPath+'//legends//picked')
        for i in AllFiles:
            print(i)
    def if_in_game(self): 
        self.searchAndClick('in_apex_game.png',needClick=False)
        # self.send_to_discord(self.d_message['in_apex_game.png'])
        self.jumpmaster = False
        if self.pick_order == 3:
            self.jumpmaster_reminder('default')
            self.jumpmaster = True
        dropship = False
        while True:
            if dropship is False:
                try:
                    x = pyautogui.locateCenterOnScreen(self.screenshotPath+'in_dropship.png', region = (0,0,2560,1440), confidence=0.8)
                    if x is not None:
                        dropship = True
                        if self.jumpmaster is False:
                            self.send_to_discord(self.d_message['in_dropship.png'])
                except:
                    pass
            else:
                try:
                    x = pyautogui.locateCenterOnScreen(self.screenshotPath+'in_dropship.png', region = (0,0,2560,1440), confidence=0.8)
                    if x is None:
                        self.send_to_discord(self.d_message['in_dropshipp.png'])
                        break
                except:
                    pass
            if self.jumpmaster is False:
                try:
                    x = pyautogui.locateCenterOnScreen(self.screenshotPath+'you_are_jumpmaster.png', region = (0,0,2560,1440), confidence=0.8)
                    if x is not None:
                        if dropship is False:
                            self.send_to_discord(self.d_message['in_dropship.png'])
                            self.jumpmaster_reminder('assigned')
                        self.jumpmaster = True
                except:
                    pass
        print('GLHF')
        return
    def jumpmaster_reminder(self,scenerio):
        if scenerio == "default":
            msg = 'you_are_jumpmaster.png'
        elif scenerio == "assigned":
            msg = 'assigned'
        self.send_to_discord(self.d_message[msg])
        time.sleep(1.5)
        self.send_to_discord(self.d_message[msg])
        time.sleep(1)
        self.send_to_discord(self.d_message[msg])
        time.sleep(1)
    @staticmethod
    def format_time(elapsed_time):
        m, s = divmod(int(elapsed_time), 60)
        time_format = "{:02d}:{:02d}".format(m, s)
        return time_format
    def respawning_check(self):
        try:
            x, y = pyautogui.locateCenterOnScreen(self.screenshotPath+'respawning.png', region = (0,150,2500,1000), confidence=0.9)
            if (x, y) is not None:
                try:
                    x, y = pyautogui.locateCenterOnScreen(self.screenshotPath+'respawningg.png', region = (0,0,2560,1440), confidence=0.9)
                    if (x, y) is not None:
                        self.send_to_discord(self.d_message['respawning.png'])
                        pass
                except:
                    return
                pass
        except:
            return
        time.sleep(20)
    def error_checking(self):
        return
    def checkScenerio(self):
        self.send_to_discord("initiated...")
        game_end = False
        self.error_checking(self)
        while True:
            if self.tryAndSearch('ready.png') or self.tryAndSearch('gameFound.png'):
                self.if_game_found()
                game_end is False
            elif self.tryAndSearch('squad_eliminated.png') and game_end is False:
                self.send_to_discord(self.d_message['squad_eliminated.png'])
                game_end = True
            self.respawning_check()
    def legends_preference(self):
        """ config """
        self.all_agents = {
            "skirmisher": ["horizon", "pathfinder","wraith"],
            "assault": ["bangalore", "fuse", "ash", "maggie"],
            "recon": ["bloodhound", "seer","vantage"],
            "support": ["gibraltar", "lifeline","loba"],
            "controller": ["rampart"]
        }
        """ config """
        """ preferences """
        self.preferences = dict()
        self.class_based = False
        self.preferences["skirmisher"] = "horizon"
        self.preferences["assault"] = "bangalore"
        self.preferences["recon"] = "vantage"
        self.preferences["support"] = "loba"
        self.preferences["controller"] = "rampart"
        """ preferences """
def main():
    a = apex()
    a.checkScenerio()
if __name__ == '__main__':
    main()