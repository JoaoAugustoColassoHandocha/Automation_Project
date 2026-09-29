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

# Browser request and link
os.system('cls' if os.name == 'nt' else 'clear')
browser = input('\nNavegador: ')
os.system('cls' if os.name == 'nt' else 'clear')
link = input('\nLink: ')
os.system('cls' if os.name == 'nt' else 'clear')

# Access the company system
pyautogui.press('win')
pyautogui.write(browser)
pyautogui.press('enter')
pyautogui.write(link)
pyautogui.press('enter')
time.sleep(5)

# Log in
pyautogui.click(x=717, y=371)
pyautogui.write('pythonimpressinador@gmail.com')
pyautogui.click(x=723, y=462)
pyautogui.write('teste')
pyautogui.click(x=962, y=524)