from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from company.models import Company


# Create your views here.

def home_page(request):
    companies = Company.objects.all()

    try:
        peaku_company = Company.objects.get(pk=1)
        return render(request, 'main/home.html', {'company': peaku_company})
    except ObjectDoesNotExist:
        return render(request, 'main/Error.html')

    return render(request, 'main/home.html', {'companies': companies})

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