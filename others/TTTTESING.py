import cv2
from pytesseract import pytesseract
import numpy as np
import pyautogui
import os

def locate_text(image_path, text):
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
        pytesseract.tesseract_cmd = r"C:\Users\kamka\Documents\AUTOvalorant\Tesseract\tesseract.exe"
        # Apply OCR to the ROI to get the text
        detected_text = pytesseract.image_to_string(roi)
        # Convert all elements to lowercase and remove spaces
        detected_text = [element.lower().replace(" ", "") for element in detected_text]
        # Check if the text matches what we're looking for
        my_string = ''.join(detected_text)
        # print(my_string)
        # Split the string into a list of words based on empty elements
        my_words = my_string.split('\n')

        print(my_words)
        # Remove empty elements from the list
        my_words = [word for word in my_words if word != '']
        if text in my_words:
            # Return the x,y coordinates of the center of the bounding box
            return x + w//2, y + h//2

    # If the text is not found, return None
    return None
screenshot = pyautogui.screenshot(r"C:\Users\kamka\Documents\AUTOvalorant\removeMe.png")
pos = locate_text(r"C:\Users\kamka\Documents\AUTOvalorant\removeMe.png", "chatgpt")
print(pos)
pyautogui.click(pos)
