import cv2
from pytesseract import pytesseract
import numpy as np
import pyautogui
import os
import re
from PIL import Image
currentPath = os.path.dirname(os.path.abspath(__file__))
currentPath += "\\"
def locate_text(image_path, text):
    # Load the image
    img = Image.open(image_path)
    pytesseract.tesseract_cmd = currentPath + "\\Tesseract\\tesseract.exe"
    # Extract text from the image
    pytesseract_text = pytesseract.image_to_string(img)

    pytesseract_text = pytesseract_text.lower().replace(" ", "")

    # Find the position of a given phrase in the text
    phrase = text
    pos = pytesseract_text.find(phrase)

    if pos != -1:
        # Get the x,y position of the phrase in the image
        x, y = img.size
        x = x * pos / len(pytesseract_text)
        y = y / 2  # Set y to halfway down the image
        print(f"The position of '{phrase}' in the image is ({x}, {y})")
        return x,y
    else:
        print(f"'{phrase}' not found in the image")
    return None


    # Load the image and convert it to grayscale
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to remove noise
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Find contours in the thresholded image
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Loop over the contours and check if the text is present
    for contour in contours:
        # Get the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)
        # Extract the region of interest (ROI) of the contour
        roi = image[y:y+h, x:x+w]

        pytesseract.tesseract_cmd = currentPath + "\\Tesseract\\tesseract.exe"
        # Apply OCR to the ROI to get the text
        detected_text = pytesseract.image_to_string(roi)
        print(type(detected_text))
        # Convert all elements to lowercase and remove spaces
        detected_text = detected_text.lower().replace(" ", "")
        # detected_text = [element.lower().replace(" ", "") for element in detected_text]
        # Check if the text matches what we're looking for
        # my_string = ''.join(detected_text)
        # print(my_string)
        # Split the string into a list of words based on empty elements
        # my_words = my_string.split('\n')

        # print(detected_text)
        print("detected_text:\n"+detected_text)
        # Remove empty elements from the list
        # my_words = [word for word in my_words if word != '']
        pattern = r"\bcypher\b"
        match = re.search(pattern, detected_text)
        if match:
            # Return the x,y coordinates of the center of the bounding box
            return x + w//2, y + h//2

    # If the text is not found, return None
    return None
# screenshot = pyautogui.screenshot(currentPath + "removeMe.png")
# pos = locate_text(currentPath + "removeMe.png", "chatgpt")
pos = locate_text(r"C:\Users\kamka\Documents\AUTOvalorant\source\testing12.png", "store")
print(pos)
pyautogui.moveTo(pos)
