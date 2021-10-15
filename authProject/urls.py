from django.urls                    import path
from django.contrib                 import admin
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp                        import views

urlpatterns = [
    path('login/',                              TokenObtainPairView.as_view()),
    path('refresh/',                            TokenRefreshView.as_view()),
    path('user/',                               views.UserCreateView.as_view()),
    path('user/<int:pk>/',                      views.UserDetailView.as_view()),
    path('plan/',                               views.PlanCreateView.as_view()),
    path('plan/<int:user>/<int:pk>/',           views.PlanUserView.as_view()),
    path('plan/remove/<int:user>/<int:pk>/',    views.PlanDeleteView.as_view()),
    path('plan/update/<int:user>/<int:pk>/',    views.PlanDeleteView.as_view()),
]