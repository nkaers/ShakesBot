import math
import operator
from functools import reduce
from time import sleep

import pywinauto.keyboard as keyboard
import win32gui
from PIL import ImageGrab
from PIL import ImageOps


def window_enum_handler(hwnd, resultList):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
        resultList.append((hwnd, win32gui.GetWindowText(hwnd)))


# this function searches for the Game Application and returns it window_handle
def get_app_list(handles=[]):
    mlst = []
    win32gui.EnumWindows(window_enum_handler, handles)
    for handle in handles:
        if "Shakes & Fidget" in handle[1]:
            mlst.append(handle)
    return mlst


# this function compares two given Images and returns the difference as an Integer
def compare(i1, i2):
    h1 = i1.histogram()
    h2 = i2.histogram()
    rms = math.sqrt(reduce(operator.add,
                           map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))
    return rms


# the main function which does all the work
def main():

    # search for the Game Window and store it in the shakes variable
    appwindows = get_app_list()
    shakes = appwindows[0][0]

    # set the Game Window as the active window
    win32gui.SetForegroundWindow(shakes)

    # store the coordinates which we use later to find and crop the images
    rect = win32gui.GetWindowRect(shakes)
    leftcrop = rect[3] // 2

    # initialize Found and anzahl
    Found = False
    anzahl = 0

    # the loop which continues until a new Item is found
    while not Found:

        # take the two screenshots of the Game window
        sleep(1)
        image1 = ImageGrab.grab(bbox=(rect[0], rect[1], rect[2], rect[3]))
        sleep(1)
        image2 = ImageGrab.grab(bbox=(rect[0], rect[1], rect[2], rect[3]))

        # crop the Images to immediately delete unnecessary information
        cimage1 = ImageOps.crop(image1, (leftcrop, 0, 0, 0))
        cimage2 = ImageOps.crop(image2, (leftcrop, 0, 0, 0))

        # compute the difference and print it to the console
        print("The difference is: " + str(compare(cimage1, cimage2)))

        # if the Images are different enough the loop will break since the Bot expects to have found an unknown item
        # if the Images are the same the bot will increment its counter and go up to the next player
        if compare(cimage1, cimage2) > 25.0:
            Found = True
        else:
            anzahl += 1
            keyboard.send_keys("{UP}")

    # After the Bot has found an item it will output some information and the user can exit the program by hitting Enter
    print("An Item was found after " + str(anzahl+1) + " Characters.")
    print()
    input("Press Enter to end the Program!")

if __name__ == "__main__":
    main()
