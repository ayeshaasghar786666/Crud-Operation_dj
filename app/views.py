from django.shortcuts import render,HttpResponseRedirect
from.forms import UserForm
from .models import User
# Create your views here.
def add(request):
    stu = User.objects.all()
    if request.method == 'POST':
        fm = UserForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm = UserForm()
    else:
        fm = UserForm()
    return render(request, 'add.html', {'forms':fm,'stud':stu})


def delete(request, id):
    if request.method == 'POST':
        fm = User.objects.get(pk=id)
        fm.delete()
    else:
        fm = UserForm()
    return HttpResponseRedirect('/')

def update(request, id):
    if request.method == 'POST':
        fm = User.objects.get(pk=id)
        fm = UserForm(request.POST,instance=fm)
        if fm.is_valid():
            fm.save()
            fm = UserForm()
    else:
        fm = User.objects.get(pk=id)
        fm = UserForm(instance=fm)
    return render(request,'update.html',{'forms':fm})
        
        
        
        
        
