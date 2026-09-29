'''
Helper code for capturing the mouse position.

'''

import time, pyautogui, os

os.system('cls' if os.name == 'nt' else 'clear')

time.sleep(5)
print(f'\n{pyautogui.position()}\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')