import pyautogui #https://medium.com/@martin.lees/how-i-made-a-python-bot-to-automate-a-tactical-mmorpg-9f6693350d10
import win32gui
#from PIL import Image, ImageGrab
#from scipy import cluster, ndimage #ndimage maybe takes array of values and can create an algorithm differentially
import time
import imagesearch #https://github.com/drov0/python-imagesearch
import cv2
from python_imagesearch.imagesearch import imagesearch
from python_imagesearch.imagesearch import *
#can pyautogui mouse down on one point, and mouse up from a completely different point

hwndtop = pyautogui.getWindowsWithTitle('League of Legends')
print(str(hwndtop[-9:-2]))


'''
while True:
    win32gui.BringWindowToTop(hwndtop)
    foundHP = imagesearch('/Python/projects/league/hpmini.png', precision=.8)

    if foundHP != -1:
        posHP = pyautogui.locateOnScreen(image='/Python/projects/league/hpmini.png')
        pyautogui.screenshot(imageFilename='/Python/projects/league/imgCB.png', region=(posHP[0], posHP[1], posHP[0] - 1075, posHP[1])).show()#posHP[0], posHP[1], posHP[0] - 500, posHP[1]
        pyautogui.moveTo(x='/Python/projects/league/imgCB.png', duration=0)
        pyautogui.tripleClick(interval=0.2, button='SECONDARY')
    else:
        print('No target')

def start(): #win32gui.GetFocus() == pyautogui.getWindowsWithTitle('League of Legends (TM) Client')
    while True:
        if True:
            return
        else:
            return
'''
        
#start()