from django.shortcuts import render
from .models import User

# Create your views here.

def all_users(request):
    user_list = User.objects.all()
    return render(request, 'user-list.html', {
        'user_list' : user_list
    })