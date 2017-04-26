from rest_framework import serializers
from aptwi.models import Genre
'''
class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)

    def create(self, validated_data):
	return Genre.objects.create(**validated_data)

    def update(self, instance, validated_data):
	instance.name = validated_data.get('name', instance.name)
	return instance
'''

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
	model = Genre
	fields = ('id', 'name')
