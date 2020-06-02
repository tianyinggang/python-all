a = ['a','b']
b = [1,2]

print(dict(zip(a,b)))

fields = ('id','name','age')
records = [['01','Bill','20'],['02','Mike','30']]
result = []
for record in records:
    result.append(dict(zip(fields,record)))
print(result)
'''
[
{'id':'01','name':'Bill','age':'20'},
{'id':'02','name':'Mike','age':'30'},
]
'''