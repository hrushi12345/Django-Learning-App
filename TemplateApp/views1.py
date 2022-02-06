import sys
from django.shortcuts import render

# Create your views here.

def index(request):
    try:
        myDict = {"insert_content": "Hello I am from 1st app"}
        return render(request, "TemplateApp/index.html", context=myDict)
    except Exception as e:
        print("Error on line {}".format(sys.exc_info()[-1].tb_lineno))
        raise
