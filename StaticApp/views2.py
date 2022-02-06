from django.shortcuts import render
import sys

# Create your views here.

def index(request):
    try:
        myDict = {"insert_content": "Hello I am from 2nd app"}
        return render(request, "StaticApp/index.html", context=myDict)
    except Exception as e:
        print("Error on line {}".format(sys.exc_info()[-1].tb_lineno))
        raise e
