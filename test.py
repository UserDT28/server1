import os, sys
import requests, json
import uuid, threading
import time, random, string
import platform, hashlib
try:
    from lequangminh import *
except:
    os.system('pip install lequangminh')
    os.sys.exit()
try:
    from requests import *
except:
    os.system('pip install requests')
    os.sys.exit()
blue = Col.light_blue

lblue = Colors.StaticMIX((Col.light_blue, Col.white, Col.white))

red = Colors.StaticMIX((Col.red, Col.white, Col.white))
def format_print(symbol, text):
    return f"""                      {Col.Symbol(symbol, lblue, blue)} {lblue}{text}{Col.reset}"""

def format_input(symbol, text):
    return f"""                      {Col.Symbol(symbol, red, blue)} {red}{text}{Col.reset}"""
  
# [ Banner ]  
def Banner():
    os.system("cls" if os.name == "nt" else "clear")
    title = "\n\n\n"
    banner = """\n                ----------INFO ADMIN----------
    \n        •Facebook : https://www.facebook.com/dtien17228
    \n•Zalo : 0338.743.623              |   Author: DOAN DUC TIEN 
    \n•RANDOM tại : Randomdtizen2.site  |   Youtube: D T I Z E N 2 
    \n\n\n\n"""

    print(Colorate.Vertical(Colors.DynamicMIX((Col.light_green, Col.light_gray)), Center.XCenter(title)) + Colorate.Vertical(Colors.DynamicMIX((Col.light_red, Col.light_blue)), Center.XCenter(banner.center(100))))
