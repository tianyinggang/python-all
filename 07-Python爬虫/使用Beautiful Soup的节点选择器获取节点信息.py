from bs4 import BeautifulSoup

html = '''
<html>
<head>
   <title>获取节点信息</title>
</head>
<body>
<div>
    <ul>
        <li class="item1" value1="1234" value2 = "hello world"><a href="https://geekori.com"> geekori.com</a></li>
        <li class="item"><a href="https://www.jd.com"> 京东商城</a></li>        
    </ul>
    <button id="button1">确定</button>
    <ul>
        <li class="item3"><a href="https://www.taobao.com">淘宝</a></li>
        <li class="item" ><a href="https://www.microsoft.com">微软</a></li>
        <li class="item2"><a href="https://www.google.com">谷歌</a></li>
    </ul>
</div>
</body>
'''

soup = BeautifulSoup(html, 'lxml')
print(soup.title.name)
print(soup.title.text)
print(soup.li.attrs)
print(soup.li.attrs['value2'])
print(soup.li['value1'])
print(soup.a['href'])
print(soup.a.string)
print(soup.a.text)

