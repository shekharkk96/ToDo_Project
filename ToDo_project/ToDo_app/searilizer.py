from rest_framework import serializers
from ToDo_app.models import List

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model= List
        #fields = ['title','date']
        fields = '__all__'
