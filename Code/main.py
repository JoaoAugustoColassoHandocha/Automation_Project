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

pyautogui.PAUSE = 1

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


# Log in