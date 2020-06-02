'''
共同点：
都是用来声明静态方法的。类名.方法名

1. @staticmethod不需要表示自身对象的self和自身类的cls参数，就像普通函数一样定义
2. @classmethod也不需要self参数，但第2个参数需要是表示自身的cls参数。避免硬编码。

'''

class MyClass:
    bar = 1 #静态变量
    def __init__(self):
        self.count = 20

    def process(self):
        print('process:',self.count)
    @staticmethod
    def static_process():
        print('static_process')
        print(MyClass.bar)
    @classmethod
    def class_process(cls):
        print('class_process')
        print(cls.bar)
        print(cls)
        cls().process()
        print(cls().count)

print(MyClass.bar)
MyClass.static_process()
MyClass.class_process()
MyClass.bar = 123
MyClass.static_process()