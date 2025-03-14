from rest_framework import serializers
from . models import BookStoreModel

class BookStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookStoreModel
        fields = '__all__'

"""
How Serializers work?
Frontend ---------> JSON ---------> Database
        serializer          API         |
                                        |
                                    response
                                        |
Frontend <--- Deserialize <---JSON  <--- API

"""
