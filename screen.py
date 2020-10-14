import pyautogui

import tkinter as tk
from tkinter.filedialog import *

root = tk.Tk()

cv1 = tk.Canvas(root, width=300,height=
300)
cv1.pack()

def takeScreenshot():
    myScreenshot = pyautogui.screenshot()
    save_path = asksaveasfilename()
    myScreenshot.save(save_path+"_screenshot.png")

myButton= tk.Button(text="Capture cet écran",command = takeScreenshot,font=10)
cv1.create_window(150,150,window=myButton)

root.mainloop()