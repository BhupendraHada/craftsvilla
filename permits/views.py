from django.shortcuts import render
from rest_framework import filters
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from .filters import FoodFacilityPermitsFilter
from .models import FoodFacilityPermits
from .serializers import FoodFacilityPermitsSerializer
# Create your views here.


class FoodFacilityPermitsListView(generics.ListCreateAPIView):
    queryset = FoodFacilityPermits.objects.all().order_by('-id')
    serializer_class = FoodFacilityPermitsSerializer
    authentication_classes = (TokenAuthentication, BasicAuthentication)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = FoodFacilityPermitsFilter


class FoodFacilityPermitsUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodFacilityPermits.objects.all().order_by('-id')
    serializer_class = FoodFacilityPermitsSerializer
    authentication_classes = (TokenAuthentication, BasicAuthentication)
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return super(FoodFacilityPermitsUpdateView, self).put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
