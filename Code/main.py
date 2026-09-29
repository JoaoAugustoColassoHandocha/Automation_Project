'''
Automation Logic:

1 - Access the company system
2 - Log in
3 - Open the database
4 - Register a product
5 - Repeat step 4 until the product list is finished


Link used in the project: https://dlp.hashtagtreinamentos.com/python/intensivao/login

'''

import pyautogui, os, time

# Pause time between each execution
pyautogui.PAUSE = 1

press = pyautogui.press
write = pyautogui.write
click = pyautogui.click
sleep = time.sleep

# Browser request and link
os.system('cls' if os.name == 'nt' else 'clear')
browser = input('\nNavegador: ')
os.system('cls' if os.name == 'nt' else 'clear')
link = input('\nLink: ')
os.system('cls' if os.name == 'nt' else 'clear')

# Access the company system
press('win')
write(browser)
press('enter')
write(link)
press('enter')
sleep(5)

# Log in
click(x=717, y=371)
write('pythonimpressinador@gmail.com') # Login
press('tab')
write('teste') # Password
press('tab')
press('enter')
sleep(5)

# Open the database