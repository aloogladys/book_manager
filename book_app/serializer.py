from .models import Book 
from rest_framework import serializers
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_pulication_date(self,value):
        if value > date.today():
            raise serializers.ValidationError("Publication date cannot be in the future ")
        return value
    
    def validate_isbn_length(value):
        if  len(value)<10 or len(value) >13:
            raise serializers.ValidationError("ISBN must be 10 or 13 digits.")
        return value
