#  q1
import json

class Product:
    def __init__(self,name,price,count):
        self.name = name
        self.price = price
        self.count = count
product = Product('特斯拉',1000000,20)
def product2Dict(obj):
    return {
        'name':obj.name,
        'price':obj.price,
        'count':obj.count
    }
jsonStr = json.dumps(product, default=product2Dict,ensure_ascii=False)
print(jsonStr)

# q2

f = open('files/products.json','r',encoding='utf-8')
jsonStr = f.read()

class Product:
    def __init__(self,d):
        self.__dict__ = d
products = json.loads(jsonStr,object_hook=Product)
print(products)
for product in  products:
    print(product.name)


jsonStr = json.dumps(products, default=product2Dict,ensure_ascii=False)
print(type(jsonStr))