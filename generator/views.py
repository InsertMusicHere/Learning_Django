from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
#def home(request):
    #return HttpResponse('Hello there!')
#have created new folder template then
#generator folder inside template
#then home.html file in generator folder
#now changing views.py by this below given code
def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):

    charecters = list('abcdefghijklmnopqrstuvwxyz')

    #if user selects uppercase charecters
    if request.GET.get('uppercase'):
        charecters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        charecters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        charecters.extend(list('1234567890'))


    #to make the length of password change just by changing
    #the url ex www...../pass/length = 2 and 12 means by default
    #it will have 12 as length
    #note that this value length is present in home.html as action
    length = int(request.GET.get('length'))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(charecters)

    return render(request, 'generator/password.html',{'password':thepassword})
