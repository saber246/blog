import pymysql  # noqa: N999
from django.http import HttpResponse

pymysql.install_as_MySQLdb()

def hello(request):
    return HttpResponse("Hello world ! ")