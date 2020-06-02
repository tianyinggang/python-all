from urllib3 import *
import threading
http = PoolManager()
disable_warnings()

f = open('urls.txt','r')
urlList = []
while True:
    url = f.readline()
    if url == '':
        break
    urlList.append(url.strip())
f.close()

print(urlList)

class DownloadThread(threading.Thread):
    def __init__(self,func,args):
        super().__init__(target=func,args=args)

def download(filename,url):
    response = http.request('GET',url)
    f = open(filename,'wb')
    f.write(response.data)
    f.close()
    print('<',url,'>','下载完成')

for i in range(len(urlList)):
    thread = DownloadThread(download,(str(i) + '.jpg',urlList[i]))
    thread.start()
