from rest_framework import serializers
from . import models

class UsersSerializer(serializers.ModelSerializer):
    last_name = serializers.SerializerMethodField()

    class Meta:
        model = models.Users
        fields = ( 'id', 'username', 'last_name',)

    def last_name(self, obj):
        return obj.last_name
