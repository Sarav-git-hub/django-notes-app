from django.shortcuts import render,redirect
from .models import Note
from django.contrib import messages

def create_note(request):
    if request.method=="POST":
        v_title=request.POST.get('n_title')
        v_content=request.POST.get('n_content')
        Note.objects.create(title=v_title,content=v_content)
        messages.success(request,"Note Successfully Created")
        return redirect('index')
    return render(request,'add_note.html')

def index(request):
    all_notes=Note.objects.all()
    return render(request,'index.html',{'notes':all_notes})

def delete_note(request,note_id):
    note=Note.objects.get(id=note_id)
    note.delete()
    messages.success(request,"Note Successfully Deleted")
    return redirect('index')

def edit_note(request,note_id):
    note=Note.objects.get(id=note_id)
    if request.method=="POST":
        note.title=request.POST.get('n_title')
        note.content=request.POST.get('n_content')
        note.save()
        messages.success(request,"Note Successfully Updated")
        return redirect('index')
    return render(request,'edit_note.html',{'note':note})


