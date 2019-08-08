"Chrono Trigger, Prehistoric Trade Handler" # Script assumes player is standing in front of trader with no other menu / dialogue open. It will attempt to bring chrono trigger to the foreground to begin trading.
import pyautogui
import win32gui
from modules.tradehandler import *
from modules.inputparameters import quantity_inp
from time import sleep
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0

def windowEnumerationHandler(hwnd, top_windows):
  top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

start_str = pyautogui.confirm('Begin trading?', title="Trader", buttons=['Yes','No'])
if start_str is 'Yes':
    pass
else:
    print("Closing trader..."); exit()
item_var = pyautogui.confirm('Which item to trade for?', title="Trade List", buttons=['Ruby Gun',"Shaman's Bow",'Stone Arm','Mammoth Tusk','Ruby Vest','Stone Helm'])
if item_var == None:
    print("Error: item_var is None. Closing trader..."); exit()
item_var = item_var.replace(" ", "_").lower() # Take item_str and turn it into something we can call later
item_var = item_var.replace("'","")
quantity_int = quantity_inp('33',"Trade Quantity") # Take user input, prompt again if answer has invalid chars or is higher than ('thisamount',"in a pyautogui.prompt with this title")
if __name__ == "__main__": # brings window named "chrono trigger" to the front. could potentially misfire if other windows containing the name are open
  results = []
  top_windows = []
  win32gui.EnumWindows(windowEnumerationHandler, top_windows)
  for i in top_windows:
    if "chrono trigger" in i[1].lower():
      print (i)
      win32gui.ShowWindow(i[0],5)
      win32gui.SetForegroundWindow(i[0])
      break
trade_handler(item_var,quantity_int) # Simulate keypresses to navigate pre-history trade menu, assumes you are standing in front of trader with no dialogue or menu open
                                     #trade_handler sleep timings can be improved
print(start_str,item_var,quantity_int,sep='\n')