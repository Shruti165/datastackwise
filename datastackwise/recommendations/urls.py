from django.urls import path
from . import views

urlpatterns = [
    path('', views.database_recommendation_form, name='database_recommendation_form'),
    path('recommendation/', views.database_recommendation, name='recommendation_results'),
    path('database-table/', views.database_table, name='database_table'),  # New URL
]
