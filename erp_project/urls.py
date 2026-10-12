"""erp_project URL Configuration."""
from django.contrib import admin
from django.urls import include, path

from placement import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.add_show, name='show_student'),
    path('update/<int:id>/', views.update_data, name='update'),
    path('delete/<int:id>/', views.delete_data, name='delete'),
]
