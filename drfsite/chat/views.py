from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from .models import *
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import ClubSerializer



"""
class ClubViewSet(viewsets.ModelViewSet):

    serializer_class = ClubSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return Club.objects.all()[:3]

        return Club.objects.filter(pk = pk)

    @action(methods = ['get'], detail = True)
    def category(self, request, pk =None):
        cats = Category.objects.get(pk = pk)
        return Response({'cats' : cats.name})
"""

class ClubAPIList(generics.ListCreateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
class ClubAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)
class ClubAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    permission_classes = (IsAdminOrReadOnly,)

"""
class ClubAPIView(APIView):
    def get(self, request):
        lst = Club.objects.all()
        return Response({'clubs': ClubSerializer(lst,many= True).data})

    def post(self, request):
        serializer = ClubSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post' : serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method Put not allowed"})

        try:
            instance = Club.objects.get(pk= pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = ClubSerializer(data=request.data, instance = instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})
"""
# class ClubAPIView(generics.ListAPIView):
#   queryset = Club.objects.all()
#   serializer_class = ClubSerializer

