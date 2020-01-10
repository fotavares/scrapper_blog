# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json
import time
import urllib.parse

import agilistabot

def find_json(jsonObject,id):
    for item in jsonObject['posts']:
        if item['id'] == id:
            return True
    
    return False

while True:
    agilistabot.logRun("Verificando novos posts")
    with open('k21.json',mode='r',encoding='utf-8') as readfile:
        js = json.load(readfile)

    url = 'https://www.knowledge21.com.br/blog/'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    page = requests.get(url, headers=headers)
    html = BeautifulSoup(page.text,'html.parser')

    posts = html.find_all('article')

    for post in posts:
        id = post.attrs['id']
        if not find_json(js,id):
            title = post.find(class_='fusion-post-title').get_text().replace('\n','')
            url = post.find(class_='fusion-read-more').get('href')
            tags = ''
            categs = post.find_all(rel='category tag')
            for categ in categs:
                tags = tags + ' #'+categ.get_text().replace(' ','_')

            #print ('Gravando id: ' + id)
            agilistabot.logRun("Post Novo! " + id)
            js['posts'].append({"id":id ,"title": title,"url":url,"tags":tags})
            
            with open('k21.json',mode='w',encoding='utf-8') as readfile:
                json.dump(js,readfile, indent = 4, sort_keys=True,ensure_ascii=False)

            instantview = '<a href="https://t.me/iv?url=' + urllib.parse.quote(url, safe='') + '&rhash=5d81b523c3001c">.</a>'
            agilistabot.enviaMsg(instantview+title + '\n' + url + '\n \n' + tags)
        #else:
            #print ('id já existente: ' + id)

    time.sleep(7200)