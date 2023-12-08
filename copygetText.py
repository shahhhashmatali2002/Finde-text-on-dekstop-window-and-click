from pytesseract import Output
import pytesseract
import cv2
import numpy as np
import pyautogui
import time

def find_and_move_to_text(text_to_find, min_conf=0):
    try:
        # Take a screenshot using PyAutoGUI
        screenshot = pyautogui.screenshot()
        screenshot_np = np.array(screenshot)
        screenshot_rgb = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2RGB)

        # Use image_to_data to get bounding box coordinates, text, and confidence
        results = pytesseract.image_to_data(screenshot_rgb, output_type=Output.DICT)

        # loop over each of the individual text localizations
        for i in range(0, len(results["text"])):
            # extract the bounding box coordinates of the text region from the current result
            x, y, w, h = results["left"][i], results["top"][i], results["width"][i], results["height"][i]

            # extract the OCR text itself along with the confidence of the text localization
            detected_text, conf = results["text"][i], int(results["conf"][i])

            # filter out weak confidence text localizations
            if conf > min_conf and text_to_find in detected_text:
                # display the confidence and text to the terminal
                print(f"Confidence: {conf}")
                print(f"Text: {detected_text}")
                print("")

                # Move the cursor to the center of the bounding box
                center_x = x + w // 2
                center_y = y + h // 2
                pyautogui.moveTo(center_x, center_y)
                pyautogui.click()
                break
            else:
                print('Text not found', results["text"][i])

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage with text_to_find set to "your_search_text"
find_and_move_to_text("Fakhir", min_conf=50)
