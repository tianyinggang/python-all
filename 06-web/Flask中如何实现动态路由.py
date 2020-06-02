'''
静态路由和动态路由

路由：Url Path
http://localhost/abc/test.html
静态路由：Path与路由函数一一对应
动态路由：多个Path与同一个路由函数对应
http://localhost/abc/test.html
http://localhost/xyz/test.html

不管访问哪一个Url，都会执行同一个服务端的路由函数

pip install flask
'''

from flask import Flask
app = Flask('__name__')
# 静态路由
@app.route('/')
def index():
    return '<h1>root</h1>'
@app.route('/greet')
def greet1():
    return '<h1>Hello everyone</h1>'
@app.route('/greet/bill')
def greetBill():
    return '<h1>你好 Bill</h1>'
# 动态路由
@app.route('/greet/<name>')
def greetName(name):
    return '<h1>hello {}</h1>'.format(name)
    
'''
如果静态路由与动态路由有冲突，优先使用静态路由


'''

@app.route('/greet/<a1>/<a2>/<a3>')
def args1(a1,a2,a3):
    return '<h1>{},{},{}</h1>'.format(a1,a2,a3)
@app.route('/greet/<a1>-<a2>-<a3>')
def args2(a1,a2,a3):
    return '<h1>{}*{}*{}</h1>'.format(a1,a2,a3)
if __name__ =='__main__':
    app.run()
