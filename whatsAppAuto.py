import pyautogui
from time import sleep


# pyautogui.click(466,1050)
# print('clicked')
pyautogui.press('winright')


sleep(2)


pyautogui.write('Whatsapp Beta')


sleep(2)


pyautogui.press('enter')


# Wait for WhatsApp to be launched (you may adjust the delay as needed)
sleep(3)



# Type the name of the contact you want to search for and press Enter
contact_name = "ALi Smiu"
pyautogui.typewrite(contact_name)
pyautogui.press("enter")

sleep(2)

# Click on the search result to open the chat with the contact
pyautogui.moveTo(x=220, y=200)
pyautogui.click()

# Wait for a moment to see the search results (you may adjust the delay as needed)
sleep(0.1)

# # Send messages quickly
for i in range(101):
    message = "Your mobile is hacked 🧑‍💻"
    pyautogui.write(message)
    pyautogui.press("enter")
    sleep(0.1)  # Add a small delay between messages
