from django.urls                    import path, include 
from django.contrib                 import admin
from django.conf.urls.static        import static
from django.conf                    import settings
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp                        import views

urlpatterns = [
    path('login/',                              TokenObtainPairView.as_view()),
    path('refresh/',                            TokenRefreshView.as_view()),
    path('user/',                               views.UserCreateView.as_view()),
    path('user/<int:pk>/',                      views.UserDetailView.as_view()),
    path('plan/',                               views.PlanCreateView.as_view()),
    path('plan/<int:user.id>/<int:pk>/',        views.PlanUserView.as_view()),
    path('plan/remove/<int:user>/<int:pk>/',    views.PlanDeleteView.as_view()),
    path('plan/update/<int:user>/<int:pk>/',    views.PlanUpdateView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,  document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)