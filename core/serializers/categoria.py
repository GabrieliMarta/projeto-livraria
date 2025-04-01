from attrs import field
from pydantic import model_serializer
from rest_framework.serializers import ModelSerializer
from core.models import Categoria

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"