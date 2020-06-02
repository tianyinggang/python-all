from django.shortcuts import  render
class MyClass:
    name = 'Bill'
def myFor(request):
    values = {'values':[{'name':'item1'},MyClass(),{'name':'Mike'}]}
    return render(request,'for.html',values)