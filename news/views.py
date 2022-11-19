from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import NewsSerializers
from .models import News
# Create your views here.

class NewsViewSets(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = News.objects.all()
    serializer_class = NewsSerializers

