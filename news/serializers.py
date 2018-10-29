from rest_framework import serializers
from . import models

class NewsSerializer(serializers.ModelSerializer):

    class Meta:

        fields = ('url', 'id', 'title', 'news_texts', 'created_at', 'updated_at',)
        model = models.CatalogNews
