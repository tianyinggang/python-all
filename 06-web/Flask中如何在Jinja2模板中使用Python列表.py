'''
Jinja2



'''

from flask import *

app = Flask(__name__)

class MyClass:
    def func(self):
        return 'myclass func'
def myfunc():
    return 'function'

@app.route('/')
def index():
    mydict = {}
    mydict['type'] = 'dict'
    mylist = []
    mylist.append('list')
    myclass = MyClass()

    return render_template('template.txt',mydict = mydict,mylist = mylist,myclass=myclass,myfunc = myfunc)


if __name__ =='__main__':
    app.run()