import win32api, win32con
import random
import time
import os

flag = True
drop_chance = ["ok", "nigga u tried", "nigga u tried", "nigga u tried", "nigga u tried", "nigga u tried", "nigga u tried", "nigga u tried", "nigga u triied", "boris has big penis yes"]

os.system("cls")
from os import system
system("title "+ "JoeyClicker")


min_cps = input("[ Minimum CPS ]>> ")
max_cps = input("[ Maximum CPS ]>> ")

while 1:
    if win32api.GetAsyncKeyState(0x01) < 0 and flag == True:
        current_delay = random.uniform(1000 / float(min_cps), 1000 / float(max_cps))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)

        drop_yes = random.choice(drop_chance)

        if drop_yes == "ok":
            current_delay = random.uniform(1000 / random.randint(1, 10), 100 / random.randint(5, 15))
            print(f"cps dropped {current_delay / 1000}")

        print("clicked")
        time.sleep(current_delay / 1000)
        print("randomized " + str(current_delay / 1000))