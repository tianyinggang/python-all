import requests

r = requests.get('http://t.cn/EfgN7gz')
#print(r.text)
with open('book.png','wb') as f:
    f.write(r.content)