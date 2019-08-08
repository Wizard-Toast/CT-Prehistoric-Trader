import pyautogui
from time import sleep
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0

def press(key): #keyDown keyUp required for chrono trigger, function for ease
  pyautogui.keyDown(key); sleep(0.3); pyautogui.keyUp(key); sleep(0.4); print(key)

def trade_handler(item_var,quantity_int):
  confirm = 'space'
  down = 's'
  quantity = 0
  sleep(1)
  press(confirm);press(confirm);press(confirm);press(confirm);press(confirm)
  while quantity < quantity_int:
    if item_var == 'ruby_gun':
      sleep(0.3);press(confirm);sleep(0.2);press(confirm);press(confirm);sleep(0.2)
      press(down);press(confirm);press(confirm);press(confirm)
    elif item_var == 'shamans_bow':
      sleep(0.3);press(confirm);sleep(0.2);press(confirm);press(confirm);sleep(0.2)
      press(down);press(down);press(confirm);sleep(0.2);press(confirm);press(confirm)
    elif item_var == 'stone_arm':
      sleep(0.3);press(confirm);sleep(0.2);press(confirm);press(confirm);sleep(0.2)
      press(down);press(down);press(down);press(confirm);sleep(0.2);press(confirm);press(confirm)
    elif item_var == 'mammoth_tusk':
      sleep(0.3);press(down);press(confirm);sleep(0.2);press(confirm);press(confirm);sleep(0.2)
      press(down);press(down);press(confirm);sleep(0.2);press(confirm);press(confirm)
    elif item_var == 'ruby_vest':
      sleep(0.3);press(down);press(confirm);sleep(0.2);press(confirm);press(confirm);sleep(0.2)
      press(down);press(down);press(down);press(confirm);sleep(0.2);press(confirm);press(confirm)
    elif item_var == 'stone_helm':
      sleep(0.3);press(down);press(down);press(confirm);sleep(0.2);press(confirm);press(confirm);sleep(0.2)
      press(down);press(down);press(down);press(confirm);sleep(0.2);press(confirm);press(confirm)
    quantity += 1
    if quantity < quantity_int:
      sleep(1);press(confirm);sleep(0.3);press(confirm);press(confirm);press(confirm);press(confirm)
      sleep(1)
    if quantity == quantity_int:
      sleep(1);press(confirm);sleep(0.6);press(down);press(confirm) # select 'no' at "still want trade?" to close menu
    print (quantity,":",quantity_int)

"""
0:petal
1:fang:s
2:horn:ss
3:feather:sss
"""
"""
ruby_gun = ['Petal','Fang']
shamans_bow = ['Petal','Horn']
stone_arm = ['Petal','Feather']
mammoth_tusk = ['Fang','Horn']
ruby_vest = ['Fang','Feather']
stone_helm = ['Horn','Feather']
"""