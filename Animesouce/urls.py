from django.urls import path
from . import views


urlpatterns = [
    path('', views.creators, name='creators'),
    path('new/', views.new, name='new'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsUpdatelView.as_view(), name='news-update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete'),

]