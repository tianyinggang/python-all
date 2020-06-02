# q1

'''
dicttoxml
pip install dicttoxml
pip install xmltodict


'''

import dicttoxml
import os
from xml.dom.minidom import parseString

d = [20,'names',{'name':'Bill','age':30,'salary':2000},
                {'name':'Mike','age':40,'salary':3000},
                {'name': 'John', 'age': 20, 'salary': 1000}]

bxml = dicttoxml.dicttoxml(d,custom_root='persons')
xml = bxml.decode('utf-8')
print(xml)
dom = parseString(xml)
prettyxml = dom.toprettyxml(indent='  ')
print(prettyxml)

f = open('files/persons1.xml','w',encoding='utf-8')
f.write(prettyxml)
f.close()

import xmltodict
f = open('files/products.xml','rt',encoding='utf-8')
xml = f.read()
import pprint
d = xmltodict.parse(xml)

print(d)
pp = pprint.PrettyPrinter(indent= 4)
pp.pprint(d)
print(type(d))
