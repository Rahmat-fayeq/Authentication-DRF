from django.urls import path,include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

router = routers.SimpleRouter()
router.register('api/register', views.RegisterViewSets, basename='register')

urlpatterns = [
    path('api/', views.showRoutes),
    path('api/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/password-forgot/', views.ForgotPasswordAPIView.as_view(), name='forgot'),
    path('api/password-reset/', views.ResetPasswordView, name='reset'),
    path('', include(router.urls)),
    path('api/user/reset-password/<int:id>', views.PasswordResetView, name='user.reset')
]