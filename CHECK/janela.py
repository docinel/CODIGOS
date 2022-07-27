import pygetwindow as gw  
import time

time.sleep(3)

win = gw.getWindowsWithTitle('Login...')[0].restore()


#win.activate()