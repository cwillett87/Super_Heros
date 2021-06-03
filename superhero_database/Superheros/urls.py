from django.urls import path
from . import views


app_name = 'Superheros'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:superhero_id>/', views.details, name='details'),
    path('new/', views.create, name='create'),
    path('edit/<int:hero_id>/', views.edit, name='edit')
    # path('delete/', views.delete, name='delete')
]
