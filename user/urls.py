# user.urls.py

from django.urls import path

from user import views

app_name='user'
urlpatterns = [
    path(
        route='',
        view=views.current_loggedin_user,
        name='current_user'
    ),
    path(
        route='register/',
        view=views.user_register_view,
        name='register'
    ),
    path(
        route='login/',
        view=views.user_login_view,
        name='login'
    ),
    path(
        route='list/',
        view=views.user_list_view,
        name='all'
    )
]
