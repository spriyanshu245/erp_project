from django.urls import path
from django.conf.urls import url
from department import views
# from .views import dept_act_1DeleteView

urlpatterns = [

       path('', views.add_show, name="add_show"),
    path('delete/<int:id>/', views.delete_data, name="delete"),
    path('update/<int:id>/', views.update_data, name="update"),
    

    url(r'^dept_act_1/$', views.dept_act_1, name="dept_act_1"),
    # path('<pk>/delete/', dept_act_1DeleteView.as_view()),
    path('dept_act_2/', views.dept_act_2, name="dept_act_2"),
    path('dept_act_3/', views.dept_act_3, name="dept_act_3"),
    path('dept_act_4/', views.dept_act_4, name="dept_act_4"),
    path('dept_act_5/', views.dept_act_5, name="dept_act_5"),
    path('dept_act_6/', views.dept_act_6, name="dept_act_6"),    


    url(r'^fac_achieve/$', views.fac_achieve, name="fac_achieve"),
    path('fac_book', views.fac_book, name="fac_book"),


    path('cur_input_1', views.cur_input_1, name="cur_input_1"),
    path('cur_input_2', views.cur_input_2, name="cur_input_2"),
    path('cur_input_3', views.cur_input_3, name="cur_input_3"),
    path('cur_input_4', views.cur_input_4, name="cur_input_4"),
    path('cur_input_5', views.cur_input_5, name="cur_input_5"),

    path('ind_inst_1', views.IndInst1Create.as_view(), name="ind_inst_1"),
]
