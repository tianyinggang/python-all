import pyquery
from pyquery import PyQuery as pq
html = '''
<div>
    <ul>
        <li class="item1" ><a href="https://geekori.com"> geekori.com</a></li>
        <li class="item"><a href="https://www.jd.com"> 京东商城（https://www.jd.com）</a></li>
        <li class="item3"><a href="https://www.taobao.com">淘宝</a></li>
        <li class="item" ><a href="https://www.microsoft.com">微软</a></li>
        <li class="item2"><a href="https://www.google.com">谷歌</a></li>                
    </ul>

</div>

'''

'''

伪类选择器
CSS选择器
'''


doc = pq(html)
# 选取第1个li节点
li = doc('li:first-child')
print(li)

# 选取最后一个li节点
li = doc('li:last-child')
print(li)

# 选取第3个li节点
li = doc('li:nth-child(3)')  # 索引从1开始
print(li)

# 选取索引小于2的li节点（索引从0开始）
li = doc('li:lt(2)')
print(li)

# 选取索引大于3的li节点（索引从0开始）
li = doc('li:gt(3)')
print(li)

# 选取序号为奇数的li节点，第1个li节点的序号为1
li = doc('li:nth-child(2n + 1)')
print(li)

# 选取序号为偶数的li节点，第1个li节点的序号为1
li = doc('li:nth-child(2n)')
print(li)

# 选取文本内容包含com的所有li节点
li = doc('li:contains(com)')
print(li)

# 选取文本内容包含com的所有节点
li = doc(':contains(com)')
print(li)