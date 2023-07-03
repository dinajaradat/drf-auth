from django.shortcuts import render
from rest_framework import generics
from .models import Recipe 
from .serializers import RecipeSerializer

# Create your views here.
class Recipe_list(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class Recipe_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer