import math, operator
from functools import reduce
from time import sleep
import pywinauto.keyboard as keyboard

import win32gui
from PIL import ImageOps
from PIL import ImageGrab


def window_enum_handler(hwnd, resultList):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
        resultList.append((hwnd, win32gui.GetWindowText(hwnd)))


def get_app_list(handles=[]):
    mlst = []
    win32gui.EnumWindows(window_enum_handler, handles)
    for handle in handles:
        if "Shakes & Fidget" in handle[1]:
            mlst.append(handle)
    return mlst


def compare(i1, i2):
    h1 = i1.histogram()
    h2 = i2.histogram()
    rms = math.sqrt(reduce(operator.add,
                           map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))
    return rms


def main():
    appwindows = get_app_list()
    shakes = appwindows[0][0]
    win32gui.SetForegroundWindow(shakes)
    rect = win32gui.GetWindowRect(shakes)
    leftcrop = rect[3] // 2
    Found = False
    anzahl = 0
    while not Found:
        sleep(1)
        image1 = ImageGrab.grab(bbox=(rect[0], rect[1], rect[2], rect[3]))
        sleep(1)
        image2 = ImageGrab.grab(bbox=(rect[0], rect[1], rect[2], rect[3]))

        cimage1 = ImageOps.crop(image1, (leftcrop, 0, 0, 0))
        cimage2 = ImageOps.crop(image2, (leftcrop, 0, 0, 0))
        print("The difference is: " + str(compare(cimage1, cimage2)))

        if compare(cimage1, cimage2) > 25.0:
            Found = True
        else:
            anzahl += 1
            keyboard.send_keys("{UP}")
    print("An Item was found after " + str(anzahl+1) + " Characters.")
    print()
    input("Press Enter to end the Program!")

if __name__ == "__main__":
    main()
