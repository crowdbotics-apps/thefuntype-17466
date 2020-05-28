from rest_framework import authentication
from dating.models import Dislike, Inbox, Like, Match, Profile, Setting, UserPhoto
from .serializers import (
    DislikeSerializer,
    InboxSerializer,
    LikeSerializer,
    MatchSerializer,
    ProfileSerializer,
    SettingSerializer,
    UserPhotoSerializer,
)
from rest_framework import viewsets


class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Like.objects.all()


class UserPhotoViewSet(viewsets.ModelViewSet):
    serializer_class = UserPhotoSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = UserPhoto.objects.all()


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Profile.objects.all()


class SettingViewSet(viewsets.ModelViewSet):
    serializer_class = SettingSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Setting.objects.all()


class DislikeViewSet(viewsets.ModelViewSet):
    serializer_class = DislikeSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Dislike.objects.all()


class MatchViewSet(viewsets.ModelViewSet):
    serializer_class = MatchSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Match.objects.all()


class InboxViewSet(viewsets.ModelViewSet):
    serializer_class = InboxSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Inbox.objects.all()
