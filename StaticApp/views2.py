from django.shortcuts import render

# Create your views here.

def index(request):
		myDict = {'insert_content': 'Hello I am from 2nd app'}
		return render(request, 'StaticApp/index.html', context=myDict)
