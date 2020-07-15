from django.urls import path 
from . import views

# app_name = 'polls'

urlpatterns = [   
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/reset/', views.reset, name='reset'), 
    path('ajax1',views.ajax1,name='ajax'),
    path('ajax2',views.ajax2,name='ajax2'),
    path('ajax3',views.ajax3,name='ajax3'),
]