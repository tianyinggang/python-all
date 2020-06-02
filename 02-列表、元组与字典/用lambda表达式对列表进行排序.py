a = [
    {'name':'Bill','age':40},
    {'name':'Mike','age':12},
    {'name':'Johb','age':29}
]

print(a)
print(sorted(a,key=lambda x:x['age']))

a.sort(key=lambda x:x['age'],reverse=True)
print(a)
