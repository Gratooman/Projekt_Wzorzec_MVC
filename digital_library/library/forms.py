from django import forms
from .models import Book
from django.core.exceptions import ValidationError

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "year", "category", "status"]
        labels = {
            "title": "Tytuł",
            "author": "Autor",
            "year": "Rok wydania",
            "category": "Kategoria",
            "status": "Status",
        }
        error_messages = {
        "title": {
            "required": "To pole jest wymagane.",
        },
        "author": {
            "required": "To pole jest wymagane.",
        },
        "year": {
            "required": "To pole jest wymagane.",
            "invalid": "Podaj poprawny rok.",
        },
        "category": {
            "required": "Wybierz kategorię.",
        },
        "status": {
            "required": "Wybierz status.",
        },
    }

    def clean_title(self):
        title = self.cleaned_data["title"]
        qs = Book.objects.filter(title__iexact=title)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise ValidationError("Książka o tym tytule już istnieje.")
        return title

    def clean_year(self):
        year = self.cleaned_data.get("year")
    
        if year is None:
            raise ValidationError("To pole jest wymagane")
        if year < 1:
            raise ValidationError("Rok musi być wiekszy od 0")
        if year > 9999:
            raise ValidationError("Rok nie może być większy niż 9999")
        return year
