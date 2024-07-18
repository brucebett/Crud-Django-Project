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


def editStudent(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        editForm = Students.objects.get(id=id)
        editForm.name = name
        editForm.email = email
        editForm.age = age
        editForm.gender = gender
        editForm.save()
        return redirect("/")
    student = Students.objects.get(id=id)
    context = {'student': student}
    return render(request, "edit.html", context)


def deleteStudent(request,id):
    student = Students.objects.get(id=id)
    student.delete()
    return redirect("/")


























