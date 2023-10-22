from rest_framework import serializers
from api.models import Book

class BookSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Book
        fields = "__all__"