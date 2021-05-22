from django.db import models

class Author(models.Model):
    username = models.CharField(max_length=25)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Book(models.Model):
    
    title = models.CharField(max_length=25)
    #authors = models.CharField(max_length=100)
    authors = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)
    publisher = models.CharField(max_length=25)
    publication_date = models.DateTimeField('publication date')
    number_of_pages = models.IntegerField()

    def __str__(self):
        return self.title
