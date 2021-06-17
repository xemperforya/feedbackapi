from rest_framework import serializers
from core.models import feedback

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