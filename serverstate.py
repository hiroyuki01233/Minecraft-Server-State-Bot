import discord
from discord.ext import tasks
import time
import requests

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

NOP = 0 

@tasks.loop(seconds=15)
async def loop():

    global NOP

    #とりあえず例として、どこかのWeb APIを叩くことにする
    url = "https://api.mcsrvstat.us/2/ip"

    #requests.getを使うと、レスポンス内容を取得できるのでとりあえず変数へ保存
    response = requests.get(url)

    #response.json()でJSONデータに変換して変数へ保存
    jsonData = response.json()

    players = jsonData["players"]

    playersNOP = players["online"]

    if "list" in players:

        playerslist = players["list"]

        if NOP == playersNOP:
            print("変わりなし")
        else:
            print("オンライン人数 : {0}\nオンラインプレイヤー : {1}".format(playersNOP,playerslist))
            channel = client.get_channel()
            await channel.send("オンライン人数 : {0}\nオンラインプレイヤー : {1}".format(playersNOP,playerslist))
    
    else:

        if NOP == playersNOP:
            print("変わりなし")
        else:
            channel = client.get_channel()
            await channel.send("オンライン人数 : {0}".format(NOP))
        
    NOP = playersNOP

loop.start()



client.run('')