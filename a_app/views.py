from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def registration(request):
    if request.method =="GET":
        return render(request,"index.html")
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        first= request.POST['firstinput']
        last= request.POST['lastinput']
        email= request.POST['emailinput']
        pw= bcrypt.hashpw(request.POST['pwinput'].encode(),bcrypt.gensalt()).decode()
        user = User.objects.create(first_name= first, last_name = last, email=email, password = pw)
        request.session["user_id"] = user.id
        return redirect('/home')

def home(request):
    if request.method =="GET":
        return render(request,"home.html")

def forum(request):
    if request.method =="GET":
        context = {
            # "count": request.session["like_count"],
            "message": Message.objects.all(),
            "comment": Comment.objects.all()
        }
        return render (request, "forum.html",context)
    if request.method == "POST":
        user = User.objects.get(id=request.session['user_id'])
        Message.objects.create(message=request.POST["postmessage"],  message_creator=user)
        return redirect("/forum")

def comment(request,id):
    if 'user_id' in request.session:
        if request.method == "GET":
            context = {
                "comment": Comment.objects.all()
            }
            return render(request,"wall.html",context)
        if request.method == "POST":
            user = User.objects.get(id=request.session['user_id'])
            message = Message.objects.get(id=id)
            Comment.objects.create(comment=request.POST["comment_on_message"], comment_creator =user,parent_message  = message )
            return redirect("/forum")
    return redirect('/')

def like_message(request,id):
    if request.method =="GET":
        user = User.objects.get(id=request.session['user_id'])
        message = Message.objects.get(id = id)
        user.liked_messages.add(message)
        return redirect("/forum") 

def like_comment(request,id):
    if request.method =="GET":
        user = User.objects.get(id=request.session['user_id'])
        comment = Comment.objects.get(id = id)
        user.liked_comments.add(comment)
        return redirect("/forum")

def videos (request):
    if request.method == "GET":
        return render(request,"videos.html")