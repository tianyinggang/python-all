d = {'a':123,'b':'456','c':'xyz'}
print(d)
print(type(d))#输出d的类型
import json
#dumps是将dict转化成str格式，loads是将str转化成dict格式。
json_str = json.dumps(d)
print(json_str)
print(type(json_str))

d1 = json.loads(json_str)
print(d1)
print(type(d1))