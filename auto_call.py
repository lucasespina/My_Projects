import time
import pyautogui as pg
import os
import win32gui, win32con


validador = "Felipe Frug Insper"


os.system('start C:\\Users\\lucas\\AppData\\Local\\WhatsApp\\whatsapp.exe')

window = win32gui.GetForegroundWindow()
win32gui.ShowWindow(window, win32con.SW_MAXIMIZE)

time.sleep(6)
pg.press("tab")
print("tabou")
time.sleep(0.5)

pg.press("tab")
print("tabou")

pg.press("tab")
print("tabou")
pg.press("tab")
print("tabou")

pg.typewrite(validador)

time.sleep(0.5)

pg.press("tab")
pg.press("tab")

time.sleep(0.5)
pg.press("tab")
pg.press("tab")

time.sleep(0.5)
pg.press("enter")
    



