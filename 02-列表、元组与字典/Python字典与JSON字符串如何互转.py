d = {'a':123,'b':'456','c':'xyz'}
print(d)
print(type(d))
import json
json_str = json.dumps(d)
print(json_str)
print(type(json_str))

d1 = json.loads(json_str)
print(d1)
print(type(d1))