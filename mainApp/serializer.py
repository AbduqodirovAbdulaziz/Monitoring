from rest_framework.serializers import ModelSerializer
from .models import *


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
