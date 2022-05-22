from .models import Student
from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm
from django.contrib import messages


def index(request):
    students  = Student.objects.all()
    context = {
        'students' : students,
    }
    return render(request, 'fscohort/index.html', context)

def student_list(request):
    students  = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'fscohort/student_list.html', context)



def student_add(request):        
    form = StudentForm(request.POST or None, request.FILES or None)
    if form.is_valid():				   
        form.save()
        messages.success(request, "Öğrenci başarıyla oluşturuldu!")
        return redirect("list")   	   
    context = {
        'form' : form
        }
    return render(request, 'fscohort/student_add.html', context)

def student_update(request, id):
    student =Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method== "POST":
        form = StudentForm(request.POST or None, request.FILES or None ,instance=student)
        if form.is_valid():
            form.save()
            messages.warning(request, "Öğrenci bilgileri güncellendi!")
            return redirect("list")   
    context = {
        'form':form,
    }
    return render(request, 'fscohort/student_update.html', context)

def student_delete(request, id):
    # student = get_object_or_404(Student, id=id)
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.delete()
        return redirect("list")
    
    context = {
        'student' : student
    }
    return render(request, "fscohort/student_delete.html", context)

def student_detail(request, id):        
    student = get_object_or_404(Student, id=id)
    context = {
        'student': student,
    }
    return render(request, 'fscohort/student_detail.html', context)






