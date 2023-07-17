import os
import pyautogui

folder_path = r'C:\Users\User\Documents\GitHub\AUTOvalorant\source'
def tryAndSearch(target):
    print('.', end='')
    try:
        x, y = pyautogui.locateCenterOnScreen(target, region = (0,0,2500,1440), confidence=0.85)
        if (x, y) is not None:
            print('\n')
            print(target)
    except:
        return
while True:
    for filename in os.listdir(folder_path):
        tryAndSearch(folder_path+'\\'+filename)
