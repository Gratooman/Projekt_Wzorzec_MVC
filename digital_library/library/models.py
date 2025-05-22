from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

CATEGORY_CHOICES = [
    ("Fantasy", "Fantasy"),
    ("Science Fiction", "Science Fiction"),
    ("Mystery", "Kryminał"),
    ("Thriller", "Thriller"),
    ("Romance", "Romans"),
    ("Historical", "Historyczna"),
    ("Non-fiction", "Literatura faktu"),
    ("Horror", "Horror"),
    ("Biography", "Biografia"),
    ("Adventure", "Przygodowa"),
]

STATUS_CHOICES = [
    ("read", "Przeczytana"),
    ("unread", "Nieprzeczytana"),
]

class Book(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100)
    year = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(9999)])
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="unread")

    def __str__(self):
        return f"{self.title} ({self.author})"