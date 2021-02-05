from django.urls import path
from django.conf.urls import url
from department import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Test Pages
   path('testPage/', views.testPage, name="test"),

#---------------------------------------------------------------
    # Registration Page and Logins
    path('login/', auth_views.LoginView.as_view(),name="login"),
    path('logout/', auth_views.LogoutView.as_view(),name="logout"),
    
    # Shubham Login Pages
    path('register/', views.registerPage, name="register"),
    path('loginPage/', views.loginPage, name = "loginPage"),
    path('logoutPage/', views.logoutPage, name = "logoutPage"),
    # path('loginPage/', views.loginPage, name="loginPage"),

#-------------------------------------------------------------------------------------------------------------------
    # STUDENT RESULT
    path('', views.StudentResultCreate.as_view(), name="stud_result"),
    path('stud_result/update/<int:pk>/', views.StudentResultUpdate.as_view(), name="stud_result_update"),
    path('stud_result/delete/<int:pk>/', views.StudentResultDelete.as_view(), name="stud_result_delete"),
    
#-------------------------------------------------------------------------------------------------------------------
    # DEPARTMENTAL ACTIVITIES
    path('dept_act_1/', views.DeptEvent1Create.as_view(), name="dept_act_1"),
    path('dept_act_1/update/<int:pk>/', views.DeptEvent1Update.as_view(), name="dept_act_1_update"),
    path('dept_act_1/delete/<int:pk>/', views.DeptEvent1Delete.as_view(), name="dept_act_1_delete"),

    path('dept_act_2/', views.DeptEvent2Create.as_view(), name="dept_act_2"),
    path('dept_act_2/update/<int:pk>/', views.DeptEvent2Update.as_view(), name="dept_act_2_update"),
    path('dept_act_2/delete/<int:pk>/', views.DeptEvent2Delete.as_view(), name="dept_act_2_delete"),

    path('dept_act_3/', views.DeptProEvent3Create.as_view(), name="dept_act_3"),
    path('dept_act_3/update/<int:pk>/', views.DeptProEvent3Update.as_view(), name="dept_act_3_update"),
    path('dept_act_3/delete/<int:pk>/', views.DeptProEvent3Delete.as_view(), name="dept_act_3_delete"),

    path('dept_act_4/', views.DeptFacultyDev4Create.as_view(), name="dept_act_4"),
    path('dept_act_4/update/<int:pk>/', views.DeptFacultyDev4Update.as_view(), name="dept_act_4_update"),
    path('dept_act_4/delete/<int:pk>/', views.DeptFacultyDev4Delete.as_view(), name="dept_act_4_delete"),

    path('dept_act_5/', views.DeptStudPart5Create.as_view(), name="dept_act_5"),
    path('dept_act_5/update/<int:pk>/', views.DeptStudPart5Update.as_view(), name="dept_act_5_update"),
    path('dept_act_5/delete/<int:pk>/', views.DeptStudPart5Delete.as_view(), name="dept_act_5_delete"),

    path('dept_act_6/', views.DeptStartUp6Create.as_view(), name="dept_act_6"),
    path('dept_act_6/update/<int:pk>/', views.DeptStartUp6Update.as_view(), name="dept_act_6_update"),
    path('dept_act_6/delete/<int:pk>/', views.DeptStartUp6Delete.as_view(), name="dept_act_6_delete"),

#-------------------------------------------------------------------------------------------------------------------
    # FACULTY CONTRIBUTIONS
    path('fac_contri_1/', views.ResProject1Create.as_view(), name="fac_contri_1"),
    path('fac_contri_1/update/<int:pk>/', views.ResProject1Update.as_view(), name="fac_contri_1_update"),
    path('fac_contri_1/delete/<int:pk>/', views.ResProject1Delete.as_view(), name="fac_contri_1_delete"),

    path('fac_contri_2/', views.ResFunds2Create.as_view(), name="fac_contri_2"),
    path('fac_contri_2/update/<int:pk>/', views.ResFunds2Update.as_view(), name="fac_contri_2_update"),
    path('fac_contri_2/delete/<int:pk>/', views.ResFunds2Delete.as_view(), name="fac_contri_2_delete"),

    path('fac_contri_3/', views.ResInternational3Create.as_view(), name="fac_contri_3"),
    path('fac_contri_3/update/<int:pk>/', views.ResInternational3Update.as_view(), name="fac_contri_3_update"),
    path('fac_contri_3/delete/<int:pk>/', views.ResInternational3Delete.as_view(), name="fac_contri_3_delete"),

    path('fac_contri_4/', views.ResNational4Create.as_view(), name="fac_contri_4"),
    path('fac_contri_4/update/<int:pk>/', views.ResNational4Update.as_view(), name="fac_contri_4_update"),
    path('fac_contri_4/delete/<int:pk>/', views.ResNational4Delete.as_view(), name="fac_contri_4_delete"),

    path('fac_contri_5/', views.ConfInternational5Create.as_view(), name="fac_contri_5"),
    path('fac_contri_5/update/<int:pk>/', views.ConfInternational5Update.as_view(), name="fac_contri_5_update"),
    path('fac_contri_5/delete/<int:pk>/', views.ConfInternational5Delete.as_view(), name="fac_contri_5_delete"),

    path('fac_contri_6/', views.ConfNational6Create.as_view(), name="fac_contri_6"),
    path('fac_contri_6/update/<int:pk>/', views.ConfNational6Update.as_view(), name="fac_contri_6_update"),
    path('fac_contri_6/delete/<int:pk>/', views.ConfNational6Delete.as_view(), name="fac_contri_6_delete"),

    path('fac_contri_7/', views.ResIndustrial7Create.as_view(), name="fac_contri_7"),
    path('fac_contri_7/update/<int:pk>/', views.ResIndustrial7Update.as_view(), name="fac_contri_7_update"),
    path('fac_contri_7/delete/<int:pk>/', views.ResIndustrial7Delete.as_view(), name="fac_contri_7_delete"),

    path('fac_contri_8/', views.FacEvents8Create.as_view(), name="fac_contri_8"),
    path('fac_contri_8/update/<int:pk>/', views.FacEvents8Update.as_view(), name="fac_contri_8_update"),
    path('fac_contri_8/delete/<int:pk>/', views.FacEvents8Delete.as_view(), name="fac_contri_8_delete"),

    path('fac_contri_9/', views.ProfessionalPrac9Create.as_view(), name="fac_contri_9"),
    path('fac_contri_9/update/<int:pk>/', views.ProfessionalPrac9Update.as_view(), name="fac_contri_9_update"),
    path('fac_contri_9/delete/<int:pk>/', views.ProfessionalPrac9Delete.as_view(), name="fac_contri_9_delete"),

    path('fac_contri_10/', views.FacPatents10Create.as_view(), name="fac_contri_10"),
    path('fac_contri_10/update/<int:pk>/', views.FacPatents10Update.as_view(), name="fac_contri_10_update"),
    path('fac_contri_10/delete/<int:pk>/', views.FacPatents10Delete.as_view(), name="fac_contri_10_delete"),

    path('fac_contri_11/', views.NationalAttend11Create.as_view(), name="fac_contri_11"),
    path('fac_contri_11/update/<int:pk>/', views.NationalAttend11Update.as_view(), name="fac_contri_11_update"),
    path('fac_contri_11/delete/<int:pk>/', views.NationalAttend11Delete.as_view(), name="fac_contri_11_delete"),

    path('fac_contri_12/', views.InternationalAttend12Create.as_view(), name="fac_contri_12"),
    path('fac_contri_12/update/<int:pk>/', views.InternationalAttend12Update.as_view(), name="fac_contri_12_update"),
    path('fac_contri_12/delete/<int:pk>/', views.InternationalAttend12Delete.as_view(), name="fac_contri_12_delete"),

#-------------------------------------------------------------------------------------------------------------------
    # FACULTY ACHIEVEMENT
    path('fac_achieve/', views.FacAchieveCreate.as_view(), name="fac_achieve"),
    path('fac_achieve/update/<int:pk>/', views.FacAchieveUpdate.as_view(), name="fac_achieve_update"),
    path('fac_achieve/delete/<int:pk>/', views.FacAchieveDelete.as_view(), name="fac_achieve_delete"),

    path('fac_book/', views.FacBookCreate.as_view(), name="fac_book"),
    path('fac_book/update/<int:pk>/', views.FacBookUpdate.as_view(), name="fac_book_update"),
    path('fac_book/delete/<int:pk>/', views.FacBookDelete.as_view(), name="fac_book_delete"),


#-------------------------------------------------------------------------------------------------------------------
    # INDUSTRY INSTITUTE INTERACTION
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

#------------------------------------------------------------------------------------------------------------------- 
    # CURRICULUM INPUT
    path('cur_input_1/', views.CurGuestLect1Create.as_view(), name="cur_input_1"),
    path('cur_input_1/update/<int:pk>/', views.CurGuestLect1Update.as_view(), name="cur_input_1_update"),
    path('cur_input_1/delete/<int:pk>/', views.CurGuestLect1Delete.as_view(), name="cur_input_1_delete"),

    path('cur_input_2/', views.CurExptLect2Create.as_view(), name="cur_input_2"),
    path('cur_input_2/update/<int:pk>/', views.CurExptLect2Update.as_view(), name="cur_input_2_update"),
    path('cur_input_2/delete/<int:pk>/', views.CurExptLect2Delete.as_view(), name="cur_input_2_delete"),

    path('cur_input_3/', views.CurStudTrain3Create.as_view(), name="cur_input_3"),
    path('cur_input_3/update/<int:pk>/', views.CurStudTrain3Update.as_view(), name="cur_input_3_update"),
    path('cur_input_3/delete/<int:pk>/', views.CurStudTrain3Delete.as_view(), name="cur_input_3_delete"),

    path('cur_input_4/', views.CurStudVisit4Create.as_view(), name="cur_input_4"),
    path('cur_input_4/update/<int:pk>/', views.CurStudVisit4Update.as_view(), name="cur_input_4_update"),
    path('cur_input_4/delete/<int:pk>/', views.CurStudVisit4Delete.as_view(), name="cur_input_4_delete"),

    path('cur_input_5/', views.CurStudSponsor5Create.as_view(), name="cur_input_5"),
    path('cur_input_5/update/<int:pk>/', views.CurStudSponsor5Update.as_view(), name="cur_input_5_update"),
    path('cur_input_5/delete/<int:pk>/', views.CurStudSponsor5Delete.as_view(), name="cur_input_5_delete"),

#-------------------------------------------------------------------------------------------------------------------
   # STUDENT /FACULTY SUPPORT SYSTEM
    path('stud_fac_1/', views.StudFac1Create.as_view(), name="stud_fac_1"),
    path('stud_fac_1/update/<int:pk>/', views.StudFac1Update.as_view(), name="stud_fac_1_update"),
    path('stud_fac_1/delete/<int:pk>/', views.StudFac1Delete.as_view(), name="stud_fac_1_delete"),

    path('stud_fac_2/', views.StudFac2Create.as_view(), name="stud_fac_2"),
    path('stud_fac_2/update/<int:pk>/', views.StudFac2Update.as_view(), name="stud_fac_2_update"),
    path('stud_fac_2/delete/<int:pk>/', views.StudFac2Delete.as_view(), name="stud_fac_2_delete"),

    path('stud_fac_3/', views.StudFac3Create.as_view(), name="stud_fac_3"),
    path('stud_fac_3/update/<int:pk>/', views.StudFac3Update.as_view(), name="stud_fac_3_update"),
    path('stud_fac_3/delete/<int:pk>/', views.StudFac1Delete.as_view(), name="stud_fac_3_delete"),

    path('stud_fac_4/', views.StudFac4Create.as_view(), name="stud_fac_4"),
    path('stud_fac_4/update/<int:pk>/', views.StudFac4Update.as_view(), name="stud_fac_4_update"),
    path('stud_fac_4/delete/<int:pk>/', views.StudFac4Delete.as_view(), name="stud_fac_4_delete"),

    path('stud_fac_5/', views.StudFac5Create.as_view(), name="stud_fac_5"),
    path('stud_fac_5/update/<int:pk>/', views.StudFac5Update.as_view(), name="stud_fac_5_update"),
    path('stud_fac_5/delete/<int:pk>/', views.StudFac5Delete.as_view(), name="stud_fac_5_delete"),

#-------------------------------------------------------------------------------------------------------------------
    # EXTRA CURRICULAR ACTIVITIES
    path('extra_curr_1/', views.ExtraCurr1Create.as_view(), name="extra_curr_1"),
    path('extra_curr_1/update/<int:pk>/', views.ExtraCurr1Update.as_view(), name="extra_curr_1_update"),
    path('extra_curr_1/delete/<int:pk>/', views.ExtraCurr1Delete.as_view(), name="extra_curr_1_delete"),

    path('extra_curr_2/', views.ExtraCurr2Create.as_view(), name="extra_curr_2"),
    path('extra_curr_2/update/<int:pk>/', views.ExtraCurr2Update.as_view(), name="extra_curr_2_update"),
    path('extra_curr_2/delete/<int:pk>/', views.ExtraCurr2Delete.as_view(), name="extra_curr_2_delete"),

    path('extra_curr_3/', views.CulturalAct3Create.as_view(), name="extra_curr_3"),
    path('extra_curr_3/update/<int:pk>/', views.CulturalAct3Update.as_view(), name="extra_curr_3_update"),
    path('extra_curr_3/delete/<int:pk>/', views.CulturalAct3Delete.as_view(), name="extra_curr_3_delete"),
    path('extra_currcount_3/update/<int:pk>/', views.CulturalCount3Update.as_view(), name="extra_currcount_3_update"),

    path('extra_curr_4/', views.SocialAct4Create.as_view(), name="extra_curr_4"),
    path('extra_curr_4/update/<int:pk>/', views.SocialAct4Update.as_view(), name="extra_curr_4_update"),
    path('extra_curr_4/delete/<int:pk>/', views.SocialAct4Delete.as_view(), name="extra_curr_4_delete"),

    path('extra_curr_5/', views.CentersAct5Create.as_view(), name="extra_curr_5"),
    path('extra_curr_5/update/<int:pk>/', views.CentersAct5Update.as_view(), name="extra_curr_5_update"),
    path('extra_curr_5/delete/<int:pk>/', views.CentersAct5Delete.as_view(), name="extra_curr_5_delete"),

    path('extra_curr_6/', views.ExtraAct6Create.as_view(), name="extra_curr_6"),
    path('extra_curr_6/update/<int:pk>/', views.ExtraAct6Update.as_view(), name="extra_curr_6_update"),
    path('extra_curr_6/delete/<int:pk>/', views.ExtraAct6Delete.as_view(), name="extra_curr_6_delete"),

    

#-------------------------------------------------------------------------------------------------------------------
    # E - CELL
    path('e_cell/', views.EcellCreate.as_view(), name="e_cell"),
    path('extra_curr_1/update/<int:pk>/', views.EcellUpdate.as_view(), name="e_cell_update"),
    path('extra_curr_1/delete/<int:pk>/', views.EcellDelete.as_view(), name="e_cell_delete"),

]

#handler404 = ''
