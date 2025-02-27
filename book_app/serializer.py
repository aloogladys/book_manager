from .models import Book 
from rest_framework import serializers
from datetime import date

class BookSerializer(serializers.ModelSerilaizer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_pulication_date(self,value):
        if value > date.today():
            raise serializers.ValidationError("Publication date cannot be in the future ")
        return value
    
