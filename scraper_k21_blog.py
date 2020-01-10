# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time

#reload(sys)
#sys.setdefaultencoding('utf-8')
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

f = open('.\\blog_k21_scraper\\k21.json',mode='w',encoding='utf-8')
meses = [1,2,3,4,5,6,7,8,9,10,11,12]
anos = [2013,2014,2015,2016,2017,2018,2019,2020]
f.write('{\n"posts":[')
for ano in anos:
    for mes in meses:
        print(str(ano)+' '+str(mes))
        url = 'https://www.knowledge21.com.br/blog/'+ str(ano) +'/'+ str(mes) +'/'
        page = requests.get(url, headers=headers)
        html = BeautifulSoup(page.text,'html.parser')

        posts = html.find_all('article')
        posts.reverse()
        for post in posts:
            id = post.attrs['id']
            title = post.find(class_='fusion-post-title').get_text().replace('\n','')
            #resumo = post.find(class_='fusion-post-content-container').get_text().replace('\n','')
            url = post.find(class_='fusion-read-more').get('href')
            tags = ''
            categs = post.find_all(rel='category tag')
            for categ in categs:
                tags = tags + ' #'+categ.get_text().replace(' ','_')

            f.write('{"id":"'+id + '",\n"title":"' + title + '",\n"url":"' + url + '",\n"tags":"' + tags + '"},\n')
        
        time.sleep(10)
f.write(']}')
        
f.close()
