from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostListApiView.as_view()),
    # path('api-delete/<int:pk>/', views.PostDeleteApiView.as_view()),
    # path('api-update/<int:pk>/', views.PostUpdateApiView.as_view()),
    path('<int:pk>/', views.PostRetrieveApiView.as_view()),
    path('common-api/<int:pk>/', views.PostCommonApiView.as_view()),

]