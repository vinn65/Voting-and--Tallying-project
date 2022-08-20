from django.urls import path
from . import views

app_name = "base"
urlpatterns = [
    path('',views.home),
    path('base/',views.index,name='index'),
    path('<int:id>/',views.detail,name="details"),
    path('<int:id>/results/',views.results,name="results"),
    path('<int:id>/vote/',views.vote,name="vote"),
]