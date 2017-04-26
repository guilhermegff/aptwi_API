'''
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from catalog.models import Genre
from livros.serializers import GenreSerializer

#Primeira Versao
@csrf_exempt
def genre_list(request):
    if request.method == 'GET':
	genres = Genre.objects.all()
	serializer = GenreSerializer(genres, many=True)
	return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
	data = JSONParser().parse(request)
	serializer = GenreSerializer(data=data)
	if serializer.is_valid():
	    serializer.save()
	    return JsonResponse(serializer.data, status=201)
	return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def genre_detail(request, pk):
    try:
	genre = Genre.objects.get(pk=pk)
    except Genre.DoesNotExist:
	return HttpResponse(status=404)

    if request.method == 'GET':
	serializer = GenreSerializer(genre)
	return JsonResponse(serializer.data)

    elif request.method == 'PUT':
	data = JSONParser().parse(request)
	serializer = GenreSerializer(genre, data=data)
	if serializer.is_valid():
	    serializer.save()
	    return JsonResponse(serializer.data)
	return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
	genre.delete()
	return HttpResponse(status=204)
'''
'''
#Segunda Versao
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from catalog.models import Genre
from livros.serializers import GenreSerializer

@api_view(['GET', 'POST'])
def genre_list(request, format=None):
    if request.method == 'GET':
	genres = Genre.objects.all()
	serializer = GenreSerializer(genres, many=True)
	return Response(serializer.data)

    elif request.method == 'POST':
	serializer = GenreSerializer(data=request.data)
	if serializer.is_valid():
	    serializer.save()
	    return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def genre_detail(request, pk, format=None):
    try:
	genre = Genre.objects.get(pk=pk)
    except Genre.DoesNotExist:
	return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
	serializer = GenreSerializer(genre)
	return Response(serializer.data)

    elif request.method == 'PUT':
	serializer = GenreSerializer(genre, data=request.data)
	if serializer.is_valid():
	    serializer.save()
	    return Response(serializer.data)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
	genre.delete()
	return Response(status=status.HTTP_204_NO_CONTENT)
'''
#Terceira Versao
from aptwi.models import Genre
from aptwi.serializers import GenreSerializer
from rest_framework import generics

class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


















































