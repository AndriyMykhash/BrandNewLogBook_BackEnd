import jwt
from django.contrib.auth import user_logged_in
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_payload_handler

from brand_new_logbook_be import settings
from users.models import CustomUser
from rest_framework import viewsets, status
from rest_framework import permissions
from users.serializers import UserSerializer, SignUpUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['POST'])
@permission_classes([AllowAny])
def authenticate_user(request):
    try:
        email = request.data['email']
        password = request.data['password']

        user = CustomUser.objects.get(email=email, password=password)
        if user:
            try:
                payload = jwt_payload_handler(user)
                token = jwt.encode(payload, settings.SECRET_KEY)

                user_details = {}
                user_details['name'] = "%s %s" % (
                    user.first_name, user.last_name)
                user_details['token'] = token
                user_logged_in.send(sender=user.__class__,
                                    request=request, user=user)
                return Response(user_details, status=status.HTTP_200_OK)

            except Exception as e:
                raise e
        else:
            res = {
                'error': 'can not authenticate with the given credentials or the account has been deactivated'}
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    except KeyError:
        res = {'error': 'please provide a email and a password'}
        return Response(res)


@api_view(['POST'])
@permission_classes([AllowAny])
def create_auth(request):
    serialized = SignUpUserSerializer(data=request.POST)
    if serialized.is_valid():
        CustomUser.objects.create_user(email=serialized.data["email"],
                                       password=serialized.data["password"],
                                       name=serialized.data["name"],
                                       surname=serialized.data["surname"],
                                       type=serialized.data["type"])
        # CustomUser.objects.create_user(email=serialized.get_value("email"),
        #                                password=serialized.get_value("password"),
        #                                name=serialized.get_value("name"),
        #                                surname=serialized.get_value("surname"),
        #                                type=serialized.get_value("type"),)
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
