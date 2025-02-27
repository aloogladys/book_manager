from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

def validate_publication_date(value):
    if value > date.today():
        raise ValidationError("Publication date cannot be in the future ")
    
def validate_isbn_length(value):
    if  len(value)<10 or len(value) >13:
        raise ValidationError("ISBN must be 10 or 13 digits.")

class Book(models.Model):
    title = models.CharField(max_length = 255)
    author =  models.CharField(max_length = 255)
    publication_date = models.DateField(validators = [validate_publication_date])
    isbn  = models.CharField(max_length=13, unique=True, validators=[validate_isbn_length])
    summary = models.TextField()

    def __str__(self):
        return self.title