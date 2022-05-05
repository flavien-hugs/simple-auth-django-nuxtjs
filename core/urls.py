# core.user.py

from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView
)

token_obtain_pair_view = TokenObtainPairView.as_view()
token_refresh_view = TokenRefreshView.as_view()


urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        route='api/v1/token/',
        view=token_obtain_pair_view,
        name='token_obtain_pair'
    ),
    path(
        route='api/v1/token/refresh/',
        view=token_refresh_view,
        name='token_refresh_view'
    ),
    path('api/v1/user/', include('user.urls', namespace='user'))
]
