# -*- coding: utf-8 -*-
import time
import json
import amanobot
import urllib.parse

#from amanobot.loop import MessageLoop
TOKEN = ''
bot = amanobot.Bot(TOKEN) 


    
def enviaMsg(msg):
    #Canal do Blog: -1001379308257
    #Canal de Log: -1001498194874
    bot.sendMessage(-1001379308257,msg,parse_mode='HTML')

def primeiraCarga():
    with open('.\\blog_k21_scraper\\k21.json',mode='r',encoding='utf-8') as readfile:
        js = json.load(readfile)
    
    for post in js['posts']:
        instantview = '<a href="https://t.me/iv?url=' + urllib.parse.quote(post['url'], safe='') + '&rhash=5d81b523c3001c">.</a>'
        msg = instantview + post['title'] + '\n' + post['url'] + '\n \n' + post['tags'].replace('-','_')
        enviaMsg(msg)
        time.sleep(30)

def printTags():
    with open('.\\blog_k21_scraper\\k21.json',mode='r',encoding='utf-8') as readfile:
        js = json.load(readfile)
    
    for post in js['posts']:
        print(post['tags'].replace('-','_'))

def GeraIV():
    with open('.\\blog_k21_scraper\\k21.json',mode='r',encoding='utf-8') as readfile:
        js = json.load(readfile)
    
    for post in js['posts']:
        instantview = '<a href="https://t.me/iv?url=' + urllib.parse.quote(post['url'], safe='') + '&rhash=5d81b523c3001c">.</a>'
        bot.sendMessage(-1001498194874,instantview)
        time.sleep(1)

#GeraIV()
#primeiraCarga()
#printTags()

#def handle(msg):
#    content_type, chat_type, chat_id = amanobot.glance(msg)
#    print(msg)

#MessageLoop(bot, handle).run_as_thread()
#while 1:
#	time.sleep(10)