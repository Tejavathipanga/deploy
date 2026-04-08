from django.shortcuts import render,redirect
from deploy_app.models import employee
from deploy_app.forms import emp_form
def details(a):
    data=employee.objects.all()
    form=emp_form()
    if a.method=='POST':
        form=emp_form(a.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    context={'form':form,
             'data':data}
    return render(a,'home.html',context)

# Create your views here.
