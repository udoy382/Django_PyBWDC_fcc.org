from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.


# def home(request):
#     context = {
#         "first_name": "Anjaneyulu",
#         "last_name": "Batta",
#         "address": "Hyderabad, India"
#     }

#     # return HttpResponse('<h1>Hey! Welcome</h>')
#     return render(request, 'home.html', context)

"""
def index(request):
    feature1 = Feature()
    feature1.id = 1
    feature1.name = 'First Item 1'
    feature1.is_true = True
    feature1.content = 'We are too Fast 1'

    feature2 = Feature()
    feature2.id = 2
    feature2.name = 'First Item 2'
    feature2.is_true = True
    feature2.content = 'We are too Fast 2'

    feature3 = Feature()
    feature3.id = 3
    feature3.name = 'First Item 3'
    feature3.is_true = False
    feature3.content = 'We are too Fast 3'

    feature4 = Feature()
    feature4.id = 4
    feature4.name = 'First Item 4'
    feature4.is_true = True
    feature4.content = 'We are too Fast 4'

    features = [feature1, feature2, feature3, feature4]

    return render(request, 'index.html', {'features':features})
"""


def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features':features})

def counter(request):
    # text = request.GET['text']
    # text = request.POST['text']
    # amount_of_text = len(text.split())

    posts = [1, 2, 3, 4, 5, 'tim', 'tom', 'udoy']

    # return render(request, 'counter.html', {'amount':amount_of_text})
    return render(request, 'counter.html', {'posts':posts})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password Not The Same')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)

    return redirect('/')



def post(request, pk):
    return render(request, 'post.html', {'pk':pk})