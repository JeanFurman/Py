# from rest_framework.decorators import api_view
# from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
# from rest_framework.response import Response
# from rest_framework.views import APIView
from .serializers import LivrosSerializer
#
from .models import Livro
#
#
# class LivrosApiView(ListAPIView):
#     queryset = Livro.objects.all()
#     serializer_class = LivrosSerializer
#
#
# class LivroCreateView(CreateAPIView):
#     queryset = Livro.objects.all()
#     serializer_class = LivrosSerializer
#
#
# class LivroUpdateView(UpdateAPIView):
#     queryset = Livro.objects.all().select_related('categoria')
#     serializer_class = LivrosSerializer
#
#
# # @api_view(['GET', 'POST'])
#
#
# livros_view = LivrosApiView.as_view()
# livros_create_view = LivroCreateView.as_view()
# livros_update_view = LivroUpdateView.as_view()
#
#
from rest_framework import viewsets


class LivrosViewSet(viewsets.ModelViewSet):
    serializer_class = LivrosSerializer
    queryset = Livro.objects.all()
