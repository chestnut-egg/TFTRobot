import random
import win32api,win32gui
import sys
import time
import win32con
from PIL import ImageGrab

def click(left,top):
    win32api.SetCursorPos([left,top])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
