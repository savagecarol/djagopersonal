from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
import requests as request
import json
def index(requests):
    if(requests.method=='POST'):
        firstname_r = requests.POST.get('fname')
        lastname_r = requests.POST.get('lname')
        r=request.get('http://api.icndb.com/jokes/random?firstName='+ firstname_r +'&lastName=' + lastname_r )
        json_data=json.loads(r.text)
        joke=json_data.get('value').get('joke')
        context={'joker' : joke }
        return render(requests, 'blog/index.html', context )
    else:
        firstname_r = requests.POST.get('fname')
        lastname_r = requests.POST.get('lname')
        r = request.get('http://api.icndb.com/jokes/random?firstName=Kartikeya&lastName=Sharma')
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')
        context = {'joker': joke}
        return render(requests,'blog/index.html',context)
# Create your views here.

def contact(requests):
    if(requests.method=='POST'):
        email_r=requests.POST.get('email')
        subject_r=requests.POST.get('subject')
        message_r=requests.POST.get('message')
        c=Contact(email=email_r,subject=subject_r,message=message_r)
        c.save()
        return render(requests, 'blog/thank.html')
    else:
        return render(requests,'blog/contact.html')



# http://api.icndb.com/jokes/random?firstName=john&lastName=Doe