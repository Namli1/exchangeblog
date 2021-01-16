from django.urls import path

from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]

# Password reset urls
urlpatterns += [
    path('password-reset/', views.ReCaptchaPasswordResetView.as_view(), name="password_reset"),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]