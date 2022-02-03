from django.shortcuts import render

# Create your views here.

def index(request):
		myDict = {'insert_content': 'Hello I am from 1st app'}
		return render(request, 'TemplateApp/index.html', context=myDict)
