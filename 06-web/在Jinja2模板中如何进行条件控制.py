from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('if.txt',user=None,intValue = 13,list=[1,2,3],dict={'a':'b'},value=None)
'''
列表或字典，None或空，被认为是False，否则是True
'''
if __name__ =='__main__':
    app.run()