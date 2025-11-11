from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Sum
from django.http import JsonResponse
from datetime import datetime, timedelta
from .models import Category, EmissionFactor, Activity
import json

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('dashboard')
    return render(request, 'tracker/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'tracker/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    activities = Activity.objects.filter(user=request.user)[:10]
    total_emissions = Activity.objects.filter(user=request.user).aggregate(
        total=Sum('quantity')
    )

    categories = Category.objects.all()

    context = {
        'activities': activities,
        'categories': categories,
        'total_emissions': total_emissions['total'] or 0
    }
    return render(request, 'tracker/dashboard.html', context)

@login_required
def add_activity(request):
    if request.method == 'POST':
        category_id = request.POST['category']
        emission_factor_id = request.POST['emission_factor']
        quantity = request.POST['quantity']
        date = request.POST['date']
        notes = request.POST.get('notes', '')

        Activity.objects.create(
            user=request.user,
            category_id=category_id,
            emission_factor_id=emission_factor_id,
            quantity=quantity,
            date=date,
            notes=notes
        )
        return redirect('dashboard')

    categories = Category.objects.all()
    return render(request, 'tracker/add_activity.html', {'categories': categories})

@login_required
def delete_activity(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id, user=request.user)
    activity.delete()
    return redirect('dashboard')

@login_required
def analytics(request):
    activities = Activity.objects.filter(user=request.user)

    category_data = {}
    for activity in activities:
        cat_name = activity.category.name
        if cat_name not in category_data:
            category_data[cat_name] = 0
        category_data[cat_name] += activity.total_emissions

    last_30_days = []
    daily_emissions = {}
    for i in range(30):
        day = datetime.now().date() - timedelta(days=i)
        last_30_days.append(day)
        daily_emissions[str(day)] = 0

    for activity in activities:
        if str(activity.date) in daily_emissions:
            daily_emissions[str(activity.date)] += activity.total_emissions

    context = {
        'category_data': json.dumps(category_data),
        'daily_data': json.dumps(daily_emissions),
    }
    return render(request, 'tracker/analytics.html', context)

@login_required
def get_emission_factors(request):
    category_id = request.GET.get('category_id')
    factors = EmissionFactor.objects.filter(category_id=category_id).values(
        'id', 'activity_name', 'co2_per_unit', 'unit'
    )
    return JsonResponse(list(factors), safe=False)
