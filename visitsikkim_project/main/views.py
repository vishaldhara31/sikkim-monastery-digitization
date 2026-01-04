

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import Monastery
import requests
import os
import json
from openai import OpenAI
from decouple import config

# ----------------- MAIN PAGES -----------------
def index(request):
    return render(request, 'index.html')

def archives(request):
    return render(request, 'archives.html')

def tour(request):
    monasteries = Monastery.objects.all()
    return render(request, "tour.html", {"monasteries": monasteries})

def interactive(request):
    return render(request, 'interactive.html')

def manuscripts(request):
    return render(request, 'manuscipts.html')

def murals(request):
    return render(request, 'murals.html')

def cultural_calendar(request):
    return render(request, 'cultural_calendar.html')

def booking_options(request):
    return render(request, 'booking_options.html')

def travel_and_stay(request):
    return render(request, 'travel_and_stay.html')

def book(request):
    return render(request, 'book.html')

def travel(request):
    return render(request, 'travel.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    return render(request, 'book.html')

def events(request):
    return render(request, 'events.html')




# ----------------- USER AUTH -----------------
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')


def user_signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return render(request, 'signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
            return render(request, 'signup.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        login(request, user)
        messages.success(request, f"Account created successfully! Welcome, {user.username}.")
        return redirect('index')

    return render(request, 'signup.html')


def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('index')




client = OpenAI(api_key=settings.OPENAI_API_KEY)

@csrf_exempt
def chatbot_response(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "")

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_message}]
            )

            bot_reply = response.choices[0].message.content
            return JsonResponse({"reply": bot_reply})
        except Exception as e:
            return JsonResponse({"reply": f"⚠️ Error: {str(e)}"})
    return JsonResponse({"reply": "Invalid request"}, status=400)

from django.shortcuts import render

def chatapp(request):
    return render(request, "chatapp.html")
