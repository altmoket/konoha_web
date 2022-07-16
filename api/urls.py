from django.urls import path

from .views import PersonaView, NinjaView, BestiaMisionPergaminoView,BestiaMiticaView, ChuninView, EquipoEnMisionPergaminoView, EquipoEnMisionView, EquipoView, GeninView, JouninView, MisionView, NinjaMedicoView, NinjaTecnicaView, PathView, PergaminoView, TecnicaAtaqueView, TecnicaCurativaView, TecnicaView
urlpatterns = [
    path('', PathView.apiOverview, name='api-overview'),
    
    path('personas/', PersonaView.persona_list, name='personas'),
    path('personas/<str:pk>/', PersonaView.persona_detail, name='persona_detail'),
    
    path('ninjas/', NinjaView.ninja_list, name='ninjas'),
    path('ninjas/<str:pk>/', NinjaView.ninja_detail, name='ninja_detail'),
    
    path('genins/', GeninView.genin_list, name='genins'),
    path('genins/<str:pk>/', GeninView.genin_detail, name='genin_detail'),
    
    path('chunins/', ChuninView.chunin_list, name='chunins'),
    path('chunins/<str:pk>/', ChuninView.chunin_detail, name='chunin_detail'),
    
    path('jounins/', JouninView.jounin_list, name='jounins'),
    path('jounins/<str:pk>/', JouninView.jounin_detail, name='jounin_detail'),
    
    path('tecnicas/', TecnicaView.tecnica_list, name='tecnicas'),
    path('tecnicas/<str:pk>/', TecnicaView.tecnica_detail, name='tecnica_detail'),
    
    path('tecnicas-ataque/', TecnicaAtaqueView.tecnica_ataque_list, name='tecnicas-ataque'),
    path('tecnicas-ataque/<str:pk>/', TecnicaAtaqueView.tecnica_ataque_detail, name='tecnica-ataque_detail'),

    path('ninjas-medicos/', NinjaMedicoView.ninja_medico_list, name='ninjas-medicos'),
    path('ninjas-medicos/<str:pk>/', NinjaMedicoView.ninja_medico_detail, name='ninja-medico_detail'),
    
    path('tecnicas-curativas/', TecnicaCurativaView.tecnica_curativa_list, name='tecnicas-curativas'),
    path('tecnicas-curativas/<str:pk>/', TecnicaCurativaView.tecnica_curativa_detail, name='tecnica-curativa_detail'),
    
    path('ninjas-tecnicas/', NinjaTecnicaView.ninja_tecnica_list, name='ninjas-tecnicas'),
    path('ninjas-tecnicas/<str:pk>/', NinjaTecnicaView.ninja_tecnica_detail, name='ninja-tecnica_detail'),
    
    path('bestias-miticas/', BestiaMiticaView.bestia_mitica_list, name='bestias-miticas'),
    path('bestias-miticas/<str:pk>/', BestiaMiticaView.bestia_mitica_detail, name='bestia-mitica_detail'),
    
    path('equipos/', EquipoView.equipo_list, name='equipos'),
    path('equipos/<str:pk>/', EquipoView.equipo_detail, name='equipo_detail'),
    
    path('misiones/', MisionView.mision_list, name='misiones'),
    path('misiones/<str:pk>/', MisionView.mision_detail, name='mision_detail'),
    
    path('equipos-en-misiones/', EquipoEnMisionView.equipo_en_mision_list, name='equipos-en-misiones'),
    path('equipos-en-misiones/<str:pk>/', EquipoEnMisionView.equipo_en_mision_detail, name='equipo-en-mision_detail'),
    
    path('pergaminos/', PergaminoView.pergamino_list, name='pergaminos'),
    path('pergaminos/<str:pk>/', PergaminoView.pergamino_detail, name='pergamino_detail'),
    
    path('equipos-en-misiones-pergaminos/', EquipoEnMisionPergaminoView.equipo_en_mision_pergamino_list, name='equipos-en-misiones-pergaminos'),
    path('equipos-en-misiones-pergaminos/<str:pk>/', EquipoEnMisionPergaminoView.equipo_en_mision_pergamino_detail, name='equipo-en-mision-pergamino_detail'),
    
    path('bestias-misiones-pergaminos/', BestiaMisionPergaminoView.bestia_mision_pergamino_list, name='bestias-misiones-pergaminos'),
    path('bestias-misiones-pergaminos/<str:pk>/', BestiaMisionPergaminoView.bestia_mision_pergamino_detail, name='bestia-mision-pergamino_detail'),
]
    
