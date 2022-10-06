from serial.tools import list_ports
import subprocess
import pyautogui
import serial.tools.list_ports
import os 



dir_path = os.path.dirname(os.path.realpath(__file__))
print (dir_path)
path_to_file = dir_path + "/cfg.txt"
 
with open(path_to_file) as file: # после этой строчки не нужно делать две пустых
    data = file.read().splitlines()
    
    





port = data[1]

#-=-=-=-=-=-==-=-==-=-=-=-=-=-=-

COM = serial.Serial(port,115200)



while True:
    rx = COM.readline()
    rxs = str(rx, "utf-8").strip()
    if rxs == "1":
        pyautogui.hotkey(data[0], data[2])
    elif rxs == "2":
        pyautogui.hotkey(data[4], data[6])
    elif rxs == "3":
        pyautogui.hotkey(data[8], data[10])
    elif rxs == "3":
        pyautogui.hotkey(data[12], data[14])
    elif rxs == "3":
        pyautogui.hotkey(data[16], data[18])
    elif rxs == "3":
        pyautogui.hotkey(data[20], data[22])
    elif rxs == "3":
        pyautogui.hotkey(data[24], data[26])
    elif rxs == "3":
        pyautogui.hotkey(data[28], data[30])
    elif rxs == "3":
        pyautogui.hotkey(data[32], data[34])
