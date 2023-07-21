import pyautogui
import keyboard
import os
import sys
import csv
from datetime import datetime
import time
currentPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, currentPath+r'\..\AUTOvalorant')
import selectAgent as s
class apex:
    def __init__(self):
        self.currentPath = os.path.dirname(os.path.abspath(__file__))
        self.currentPath += '\\'
        self.screenshotPath = self.currentPath+'apex_source\\'
        self.others_path = self.currentPath+'others\\'
        self.accounts_info_path = self.currentPath+'accounts_info\\'
        self.debugging = 1
        self.solo_agent = 'seer'
    def searchAndClick(self,target, needClick=True):
        self.debugger(self.screenshotPath+target)
        while True:
            try:
                x, y = pyautogui.locateCenterOnScreen(self.screenshotPath+target, region = (0,0,2500,1440), confidence=0.8)
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
        self.debugger(f"try searching: {target}")
        try:
            x, y = pyautogui.locateCenterOnScreen(self.screenshotPath+target, region = (0,0,2500,1440), confidence=confidence)
            if (x, y) is not None:
                if withoutMove is not True:
                    pyautogui.moveTo(x, y)
                if withoutClick is not True:
                    pyautogui.click()
                return x,y
        except:
            return
    def if_game_found(self):
        print('queuing')
        start_time = time.time()
        while True:
            if self.tryAndSearch('gameFound.png', withoutClick=True, withoutMove=True):
                break
            self.tryAndSearch('ready.png', withoutClick=False, withoutMove=False)
        elapsed_time = time.time() - start_time
        print(f"Queue time: {self.format_time(elapsed_time)}")
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
        print(f"selected: {legend}")
        return
    def select_legends(self):
        self.searchAndClick("selecting_agent.png")
        print('selecting agents')
        if self.tryAndSearch("solo.png"):
            self.actual_pick(self.solo_agent)
            print('solo confirmed')
            return
        #preference by class
        if type(self.preferences) is dict:
            for pclass,plegend in self.preferences.items():
                for alegend in self.all_agents[pclass]:
                    if self.tryAndSearch("\\legends\\available\\"+alegend+".png", withoutClick=True, withoutMove=False, confidence=0.975):
                        pass
                    else:
                        print(f"{alegend}({pclass}) is picked")
                        break
                else:
                    """ return to neutral position """
                    pyautogui.move(1200,350)
                    self.actual_pick(plegend)
                    return
    def testing(self):
        AllFiles = os.listdir(self.screenshotPath+'//legends//picked')
        for i in AllFiles:
            print(i)
    def if_in_game(self):
        self.searchAndClick('in_apex_game.png',needClick=False)
        print('GLHF')
        return
    @staticmethod
    def format_time(elapsed_time):
        m, s = divmod(int(elapsed_time), 60)
        time_format = "{:02d}:{:02d}".format(m, s)
        return time_format
    def legends_preference(self):
        """ config """
        self.all_agents = {
            "skirmisher": ["horizon", "pathfinder","wraith"],
            "assault": ["bangalore", "fuse", "ash", "maggie"],
            "recon": ["bloodhound", "seer"],
            "support": ["gibraltar", "lifeline","loba"],
            "controller": ["rampart"]
        }
        """ config """
        """ preferences """
        self.preferences = dict()
        self.preferences["support"] = "loba"
        self.preferences["skirmisher"] = "pathfinder"
        self.preferences["assault"] = "ash"
        self.preferences["controller"] = "rampart"
        self.preferences["recon"] = "seer"
        """ preferences """
def main():
    a = apex()
    a.legends_preference()
    a.if_game_found()
    a.select_legends()
    a.if_in_game()
if __name__ == '__main__':
    main()