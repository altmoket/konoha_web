from django.urls import path

from .views import general,consultas,PathView
urlpatterns = [
    path('', PathView.apiOverview, name='api-overview'),

    path('listar/<str:data>/<int:pk>', general.get_put_delete, name="get put delete"),
    path('listar/<str:data>', general.get_post, name="index"),
    path('crear/', general.get_post, name="create"),

    path('female-medical-ninjas/', consultas.female_medical_ninjas, name='female-medical-ninjas'),
    path('captain-in-C-rank-missions/', consultas.captain_in_C_rank_missions, name='captain-in-C-rank-missions'),
    path('ninja-invocation-in-S-rank-missions/', consultas.ninja_invocation_in_S_rank_missions, name='ninja-invocation-in-S-rank-missions'),
    path('hidden-techniques/', consultas.hidden_techniques, name='hidden-techniques'),
    path('medical-ninja-captains/', consultas.medical_ninja_captains, name='medical-ninja-captains'),
    path('highest-reward-missions/', consultas.highest_reward_missions, name='highest-reward-missions')

]
    
