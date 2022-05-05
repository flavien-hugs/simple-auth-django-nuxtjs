# user.views.py

from django.shortcuts import render
from django.contrib.auth import get_user_model

import requests
from rest_framework.decorators import api_view
from rest_framework import(
    generics, exceptions, response,
    reverse, viewsets
)
from rest_framework.permissions import IsAuthenticated, AllowAny

from user.serializers import UserRegisterSerializer, UserSerializer


user_model = get_user_model()


class UserRegisterView(generics.CreateAPIView):
    queryset = user_model.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer


user_register_view = UserRegisterView.as_view()


@api_view(['POST'])
def userLoginView(request):
    phone = request.data.get('phone')
    password = request.data.get('password')

    user = user_model.objects.filter(phone=phone).first()
    if user is None:
        raise exceptions.AuthenticationFailed(
            'User not found !')

    if not user.check_password(password):
        raise exceptions.AuthenticationFailed(
            'Incorrect Password !')

    response_obj = response.Response()
    token_endpoint = reverse.reverse(
        viewname='token_obtain_pair',
        request=request
    )
    tokens = requests.post(
        token_endpoint,
        data=request.data
    ).json()

    response_obj.data = {
        'access_token': tokens.get('access'),
        'refresh_token': tokens.get('refresh'),
        'phone': user.phone
    }

    return response_obj


user_login_view = userLoginView


class UserListView(generics.ListAPIView):
    queryset = user_model.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer


user_list_view = UserListView.as_view()


class CurrentLoggedInUser(viewsets.ModelViewSet):
    queryset = user_model.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        user_profile = self.queryset.get(phone=request.user.phone)
        serializer = self.get_serializer(user_profile)
        return response.Response({'user': serializer.data})


current_loggedin_user = CurrentLoggedInUser.as_view({'get': 'retrieve'})
