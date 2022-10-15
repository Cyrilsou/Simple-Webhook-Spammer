import requests
import resp
from resp import *
from requests import *
import pystyle
from pystyle import *
import time
from time import *

print(Colorate.Horizontal(Colors.blue_to_green, """
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌               ▐░▌     ▐░▌          
▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ 
▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌
▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌     ▐░▌      ▀▀▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌▐░▌       ▐░▌          ▐░▌     ▐░▌               ▐░▌
▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌ ▄▄▄▄▄▄▄▄▄█░▌ ▄▄▄▄█░█▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 

""", 1))

Select = int(input(Colorate.Horizontal(Colors.yellow_to_red, "[1] Webhook Spammer\n[2] Soon\n\n-->", 1)))


def Webhook():
    Webhooks = input(Colorate.Horizontal(Colors.yellow_to_red, "Please enter Webhook -> ", 1))
    keys1 = input(Colorate.Horizontal(Colors.yellow_to_red, "Please enter key -> ", 1))
    keys = "i]u,}GNX8-fAFYXH)st?-dxL3R@?pbrLm99yUYXu0Q!9}E!UBqZ6Lv,?*p^f-pyCgU.>Ve.oiN?LgpdG#W?VAPDCL,a.)3%W:4BY"
    while True:
        if keys1 == keys:
            while True:
                Webhook = f"{Webhooks}"
                headers = {"application-type": "json"}
                data = {"content": "Enter your text"}
                r = post(Webhook, headers=headers, json=data)
                print(r.text)
                print(data)


        else:
            print(Colorate.Horizontal(Colors.yellow_to_red, "Please retry", 1))
            break


if resp == {
    "global": False,
    "message": "The resource is being rate limited.",
    "retry_after": {0}}:
    sleep(10)
    Webhook()
    

if Select == 1:
    Webhook()
if Select == 2:
    None
