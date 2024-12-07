from django.urls import path
from . import views
urlpatterns=[
    #nationalaties
    path('',views.learn,name='eng_path'),
    path('nl1/',views.n_b_quiz,name='n_bl_1'),
    path('nl2/',views.n_m_quiz,name='n_ml_2'),
    path('nl3/',views.n_a_quiz,name='n_al_3'),
    #proffesional
    path('pl1/',views.prof_b_quiz,name='prf_bl_1'),
    path('pl2/', views.prof_m_quiz, name='prf_ml_2'),
    path('pl3/', views.prof_a_quiz, name='prf_al_3'),
    #people
    path('ppl1/', views.ppl_b_quiz, name='ppl_bl_1'),
    path('ppl2/', views.ppl_m_quiz, name='ppl_ml_2'),
    path('ppl3/', views.ppl_a_quiz, name='ppl_al_3'),
    #places
    path('plc1/', views.plc_b_quiz, name='plc_bl_1'),
    path('plc2/',views.plc_m_quiz,name='plc_ml_2'),
    path('plc3/', views.plc_a_quiz, name='plc_al_3'),
    #food
    path('fod1/', views.fod_b_quiz, name='fod_bl_1'),
    path('fod2/', views.fod_m_quiz, name='fod_ml_2'),
    path('fod3/',views.fod_a_quiz,name='fod_al_3'),
    #color
    path('clr1/', views.clr_b_quiz, name='clr_bl_1'),
    path('clr2/', views.clr_m_quiz, name='clr_ml_2'),
    path('clr3/',views.clr_a_quiz,name='clr_al_3'),
    #weather
    path('wth1/', views.wth_b_quiz, name='wth_bl_1'),
    path('wth2/', views.wth_m_quiz, name='wth_ml_2'),
    path('wth3/', views.wth_a_quiz, name='wth_al_3'),
    #technology
    path('tec1/',views.tec_b_quiz,name='tec_bl_1'),
    path('tec2/', views.tec_m_quiz, name='tec_ml_2'),
    path('tec3/',views.tec_a_quiz,name='tec_al_3'),
]