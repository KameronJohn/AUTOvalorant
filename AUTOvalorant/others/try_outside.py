from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con, win32gui
import webbrowser
import os
import pyperclip
# from openpyxl import Workbook, load_workbook
from datetime import date
# from openpyxl.utils import get_column_letter
import pandas as pd
import numpy as np
import sys
import pygetwindow
import datetime
from PIL import Image
# from pytesseract import pytesseract
import os
def getMousePosition():
    PosList = []
    while True:
        a = pyautogui.position()
        print(a)
        if keyboard.is_pressed('1'):
            x,y = a
            PosList.append((x,y))
            # PosList.append(a)112
            print(PosList)
            time.sleep(0.3)
        if keyboard.is_pressed('2'):
            print(PosList)
            return
getMousePosition()
def afk():
    while True:
        try:
            if keyboard.is_pressed('1'):
                print('pressed')
                while True:
                    pyautogui.press('6')
                    pyautogui.keyDown('w')
                    time.sleep(2)
                    pyautogui.keyUp('w')
                    # pyautogui.press('b')
                    # pyautogui.click()
                    # pyautogui.press('b')
                    # pyautogui.press('1')
                    # pyautogui.press('g')
                    # pyautogui.press('2')
                    # pyautogui.press('g')
                    # pyautogui.press('3')
                    # pyautogui.press('g')
                    # pyautogui.press('4')
                    # pyautogui.press('g')
                    # time.sleep(5)
                    for i in range(50):
                        pyautogui.press('s')
                    time.sleep(5)
                    pyautogui.press('s')
                    pyautogui.press('s')
                    pyautogui.press('s')
                    pyautogui.press('s')
                    pyautogui.press('s')
                    try:
                        if keyboard.is_pressed('1'):
                            exit()
                    except:
                        pass
        except:
            pass
def ifFoundInSection():
    while True:
        print('trying')
        try:
            x, y = pyautogui.locateCenterOnScreen(r'C:\Users\kamka\Documents\AUTOvalorant\source\availableAgent.png', region = (0,0,2500,1440), confidence=0.85)
            if x is not None:
                pyautogui.moveTo(x, y)
                # click()
                print('foundnoudnuodnuondounudu')
                break
            else:
                print('nope')
        except:
            pass
def screenshot():
    pyautogui.screenshot(r"C:/Users/kamka/Documents/333/log/"'my_screensho.png', region = (715,0,1100,1440))    
def screenshotMultiple():
    for a in np.arange(600, 800, 20).tolist():
        print('his')
        scName = r"C:/Users/kamka/Documents/333/log/" + f'testing_{a}_b.png'
        print(scName)
        pyautogui.screenshot(scName, region = (a,0,1000,1440))
    print('done')
def trying():
    return 't1', 't2'
def fn1():
    a,b = trying()
    print(a)
    print(b)
def fn2():
    os.system('C:')
    type = 'git fetch origin'
    os.system(type)
    type = 'git pull origin main'
    os.system(type)
    type = 'git add .'
    os.system(type)
    today = 'testing'
    os.system(type)
    type = f"git commit -m {today}"
    os.system(type)
    type = 'git push -f origin main'

"""  """
# while True:
#     try:
#         x,y = pyautogui.locateCenterOnScreen('username.png', region = (0,0,2560,1440), confidence=0.8)
#         if x is not None:
#             break
#     except:
#         pass
"""  """
# afk()
# import os
# def startSim():
#     os.startfile("timertesting.bat")
# startSim()
# while True:
#     time.sleep(1) 
# import subprocess
# subprocess.call([r'C:\Users\kamka\Documents\333\timertesting.bat'])
# print('halo')
# ifFoundInSection()
# fn2()
# screenshotMultiple()
# screenshot()


# dir = r'C:\Users\John\Documents\John\333\RealESRGAN\results'
# for f in os.listdir(dir):
#     os.remove(os.path.join(dir, f))

# os.chdir("./RealESRGAN")
# command = r'python C:\Users\John\Documents\John\333\RealESRGAN\inference_realesrgan.py'
# os.system(f'cmd /c "{command}"')
# os.chdir("..")








# os.system("")



# if totalCount > 20 or len(tmpdata)>10:
#     print('jeng')

# text = '@str9tos\n @Mofonger\n give me luck to win this shit'
# if 'win' in text:

#     print('expected')


# line added in main branch 

# win = pygetwindow.getWindowsWithTitle(r'D:\Python\python.exe')[0]
# win = pygetwindow.getWindowsWithTitle(r'Visual Studio Code')[0]
# win.size = (620, 1350)
# win.moveTo(0, 100)
# pyautogui.press('win')
# time.sleep(0.5)
# pyautogui.write('deskpins.exe')
# time.sleep(0.4)
# pyautogui.press('enter')
# time.sleep(0.2)
# pyautogui.moveTo(x=2504, y=1249)
# time.sleep(0.2)
# click()


# pyautogui.moveTo(x=387, y=623)
# click()



# urls = ['Gr1m3_2', 'nol_mal', 'antoniomeee', 'OrzNille', 'A2v2w2is', 'ZonSiv', 'sAv1tArrrr', 'a11an_stro11', 'Ston3_Kameron', 'gr22nhat', 'RoxTobbie', 'Marc211015', 'Mas_sdgm', 'MarcusBrannd', 'sKiel2r', '323_aaron', 'IssacDuhman', 'bonlobsterr31', '5_K2nt', 'Bstro44', 'MessiLonzZ']
# urls = ['Gr1m3_2', 'nol_mal']
# print(urls[-2])
# listSplit = 5
# if listSplit:
#     urlsInSubList = [urls[x:x+listSplit] for x in range(0, len(urls), listSplit)]
#     if len(urlsInSubList[-1])< listSplit/2:
#         for i in urlsInSubList[-1]:
#             urlsInSubList[-2].append(i)
#             urlsInSubList.pop()
#     for i in urlsInSubList:
#         print(i)
# else:
#     pass

# sys.path.append('../')


# pyautogui.moveTo(x=714, y=360)


# x = 0
# def fn1():
#     x = 0
#     while True:
#         x +=1
#         print(x)
#         if x >100:
#             print('bye')
#             return
# fn1()
# x, y = 123,432
# a = x,y
# print(a)

# aclist = {0: '@KameronW_Stone', 1: '@Andrew_Grime574', 2:'@Mick_j0n',
#                 3: '@jacoBstro4', 4: '@S_K32T', 5: '@sambjmf',
#                 6: '@SivZon', 7: '@Greenhattt', 8: '@MillerNileOrz', 7:'ZonSiv',
#                 9: '@antoniochorr', 10: '@ernestTTy', 11: '@Aeveweis',
#                 12: '@harperjames31', 13: '@JesseliamxX', 14: '@Martin07215',
#                 15: '@xav1errr', 16: '@Stephzip', 17: '@RainingTrainn',
#                 18: '@issacbrook19', 19: '@BonoLanda'}

# print(aclist[4])

# aclist = {'Ston3_Kameron': 1, 'Bstro44': 4, 'ZonSiv': 7, '323_aaron': 3}
# print(aclist["Bstro44"])
# a = '01-07-2022'
# print(a[3:5])

# while True:
#     print('trying')
#     try:
#         start = pyautogui.locateCenterOnScreen('dpage_loaded.png', region = (0,0,2560,1440), confidence=0.85)
#         if start is not None:
#             pyautogui.moveTo(start)
#             click()
#             break
#     except:
#         pass

# url_list = "https://twitter.com/homehttps://twitter.com/ethoz/status/1538935169691705344https://twitter.com/KenEmpowered/status/1539307914023903232https://twitter.com/TorontoSRN/status/1539352462603296768https://twitter.com/compete_wtp/status/1539241225299324928https://twitter.com/WeilluminateCC/status/1539123972054425601https://twitter.com/PlayWCF/status/1539650557451051008https://twitter.com/mogulcuh/status/1538801484875575296https://twitter.com/Originnfnt/status/1538743936398741504https://twitter.com/Liquid01hp/status/1539301744173359105https://twitter.com/Cyreptis/status/1538948416138620928https://twitter.com/DoctorMonnix/status/1538966079724298241https://twitter.com/VoltValorant/status/1538734206028636161https://twitter.com/saikoBTW/status/1539234056495370241https://twitter.com/OLIZERA/status/1539245369930010627"
# print(url_lisreplace('https:', '\nhttps:')[1:])
# Python code to demonstrate 
# to find nth occurrence of substring
# Initialising values
# ini_str = "https://twitter.com"
# ini_str = 'https://twitter.com/01xBrian/status/1482666819983130626'
# ini_str = 'https://twitter.com//////////////////////////////////////'
# sub_str = "/"

# newlist = []
# for i in tag_list:   
#     pos = i.find('?utm_medium=copy_link')
#     i = i[:pos:]
#     i.replace('https://instagram.com/', '')
#     print(i)
#     newlisappend(i)
# print(new_list)


# pyautogui.moveTo(2224, 264)

# for a in np.arange(0, 100, 10).tolist():
#     for b in np.arange(500, 700, 20).tolist():
#         im = pyautogui.screenshot('my_screenshopng', region = (a,b,700,150))
# print('done')
# pyautogui.moveTo(x=1041, y=1395)

# while True:
#   try:
#       x, y = pyautogui.locateCenterOnScreen('brave_importbookmarks.png', region = (0,0,2100,1450), grayscale=True, confidence=0.8)
#       if x is not None:
#           print('found')
#           pyautogui.moveTo(x, y)
#       else:
#           print('cant')
#   except:
#       print('nope')
# os.startfile('Brave') b



# os.startfile('msedge')
# hwnd = win32gui.GetForegroundWindow()
# win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

# url = 'google.com'
# chrome = webbrowser.Chrome(r'C:\Program Files\Google\Chrome\Application\chrome.exe')
# edge = webbrowser.edge(r'C:\Program Files\Mozilla Firefox\firefox.exe')

# opera_open()
# pyautogui.hotkey('ctrl', 'n', delay=0.25)
# pyautogui.write("https://www.websiteplanecom/webtools/multiple-url/")
# pyautogui.press('enter')
# opera_path = 'C:\\Users\\kamka\\AppData\\Local\\Programs\\Opera\\opera.exe'
# webbrowser.register('opera', None,webbrowser.BackgroundBrowser(opera_path))
# webbrowser.get("opera").open_new_tab("https://www.bing.com")
# time.sleep(0.1)
# webbrowser.get("opera").open("https://gleam.io/iXErC/aim-lab-custom-pc-giveaway")
# time.sleep(0.1)
# webbrowser.get("opera").open("https://twitter.com/home")
# time.sleep(0.1)
# opera.open_new(url)
# time.sleep(0.5)
# os.startfile('Opera')
# time.sleep(2)
# os.system("TASKKILL /F /IM Opera.exe")
# os.startfile('msedge')
# time.sleep(2)
# os.system("TASKKILL /F /IM msedge.exe")

# os.startfile('chrome')
# time.sleep(2)
# os.system("TASKKILL /F /IM chrome.exe")