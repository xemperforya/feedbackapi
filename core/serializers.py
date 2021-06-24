from rest_framework import fields, serializers
from core.models import feedback
from core.models import comments
from rest_framework.pagination import PageNumberPagination as pg

class feedbackserializer(serializers.ModelSerializer):

    class Meta:
        model = feedback
        fields = (
            'id',
            'email',
            'tag',
            'feed',
            'feed_time',
        )
    

class commentserializer(serializers.ModelSerializer):

    class Meta:
        model = comments
        fields = (
            'id',
            'feed_id',
            'comment',
            'comment_time'
        )
