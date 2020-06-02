'''
Session(服务端，key-value）
Cookie(Map,key-value)

'''

from django.http import HttpResponse
def writeSession(request):
    request.session['name'] = 'Bill'
    request.session['age'] = 20
    return HttpResponse('writeSession')

def readSession(request):
    result = ''
    name = request.session.get('name')
    age = request.session.get('age')
    if name:
        result = '<h2>name:<font color="red">' + name + '</font></h2>'
    if age:
        result += '<h2>age:<font color="blue">' + str(age) + '</font></h2>'
    return HttpResponse(result,content_type='text/html')