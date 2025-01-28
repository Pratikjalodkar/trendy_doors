from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('test/', views.testEndPoint, name='test'),
    path('/', views.getRoutes),
    path('profile/update/', views.UpdateProfileView.as_view(), name='profile-update'),
    path('profile/view/', views.ViewProfileView.as_view(), name='profile-view'),

]