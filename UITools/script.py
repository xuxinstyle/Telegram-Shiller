# coding=utf-8
# Program to send bulk customized messages through Telegram Desktop application
# Author @inforkgodara

import pyautogui

import pyperclip
import pandas
import time
import tkinter
import tkinter.messagebox
import os
from Message import fetch_text, group0, group1, group2, group3,  fetch_text1, fetch_text2
pyautogui.FAILSAFE = False
api_hash = '7d820d4557af57f57ae3c5d40524ce80'
api_id = '11770907'

# pip install pyinstaller
# pyinstaller -F -c -i python.ico script.py  生成exe 的命令






def group_send(path="", message=""):

      print("open telegram ....")
      dirt = "D:\Telegram Desktop\Telegram.exe"
      if path!="":
            dirt=path

      print (dirt)
      time.sleep(2)
      os.startfile(dirt)
      print("open telegram start!")
      count = 0
      for column in group0():
            pyautogui.press('esc')
            pyautogui.press('esc')
            pyautogui.press('esc')
            pyautogui.hotkey('ctrl', 'f')
            time.sleep(1)
            pyautogui.write(str(group0()[count]));

            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('down')

            pyautogui.press('enter')

            msg = fetch_text1()
            if message != "":
                  msg = message
            time.sleep(2)

            pyperclip.copy(msg)
            pyautogui.hotkey('ctrl', 'v')
            # pyautogui.write("nanshanxili  400mi  70fenzhong huanbao  guanshifuwu ");
            pyautogui.press('enter')
            pyautogui.press('esc')
            print("send message :" + msg + " to " + str(group0()[count]) + " success!")
            count = count + 1

      # tkinter.messagebox.showinfo(title='tips', message='send message success!!!')
      print('The script executed successfully. send message '+str(count)+'')


