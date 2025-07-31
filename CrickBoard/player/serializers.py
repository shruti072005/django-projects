from rest_framework import serializers
from .models import player

class playerSerializer(serializers.ModelSerializer):
    class Meta:
        model = player
        #fields = '__all__'
        fields = ['jn', 'name', 'runs','wickets', 'teamname']
