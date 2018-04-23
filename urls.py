from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('questions', views.questions, name='questions'),
    path('detail/<int:question_id>',views.detail,name='detail'),
    path('vote/<int:question_id>', views.vote, name='vote'),
]