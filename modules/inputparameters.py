import re
import pyautogui

def quantity_inp(max_val,title): 
  while True:
    try:
      x = pyautogui.prompt('How many times? (Max: '+ max_val +')',title=title)
    except ValueError:
      print("Error: ValueError qinp",x)
    if x == None or x == '':
      print ("Error: quantity_inp is",x)
      exit()
    elif not re.match('[0-9]*$',x): # Characters entered must be numbers 0 through 9
      pyautogui.alert("Invalid character: "+x,"Error")
      continue
    elif int(x) > int(max_val): # If amount entered is higher than max_val, prompt again.
      pyautogui.alert("Value must be lower than: "+max_val,"Error")
      continue
    return int(x)
    break