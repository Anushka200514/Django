from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    peoples=[
        {'name':'Anushka Chaturvedi','age':100},
        {'name':'muskan verma','age':78},
        {'name':'Ashustosh Rana','age':17},
        {'name':'Anamika','age':40},


    ]
    for people in peoples:
        print(people)
    return render(request,"./home/index.html")


def success_page(request):
    print("*"*10)
    return HttpResponse("<h1>Hey this a success page</h1>")