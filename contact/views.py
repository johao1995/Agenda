from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact
from .forms import  ContactForm

def list_contact(request):
    template_name='contact/index.html'
    name=request.GET.get('name','')
    print(name) 
    contact=Contact.objects.filter(name__contains=name)
    context={
        'contactos':contact
    }
    return render(request,template_name,context)

def detail_contact(request,pk):
    template_name='contact/detail.html'
    pk_contacto=pk
    contactos=Contact.objects.get(pk=pk_contacto)
    context={
        'title':'Detalle De Contacto',
        'contactos':contactos
    }
    return render(request,template_name,context)

def edit_contact(request,pk):
    template_name='contact/edit.html'
    contact=Contact.objects.get(pk=pk)
    if request.method=="GET":   
        form=ContactForm(instance=contact)
        context={
            'form':form,
            'pk':pk,
            'title':'Actualizar Datos'
        }
        return render(request,template_name,context)
    elif request.method=="POST":
        Contact.objects.filter(pk=pk).update(
            name=request.POST['name'],
            last_name=request.POST['last_name'],
            phone=request.POST['phone'],
            mobile=request.POST['mobile'],
            company=request.POST['company'],
            email=request.POST['email'],
            date=request.POST['date'],
            notes=request.POST['notes']
        )
        return redirect('contact:list-contact')


    
def delete_contact(request,pk):
    Contact.objects.filter(pk=pk).delete()
    return redirect('contact:list-contact')

def create_contact(request):
    template_name='contact/create.html'
    if request.method=="GET":
        form=ContactForm()
        context={
            'form':form
        }
        return render(request,template_name,context)
    elif request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact:list-contact')
        else:
            context={'form':form}
            return render(request,template_name,context)