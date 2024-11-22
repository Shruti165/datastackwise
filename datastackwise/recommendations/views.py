from django.shortcuts import render
from .forms import DatabaseForm
from .models import Database

def database_recommendation_form(request):
    if request.method == 'POST':
        form = DatabaseForm(request.POST)
        if form.is_valid():
            # Process form data here, query the database and prepare recommendations
            recommendations = Database.objects.all()
            context = {
                'form': form,
                'recommendations': recommendations,
            }
            return render(request, 'recommendations/recommendation.html', context)
    else:
        form = DatabaseForm()

    return render(request, 'recommendations/form.html', {'form': form})

def database_recommendation(request):
    # Logic to display database recommendations based on user input
    recommendations = Database.objects.all()
    return render(request, 'recommendations/recommendation.html', {'recommendations': recommendations})

def database_table(request):
    # Logic to fetch and display all database information
    databases = Database.objects.all()
    return render(request, 'recommendations/database_table.html', {'databases': databases})
