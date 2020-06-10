import re #提供 Perl 风格的正则表达式模式

s ='<a href="https://geekori.com">极客起源</a> <a href="https://www.microsoft.com">微软</a>'

result = re.findall('<a[^>]*href="([^>]*)">',s,re.I) #在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表 
print(result)
for url in result:
    print(url)