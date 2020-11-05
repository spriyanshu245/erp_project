from django.urls import path
from django.conf.urls import url
from department import views
from django.contrib.auth import views as auth_views
# from .views import dept_act_1DeleteView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(),name="login"),
    path('logout/', auth_views.LogoutView.as_view(),name="logout"),
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
    path('fac_book/', views.fac_book, name="fac_book"),


    path('cur_input_1/', views.cur_input_1, name="cur_input_1"),
    path('cur_input_2/', views.cur_input_2, name="cur_input_2"),
    path('cur_input_3/', views.cur_input_3, name="cur_input_3"),
    path('cur_input_4/', views.cur_input_4, name="cur_input_4"),
    path('cur_input_5/', views.cur_input_5, name="cur_input_5"),

    # Industry Institute Interaction
    path('ind_inst_1/', views.IndInst1Create.as_view(), name="ind_inst_1"),
    path('ind_inst_1/update/<int:pk>/', views.IndInst1Update.as_view(), name="ind_inst_1_update"),
    path('ind_inst_1/delete/<int:pk>/', views.IndInst1Delete.as_view(), name="ind_inst_1_delete"),
    
    path('ind_inst_2/', views.IndInst2Create.as_view(), name="ind_inst_2"),
    path('ind_inst_2/update/<int:pk>/', views.IndInst2Update.as_view(), name="ind_inst_2_update"),
    path('ind_inst_2/delete/<int:pk>/', views.IndInst2Delete.as_view(), name="ind_inst_2_delete"),

    path('ind_inst_3/', views.IndInst3Create.as_view(), name="ind_inst_3"),
    path('ind_inst_3/update/<int:pk>/', views.IndInst3Update.as_view(), name="ind_inst_3_update"),
    path('ind_inst_3/delete/<int:pk>/', views.IndInst3Delete.as_view(), name="ind_inst_3_delete"),

    path('ind_inst_4/', views.IndInst4Create.as_view(), name="ind_inst_4"),
    path('ind_inst_4/update/<int:pk>/', views.IndInst4Update.as_view(), name="ind_inst_4_update"),
    path('ind_inst_4/delete/<int:pk>/', views.IndInst4Delete.as_view(), name="ind_inst_4_delete"),
    
    path('ind_inst_5/', views.IndInst5Create.as_view(), name="ind_inst_5"),
    path('ind_inst_5/update/<int:pk>/', views.IndInst5Update.as_view(), name="ind_inst_5_update"),
    path('ind_inst_5/delete/<int:pk>/', views.IndInst5Delete.as_view(), name="ind_inst_5_delete"),

    path('ind_inst_6/', views.IndInst6Create.as_view(), name="ind_inst_6"),
    path('ind_inst_6/update/<int:pk>/', views.IndInst6Update.as_view(), name="ind_inst_6_update"),
    path('ind_inst_6/delete/<int:pk>/', views.IndInst6Delete.as_view(), name="ind_inst_6_delete"),

    path('ind_inst_7/', views.IndInst7Create.as_view(), name="ind_inst_7"),
    path('ind_inst_7/update/<int:pk>/', views.IndInst7Update.as_view(), name="ind_inst_7_update"),
    path('ind_inst_7/delete/<int:pk>/', views.IndInst7Delete.as_view(), name="ind_inst_7_delete"),

    path('ind_inst_8/', views.IndInst8Create.as_view(), name="ind_inst_8"),
    path('ind_inst_8/update/<int:pk>/', views.IndInst8Update.as_view(), name="ind_inst_8_update"),
    path('ind_inst_8/delete/<int:pk>/', views.IndInst8Delete.as_view(), name="ind_inst_8_delete"),

    path('ind_inst_9/', views.IndInst9Create.as_view(), name="ind_inst_9"),
    path('ind_inst_9/update/<int:pk>/', views.IndInst9Update.as_view(), name="ind_inst_9_update"),
    path('ind_inst_9/delete/<int:pk>/', views.IndInst9Delete.as_view(), name="ind_inst_9_delete"),

]

#handler404 = ''