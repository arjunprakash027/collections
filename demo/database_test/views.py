from django.shortcuts import render,redirect
from .models import details

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        print(name, age)
        new_entry = details(name=name, age=age)
        new_entry.save()
        return redirect('home')
    return render(request, 'home.html')
    
def see(request):
    data = details.objects.all()
    return render(request, 'see.html', {'data': data})