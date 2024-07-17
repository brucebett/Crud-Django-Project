from django.shortcuts import render, redirect

from app.models import Students


# Create your views here.
def index(request):
    data = Students.objects.all()
    context = {'data': data}
    return render(request, 'index.html', context)


def save(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        form = Students(name=name, email=email, age=age, gender=gender)
        form.save()
        return redirect("/")
    return render(request, 'index.html')
