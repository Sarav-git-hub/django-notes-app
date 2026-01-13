from django.shortcuts import render,redirect
from .models import Note
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request,"Registration Success Welcome")
            return redirect('index')
    else:
        form=UserCreationForm()
    return render(request,'register.html',{'form':form})


def create_note(request):
    if request.method=="POST":
        v_title=request.POST.get('n_title')
        v_content=request.POST.get('n_content')
        Note.objects.create(title=v_title,content=v_content,user=request.user)
        messages.success(request,"Note Successfully Created")
        return redirect('index')
    return render(request,'add_note.html')

@login_required
def index(request):
    all_notes=Note.objects.filter(user=request.user)

    query=request.GET.get('q')
    if query:
        all_notes=all_notes.filter(Q(title__icontains=query) | Q(content__icontains=query))
    return render(request,'index.html',{'notes':all_notes})

@login_required
def delete_note(request,note_id):
    note=Note.objects.filter(id=note_id,user=request.user).first()
    if note:
        note.delete()
        messages.warning(request,"Note Deleted")
    else:
        messages.error(request,"You can't delete this note")
    return redirect('index')

@login_required
def edit_note(request,note_id):
    note=Note.objects.filter(id=note_id,user=request.user).first()
    if not note:
        messages.error(request,"You can't edit this note")
        return redirect('index')
    if request.method=="POST":
        note.title=request.POST.get('n_title')
        note.content=request.POST.get('n_content')
        note.save()
        messages.success(request,"Note Successfully Updated")
        return redirect('index')
    return render(request,'edit_note.html',{'note':note})

@login_required
def toggle_pin(request,note_id):
    note=Note.objects.filter(id=note_id,user=request.user).first()
    if note:
        note.is_pinned= not note.is_pinned
        note.save()
    return redirect('index')



