from rest_framework import serializers
from . import models

class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'news_texts',)
        model = models.CatalogNews
