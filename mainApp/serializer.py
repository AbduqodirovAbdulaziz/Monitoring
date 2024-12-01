from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *


class MevaTuriSerializer(ModelSerializer):
    class Meta:
        model = MevaTuri
        fields = "__all__"


class BogSerializer(ModelSerializer):
    class Meta:
        model = Bog
        fields = "__all__"


class XaridorSerializer(ModelSerializer):
    class Meta:
        model = Xaridor
        fields = "__all__"


class SotuvSerializer(ModelSerializer):
    class Meta:
        model = Sotuv
        fields = "__all__"


class XarajatlarSerializer(ModelSerializer):
    class Meta:
        model = Xarajatlar
        fields = "__all__"
