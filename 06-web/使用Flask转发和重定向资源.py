'''
转发与重定向

转发：对用户是透明的，或者说在Web浏览器中的Url是不会变的，在服务端会根据请求Url去读取特定的资源，并将
资源的内容返回给客户端
http://localhost:5000/test.html
服务端资源对于用户不一定是可访问的


重定向：用户是可见的，Web浏览器地址栏中的Url将改变
http://localhost:5000/test.html
http://localhost:5000/abc.html

服务端资源必须是可访问的

'''

from flask import *
app = Flask(__name__)
# 转发
@app.route('/test')
def test():
    return app.send_static_file('test1.txt')

# 重定向
@app.route('/abc')
def abc():
    return redirect('/static/test1.txt')




if __name__ =='__main__':
    app.run()