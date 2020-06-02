'''
https://music.douban.com/top250?start=25
https://music.douban.com/top250?start=50
https://music.douban.com/top250?start={}



'''

import requests
from bs4 import BeautifulSoup
import csv
import time
import re
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

# 抓取指定Top250排行榜页面
def get_url_music(url):
    html = requests.get(url,headers=headers)

    soup = BeautifulSoup(html.text,'lxml')
    aTags = soup.find_all('a',attrs={'class':'nbg'})
    for aTag in aTags:
        print(aTag['href'])
        get_music_info(filename,aTag['href'])
# 抓取专辑页面中的信息
def get_music_info(filename,url):
    html = requests.get(url,headers=headers)
    soup = BeautifulSoup(html.text,'lxml')
    # 获取专辑的名称
    name = soup.find(attrs = {'id':'wrapper'}).h1.span.text
    # 获取表演者
    author = soup.find(attrs = {'id':'info'}).find('a').text

    # 获取流派
    styles = re.findall('<span class="pl">流派:</span>&nbsp;(.*?)<br />',html.text,re.S)

    if len(styles) == 0:
        style = '未知'
    else:
        style = styles[0].strip()

    # 获取发行时间
    time = re.findall('发行时间:</span>&nbsp;(.*?)<br />',html.text,re.S)[0].strip()
    # 获取出版者
    publishers = re.findall('<span class="pl">出版者:</span>&nbsp;(.*?)<br />',html.text,re.S)
    if len(publishers) == 0:
        publisher = '未知'
    else:
        publisher = publishers[0].strip()

    info = {
        'name':name,
        'author':author,
        'style':style,
        'time':time,
        'publisher':publisher
    }
    print(info)
    save_csv(filename,info)
    # 保存分析结果
def save_csv(filename,info):
    with open(filename,'a',encoding='utf-8') as f:
        fieldnames = ['name','author','style','time','publisher']
        writer = csv.DictWriter(f,fieldnames=fieldnames)
        writer.writerow(info)

if __name__ == '__main__':
    urls = ['https://music.douban.com/top250?start={}'.format(str(i)) for i in range(0,250,25)]
    print(urls)
    filename = 'music.csv'
    with open(filename,'w',encoding='utf-8') as f:
        fieldnames = ['name','author','style','time','publisher']
        writer = csv.DictWriter(f,fieldnames = fieldnames)
        writer.writeheader()
    for url in urls:
        get_url_music(url)
        time.sleep(1)
