from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import Details
from .models import Student
# Create your views here.
def det(request):
    d=Details()
    if request.method=="POST":
        d1=Details(request.POST)
        if d1.is_valid():
            d1.save()
            return redirect('getdata')
    return render(request,'form.html',{'d':d})
def getdata(request):
    s1=Student.objects.all()
    return render(request,'getdata1.html',{'s1':s1})
def edit(request,id):
    s2=get_object_or_404(Student,id=id)
    form=Details(instance=s2)
    return render(request,'edit.html',{'form':form,'s2':s2})
def update(request,id):
    s2=get_object_or_404(Student,id=id)
    if request.method=="POST":
        form=Details(request.POST,instance=s2)
        if form.is_valid():
            form.save()
            return redirect('getdata')
    else:
        form = Details(instance=s2)
    return render(request,'edit.html',{'form':form,'s2':s2})

def destroy(request,id):
    s2=Student.objects.get(id=id)
    s2.delete()
    return redirect('getdata')