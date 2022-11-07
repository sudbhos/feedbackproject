from django.shortcuts import render
from .import forms
# Create your views here.

def thanks(request):
    return render(request,"test/hello.html")

def infor(request):
    if request.method=="GET":
        form = forms.feedbackinfo()
        return render(request, "test/index.html", {'form': form})

    if request.method=="POST":
        form=forms.feedbackinfo(request.POST)
        if form.is_valid():
            print("Form validation successfully printing form information.")
            print("Name: ",form.cleaned_data["name"])
            print("Roll No :",form.cleaned_data["rollno"])
            print("Email: ",form.cleaned_data["email"])
            print("Feedback :",form.cleaned_data["feedback"])
            # return thanks(request)
        return render(request, "test/index.html", {'form': form})


