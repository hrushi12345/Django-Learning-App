import sys
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . import forms
from FormApp.models import SimpleForm


# Create your views here.

@csrf_exempt
def index(request):
    try:
        return render(request, "FormApp/index.html")
    except Exception as e:
        print("Error on line {}".format(sys.exc_info()[-1].tb_lineno))
        raise e

@csrf_exempt
def formView(request):
    try:
        form = forms.FormName()
        if request.method == "POST":
            form = forms.FormName(request.POST)
            if form.is_valid():
                print("Validation Success!!!")
                print("NAME : ", form.cleaned_data["name"])
                print("ADDRESS : ", form.cleaned_data["address"])
                print("EMAIL : ", form.cleaned_data["email"])
                name = form.cleaned_data["name"]
                address = form.cleaned_data["address"]
                email = form.cleaned_data["email"]
                SimpleForm.objects.create(name=name, address=address, email=email)
                print("Entry created successfully!!!")
        return render(request, "FormApp/formPage.html", {"Form": form})
    except Exception as e:
        print("Error on line {}".format(sys.exc_info()[-1].tb_lineno))
        raise e