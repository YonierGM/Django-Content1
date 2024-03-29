from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from company.models import Company


# Create your views here.

def home_page(request):
    peaku_companies = Company.objects.filter(name='PeakU')

    if not peaku_companies:
        return render(request, 'main/Error.html')
    return render(request, 'main/home.html', {'companies': peaku_companies})

def users_page(request):
    users = [
        {
            'name': 'JuanP',
            'email': 'juanp@gmail.com',
            'edad': 25
        },
        {
            'name': 'Miguel',
            'email': 'miguel@gmail.com',
            'edad': 16
        }
    ]
    return render(request, 'main/users.html', {'users': users})