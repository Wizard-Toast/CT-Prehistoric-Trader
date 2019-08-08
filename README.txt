Built on Python 3.7.4 (x64)

To use:
Double click CT_Prehistory_Trader.py to begin trader.
Program assumes the player is standing in front of Ioka Village trader, with all menus and dialogue closed prior to starting.
Simulates keypresses using pyautogui to navigate trade menu; user input determines which item to trade for, and how many times to trade for that item.
Move mouse to upper left corner of your screen to stop program abruptly.
@Important: Assumes 'space' be bound to 'confirm', and 's' be bound to 'down' || can be reconfigured in tradehandler.py lines 10 & 11

Folder structure:
.../CT_Prehistory_Trader
      .../README.txt
      .../CT_Prehistory_Trader.py
      .../__init__.py
.../CT_Prehistory_Trader/modules
      .../inputparameters.py
      .../tradehandler.py
      .../__init__.py

Required:
* PyAutoGUI: "pip install pyautogui"
* Regular Expressions: "pip install regex"
* Pywin32: "pip install pywin32"

** For help with modules **
https://pyautogui.readthedocs.io/en/latest/install.html
https://pypi.org/project/regex/
https://pypi.org/project/pywin32/
**                        **