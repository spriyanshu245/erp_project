from django.urls import path
from . import views
urlpatterns = [
    path('', views.add_show, name="show_student"),
    path('delete/<int:id>/', views.delete_data, name="delete"),
    #path('edit/<int:id>/', views.edit_data, name="edit"),
]