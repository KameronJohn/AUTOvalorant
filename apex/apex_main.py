import pandas as pd
import pyautogui
import keyboard
import os
import sys
# import csv
from datetime import datetime
import time
from extraCode import chop_image
currentPath = os.path.dirname(os.path.abspath(__file__))
dc_path = currentPath +r'\..\..\kmjAUTO\core'
sys.path.insert(0, dc_path)
import discord_send_msg as d
class apex:
    def __init__(self):
        self.netural_pos = 1200,350
        self.currentPath = os.path.dirname(os.path.abspath(__file__))
        self.currentPath += '\\'
        self.screenshotPath = self.currentPath+'apex_source\\'
        self.others_path = self.currentPath+'others\\'
        self.accounts_info_path = self.currentPath+'accounts_info\\'
        self.debugging = 1 # self.debugger()
        self.solo_agent = 'vantage'
        self.last_pos = (1,1)
        self.line_and_class = [{948:[{"assult":[626,730,840,944,1060]},
                                  {"skirmisher":[1283,1390,1478,1598,1710,1829]}]},
                            {1134:[{"recon":[409,525,630,736]},
                                   {"support":[972,1061,1173,1282,1395,1507]},
                                   {"controller":[1735,1846,1961,2056]}]}]
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
    def get_legends_position(self):
        self.df = pd.read_excel(self.currentPath+'\\apex_legends.xlsx')
        """ description: filter the df to the preferred legends only """
        # if type(self.preferences) is dict:
        #     # dictionary value to list
        #     data_as_list = values_list = list(self.preferences.values())
        #     self.debugger("data_as_list:")
        #     self.debugger(data_as_list)
        #     self.df = self.df[self.df['legends'].isin(data_as_list)]
        # elif type(self.preferences) is list:
        #     self.df = self.df[self.df['legends'].isin(self.preferences)]
        # self.debugger("filtered")
        # self.debugger(self.df)
        return
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
            return False
    def if_game_found(self):
        self.legends_preference()
        start_time = time.time()
        self.send_to_discord("\n⬇️️  ⬇️  ⬇️  ⬇️  queuing  ⬇️  ⬇️  ⬇️  ⬇️")
        while True:
            if self.tryAndSearch('gameFound.png', withoutClick=True, withoutMove=True) is not False:
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
    def actual_pick(self,df_row):
        start_time = time.time() 
        x = df_row['xindex']
        # to click towards the box's center
        y = int(df_row['yindex']) + 50
        while True:
            pyautogui.FAILSAFE = False
            pyautogui.move(self.netural_pos)
            for i in range(6):
                pyautogui.mouseDown(x,y)
                time.sleep(0.1)
                pyautogui.mouseUp(x,y)
            elapsed_time = time.time() - start_time
            if elapsed_time > 2:
                break
        msg = f"selected: {df_row['legends']}"
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
            self.send_to_discord(f"error: pick_order = 4, pick_time recorded: {pick_time}")
        print(f"pick order: {self.pick_order}")
        print('selecting agents...')
        if self.pick_order <= 2:
            if self.tryAndSearch("not_3.png", confidence=0.9) is not False:
                msg = 'not a full team'
                self.send_to_discord(msg)
                self.screenshot(msg)
                self.actual_pick(self.df[self.solo_agent])
                return
        #preference by class
        if type(self.preferences) is dict:
            if self.force_pick is False:
                self.check_what_picked()
                self.debugger(f"self.preferences: {self.preferences}")
                for pclass,plegend in self.preferences.items():
                    """ return to neutral position """
                    pyautogui.FAILSAFE = False
                    pyautogui.move(self.netural_pos)
                    self.actual_pick(self.df[plegend])
                    if self.tryAndSearch('agent_picked.png') is not False:
                        return
                    else:
                        print(f"agent_picked.png not found when picking {plegend}")
                else:
                    ValueError("gg lor")
            elif self.force_pick is True:
                self.debugger(f"self.force_pick is {self.force_pick}")
                for pclass,plegend in self.preferences.items():
                    if self.simple_pick(plegend) is True:
                        return
                else:
                    self.screenshot("nothing can be selected wor")
                    InterruptedError("GG")
        elif type(self.preferences) is list:
            for plegend in self.preferences:
               if self.simple_pick(plegend) is True:
                    return
            else:
                self.screenshot("nothing can be selected")
                InterruptedError("GG")
    def simple_pick(self,plegend,screenshot_needed=False):
        """ return to neutral position """
        pyautogui.FAILSAFE = False
        pyautogui.move(self.netural_pos)
        self.actual_pick(self.df[plegend])
        if self.tryAndSearch('agent_picked.png') is not False:
            return True
        else:
            msg = f"{plegend} is picked"
            print(msg)
            return False
    def screenshot(self,details):
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
        pyautogui.screenshot(self.screenshotPath+formatted_datetime+f"_{details}.png")
    def check_what_picked(self):
        yellow = (245,165,35)
        green = (125,175,10)
        blue = (10,180,180)
        picked_index = set()
        for i, row in self.df.iterrows():
            x = row['xindex']
            y = row['yindex']
            if pyautogui.pixelMatchesColor(x, y, yellow, tolerance=0) or pyautogui.pixelMatchesColor(x, y, green, tolerance=0) or pyautogui.pixelMatchesColor(x, y, blue, tolerance=0):
                picked_index.add(i)
                del self.preferences[row['class']]
                print("picked: "+row['class']+" - "+row['legends'])
        return picked_index
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
    def open_apex_packs(self):
        print('HI')
        while True:
            if self.searchAndClick(target="apex_packs.png", needClick=False):
                time.sleep(3)
                self.screenshot("apex_packs")
            while True:
                if self.tryAndSearch("apex_packs.png", withoutClick=False, withoutMove=False) is not False:
                    break
    def error_checking(self):
        return
    def checkScenerio(self):
        self.send_to_discord("initiated...")
        game_end = False
        self.error_checking()
        self.get_legends_position()
        while True:
            if self.tryAndSearch('ready.png') is not False or self.tryAndSearch('gameFound.png') is not False:
                self.if_game_found()
                game_end is False
            elif self.tryAndSearch('squad_eliminated.png') is not False and game_end is False:
                self.send_to_discord(self.d_message['squad_eliminated.png'])
                game_end = True
            self.respawning_check()
    def legends_preference(self):
        """ config """
        self.all_agents = {
            "skirmisher": ["horizon", "pathfinder","wraith"],
            "assault": ["bangalore", "fuse", "ash", "maggie"],
            "recon": ["bloodhound", "seer","vantage"],
            "support": ["gibraltar", "lifeline","loba",""],
            "controller": ["rampart", "caustic", "catalyst"]
        }
        """ config """
        """ preferences """
        self.preferences = dict()
        self.force_pick = True
        self.preferences["skirmisher"] = "pathfinder"
        self.preferences["recon"] = "vantage"
        self.preferences["support"] = "loba"
        self.preferences["controller"] = "rampart"
        self.preferences["assault"] = "bangalore"
        """  """
        self.preferences = ["vantage","caustic", "rampart","seer"]
        """ preferences """
def main():
    a = apex()
    a.legends_preference()
    a.get_legends_position()
    a.check_what_picked()
    """  """
    # a.open_apex_packs()
    a.checkScenerio()
if __name__ == '__main__' :
    main()
    # chop_image.main()