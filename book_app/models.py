from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
from datetime import date

def validate_publication_date(value):
    if value > date.today():
        raise ValidationError("Publication date cannot be in the future ")

class Book(models.Model):
    title = models.CharField(max_length = 255)
    author =  models.CharField(max_length = 255)
    publication_date = models.DateField(validators = [validate_publication_date])
    isbn  = models.CharField(max_length=13, unique=True, validators=[MinLengthValidator(10), MaxLengthValidator(13)])
    summary = models.TextField()

    def __str__(self):
        return self.title