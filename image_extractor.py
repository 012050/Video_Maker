import pyautogui
import time
import os

img = []
time.sleep(5)

for i in range(1, 120):
    path = os.getcwd() + f"\Images\{i}.png"
    pyautogui.screenshot(path)
    print(i)
    time.sleep(1)