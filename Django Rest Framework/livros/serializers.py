from rest_framework import serializers
from .models import Livro, Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        modal = Categoria
        fields = '__all__'


class LivrosSerializer(serializers.ModelSerializer):
    disponivel = serializers.ReadOnlyField()

    class Meta:
        model = Livro
        exclude = ['em_estoque']

