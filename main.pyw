import pyautogui
import cv2
import numpy as np
import time
import os
import sys
time.sleep(10)
dir_path = "c:\\zoui"
dir_path2 = "c:\\zoui\\video"
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
    f = open("c:\\zoui\\s.txt","w")
    f.write("1")
    f.close()
else :
    if os.path.exists("c:\\zoui\\s.txt"):
        f = open("c:\\zoui\\s.txt","r")
        sos = f.read()
        f.close()
        if sos == "1" :
            pass
        else :
            sys.exit()
    else :
        f = open("c:\\zoui\\s.txt","w")
        f.write("1")
        f.close()
if not os.path.exists(dir_path2):
    os.makedirs(dir_path2)
screen_size = pyautogui.size()
filename = "c:\\zoui\\video\\" + str(time.localtime(time.time())) + ".avi"
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(filename, fourcc, 20.0, screen_size)
while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    f = open("c:\\zoui\\s.txt","r")
    sos = f.read()
    f.close()
    if sos == "1" :
        pass
    else :
        break
out.release()
cv2.destroyAllWindows()
