import os
import glob
import pyautogui

currentPath = os.path.dirname(os.path.abspath(__file__))
# Use glob to find all PNG files in the directory
png_files = glob.glob(os.path.join(currentPath, '*.png'))
left_png = []
while True:
    # Loop through each PNG file
    for number,file_path in enumerate(png_files):
        try:
            x, y = pyautogui.locateCenterOnScreen(file_path, region = (0,0,2500,1440), confidence=0.8)
            if (x, y) is not None:
                print('\n')
                print("================================================================")
                print(file_path)
                print("================================================================")
        except:
            print(number,end="")
            left_png.append(file_path)
    png_files = left_png
    print(png_files)