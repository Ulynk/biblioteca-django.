from rest_framework import serializers
from .models import Categoria, Autor, Livro
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from .models import Livro
from .serializers import LivroSerializer

class CategoriaSerializer(serializers.Serializer):
 id = serializers.IntegerField(read_only=True)
 nome = serializers.CharField(max_length=100)

def create(self, validated_data):
 return Categoria.objects.create(**validated_data)

def update(self, instance, validated_data):
 instance.nome = validated_data.get('nome', instance.nome)
 instance.save()
 return instance

class AutorSerializer(serializers.Serializer):
 id = serializers.IntegerField(read_only=True)
 nome = serializers.CharField(max_length=100)

def create(self, validated_data):
 return Autor.objects.create(**validated_data)

def update(self, instance, validated_data):
 instance.nome = validated_data.get('nome', instance.nome)
 instance.save()
 return instance

class LivroSerializer(serializers.Serializer):
 id = serializers.IntegerField(read_only=True)
 titulo = serializers.CharField(max_length=200)
 autor = serializers.PrimaryKeyRelatedField(queryset=Autor.objects.all())
 categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())
 publicado_em = serializers.DateField()

def create(self, validated_data):
 return Livro.objects.create(**validated_data)

def update(self, instance, validated_data):
 instance.titulo = validated_data.get('titulo', instance.titulo)
 instance.autor = validated_data.get('autor', instance.autor)
 instance.categoria = validated_data.get('categoria',
 instance.categoria)
 instance.publicado_em = validated_data.get('publicado_em',
 instance.publicado_em)
 instance.save()
 return instance

@api_view(['GET', 'POST'])
@csrf_exempt
def livro_list_create(request):
    if request.method == 'GET':
        livros = Livro.objects.all()
        serializer = LivroSerializer(livros, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = LivroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def livro_detail(request, pk):
    try:
        livro = Livro.objects.get(pk=pk)
    except Livro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LivroSerializer(livro)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = LivroSerializer(livro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        livro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
