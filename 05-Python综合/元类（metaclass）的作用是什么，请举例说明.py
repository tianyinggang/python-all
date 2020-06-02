'''
metaclass：元类，类似于创建类的模板，所有的类都是通过他来创建的，可以自由控制类的创建过程

。单例模式、ORM模式

'''

class Singleton(type):
    def __init__(self,*args,**kwargs):
        print('in __init__')
        self.__instance = None
        super(Singleton,self).__init__(*args,**kwargs)
    def __call__(self,*args,**kwargs):
        print('in __call__')
        if self.__instance is None:
            self.__instance = super(Singleton,self).__call__(*args,**kwargs)
            print(type(self.__instance))
        return self.__instance
class MyClass(metaclass=Singleton):
    pass

my1 = MyClass()
my2 = MyClass()

print(my1 is my2)
