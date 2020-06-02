from django.conf.urls import url

from . import session,myfor

urlpatterns = [
    url(r'^writeSession$',session.writeSession),
    url(r'^readSession$',session.readSession),
    url(r'^for$',myfor.myFor)

]