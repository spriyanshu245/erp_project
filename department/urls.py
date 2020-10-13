from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^tab1/$', tab1, name="TAB 1"),
    # url(r'^tab2$', tab2, name="TAB 2"),
    # url(r'^tab3$', tab3, name="TAB 3"),

    path('', views.add_show, name="add_show"),
    path('dept_act_2/', views.dept_act_2, name="dept_act_2"),
    path('dept_act_3/', views.dept_act_3, name="dept_act_3"),
    path('dept_act_4/', views.dept_act_4, name="dept_act_4"),
    path('dept_act_5/', views.dept_act_5, name="dept_act_5"),
    path('dept_act_6/', views.dept_act_6, name="dept_act_6"),    
    path('delete/<int:id>/', views.delete_data, name="delete"),
    path('update/<int:id>/', views.update_data, name="update"),
]
