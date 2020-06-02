'''
q1：
可以处理的数据类型：str、int、list、tuple、dict、bool、None

但datetime不支持json序列化的，

'''

'''
q2：

default
'''
import json
from datetime import datetime,date
class DateToJson(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj,datetime):
            return obj.strftime('%Y年%m月%d日  %H:%M:%S')
        elif isinstance(obj,date):
            return obj.strftime('%Y年%m月%d日')
        else:
            return json.JSONEncoder.default(self,obj)

d = {'name':'Bill','date':datetime.now()}
print(json.dumps(d,cls=DateToJson,ensure_ascii=False))