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

# Browser request and link
os.system('cls' if os.name == 'nt' else 'clear')
browser = input('\nNavegador: ')
os.system('cls' if os.name == 'nt' else 'clear')
link = input('\nLink: ')
os.system('cls' if os.name == 'nt' else 'clear')

# Access the company system
press('win')
pyautogui.write(browser)
press('enter')
pyautogui.write(link)
press('enter')
time.sleep(5)

# Log in
pyautogui.click(x=717, y=371)
pyautogui.write('pythonimpressinador@gmail.com')
press('tab')
pyautogui.write('teste')
press('tab')
press('enter')