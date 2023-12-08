import pyautogui
import time
import pygetwindow as gw

# Disable fail-safe (not recommended)
pyautogui.FAILSAFE = False

# Introduce a delay before taking a screenshot
time.sleep(5)  # You can adjust the delay based on your needs

# Capture the Entire Screen
screenshot = pyautogui.screenshot()
screenshot_path = 'entire_screen.png'
screenshot.save(screenshot_path)

# Search for a Particular Text
search_text = 'AbDuLIAh ZaHiD SMIU 5:12 PM'

# Get all windows
windows = gw.getAllTitles()

# Loop through each window to find the search text
for window_title in windows:
    if search_text in window_title:
        print(f"Text found in window: {window_title}")

        # Get the active window containing the text
        window = gw.getWindowsWithTitle(window_title)[0]

        # Get the position of the top-left corner of the window
        x, y = window.left, window.top
        print(f"Window found at X: {x}, Y: {y}")

        # Move the cursor to the position
        pyautogui.moveTo(x, y, duration=1)  # Adjust duration as needed
        print(f"Cursor moved to X: {x}, Y: {y}")
        break  # Exit the loop if the text is found in any window
else:
    print("Text not found in any window.")
