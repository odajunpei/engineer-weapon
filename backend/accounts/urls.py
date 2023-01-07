from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'accounts'
urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('account/', views.AccountUpdateView.as_view(), name='account'),
    path('accounts/', views.AccountListView.as_view(), name='account_list'),
    path('profile/<str:pk>/update',
         views.ProfileUpdateView.as_view(), name='profile'),
    path('profile/<str:pk>', views.ProfileDetailView.as_view(), name='profile_detail')
]
