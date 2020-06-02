import json
class Product:
    def __init__(self,d):
        self.__dict__ = d

f = open('files/product.json','r')
jsonStr = f.read()
print(jsonStr)
product = json.loads(jsonStr,object_hook=Product)
print(type(product))
#print(product['name'])
print(product.name)
print(product.price)

def json2Product(d):
    return Product(d)

product1 = json.loads(jsonStr,object_hook=json2Product)
print(product1.name)
print(product1.price)


