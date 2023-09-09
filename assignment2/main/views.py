from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Cyrill Adrian Wicaksono',
        'class': 'PBP KI',
        'app_name' : 'Supermarket Product Management'
    }

    return render(request, 'main.html', context)