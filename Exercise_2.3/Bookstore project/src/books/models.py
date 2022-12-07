from django.db import models

# Create your models here.
class Book(models.Model):
  name = models.CharField(max_length=120)
  genre_choices = (
    ('classic',
    'Classic'),
    ('romantic',
    'Romantic'),
    ('comic',
    'Comic'),
    ('fantasy',
    'Fantasy'),
    ('horror',
    'Horror'),
    ('educational',
    'Educational')
    )

  genre = models.CharField(max_length=12, choices=genre_choices, default='classic')

  book_type_choices = (('hardcover','Hard cover'),('ebook','E-Book'),('audiob','Audiobook'))

  book_type = models.CharField(max_length=12, choices=book_type_choices, default='hardcopy')

  price = models.FloatField(help_text= 'in US dollars $')

  author_name = models.CharField(max_length=120)

  def __str__(self):
    return str(self.name)