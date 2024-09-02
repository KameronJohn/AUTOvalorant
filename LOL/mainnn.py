import sys
import os
currentPath = os.path.dirname(os.path.abspath(__file__))
corepath = currentPath +r'\..\..\kmjAUTO\core'
import sys
print(corepath)
sys.path.insert(0, corepath)
import pyautogui
from kjautogui import kjgui
import discord_send_msg
class lolmain:
    def __init__(self) -> None: 
        self.sourcepath = currentPath +'\\source\\'
        self.kg = kjgui()
    def scenerio(self):
        print(self.sourcepath+"accept.png")
        # self.kg.wait_until_found(target_path = self.sourcepath+"accept.png")
        # print('nice')
        while True:
            a = self.kg.tryAndSearch(target_path = self.sourcepath+"accept.png",Click=True, Move=True)  
            if a is not None:
                print('nice')
                break
        discord_send_msg.send("LOL", "GAME FOUND nigga")
            
if __name__ == "__main__":
    lolmain = lolmain()
    lolmain.scenerio()