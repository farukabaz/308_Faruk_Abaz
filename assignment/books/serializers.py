from rest_framework import serializers

from books.models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    """Serializer for the book objects"""

    class Meta:
        model = Book
        fields = (
                'id', 'title', 'authors', 
                'publisher', 'publication_date',
                'number_of_pages'
        )
        read_only_fields = ('id',)

""" Create new model serializer AuthorSerializer that uses 
model User in Meta class, additionally add field books 
that is reverse relationship on the User model 
(serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())),
books field will not be included by default when using
model serializer so don’t forget to add an explicit 
field for it (in fields = (…))
 """

class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for the author objects"""

    books = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())

    class Meta:
        model = Author
        fields = (
                'id', 'name', 'username', 'books'
        )
        read_only_fields = ('id','books','username')