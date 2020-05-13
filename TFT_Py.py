import random
import win32api,win32gui
import sys
import time
import win32con
from PIL import ImageGrab
from win import *


hwnd = win32gui.FindWindow(None, "Foxmail 属性")

left = 0
top = 0
right = 0
bottom = 0

if hwnd:
    print("找到窗口")
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    #win32gui.SetForegroundWindow(hwnd)
    print("窗口坐标：")
    print(str(left)+' '+str(right)+' '+str(top)+' '+str(bottom))
else:
    print("未找到窗口")


#left += 100
#top += 344
#click(left,top)

left += 250
top += 317
click(left,top)
keybd(0x57)