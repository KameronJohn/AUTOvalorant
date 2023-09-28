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
currentPath = os.path.dirname(os.path.abspath(__file__))
dc_path = currentPath +r'\..\..\kmjAUTO\core'
sys.path.insert(0, dc_path)
import discord_send_msg as d
currentPath = os.path.dirname(os.path.abspath(__file__))
currentPath += '\\'
screenshotPath = currentPath+'source\\'
print('debugging')
while True:
    for i in range(1,5):
        try:
            filename = screenshotPath+'debug'+str(i)+'.png'
            print(filename)
            x, y = pyautogui.locateCenterOnScreen(filename, region = (0,0,2500,1440), confidence=0.7)
            if (x, y) is not None:
                pyautogui.moveTo(x, y)
                pyautogui.click()
                break
        except:
            pass
