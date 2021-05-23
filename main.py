import os
import telebot
import urllib.request
import ssl
import json
import time
from dotenv import load_dotenv

# /ERCGMYTV3QBOJMFR

load_dotenv()
COIN_API_KEY = os.environ.get('COIN_API_KEY')
coin_list = [
    "SAFEMOON",

]
coins = ','.join(coin_list)
map = [
    {"name":""},
    {"symbol": ""},
    {"price": " Price: "},
    {"percent_change_24h": " - 24 Hour Percent Change: "},
]
def final_render(asset_coin, value, key, asset):
    if key == 'symbol':
        asset_coin += " (" + asset[key] + ")"
    elif key == 'percent_change_24h':
        asset_coin += value + str(asset[key]) + "%"
    else:
        asset_coin += value + str(asset[key])
        # assets = 0
    return asset_coin


url = "https://api.lunarcrush.com/v2?data=assets&key=" + COIN_API_KEY + "&symbol=" + coins
assets = json.loads(urllib.request.urlopen(url).read())
for asset in assets['data']:
        asset_coin = ""
        for field in map:
            key = list(field.keys())[0]
            value = list(field.values())[0]
            asset_coin = final_render(asset_coin, value, key, asset)
        print(asset_coin)

# print(assets.price)

# print(os.environ.get('API_KEY'))

API_KEY = os.environ.get('API_KEY')
print(API_KEY)
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['/SAFEMOON'])
def greet(message):
    bot.reply_to(message, asset_coin)

bot.polling()

