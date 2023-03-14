import pyautogui
import time
import os

zero = "00"
count = 0

for a in range(1, 6):
    print(a)
    time.sleep(1)

print("\nCapture start..")
for i in range(1, 641):
    if i >= 10 and count == 0:
        zero = zero.replace("00", "0")
        count = 1
    elif i >= 100 and count == 1:
        zero = zero.lstrip("0")
        count = 2
    path = os.getcwd() + f"\Images\{zero}{i}.png"
    pyautogui.screenshot(path)
    print(i)
    # time.sleep(1.5)