# serializers 란 데이터 직렬화를 의미한다.
# 쉡게 말하면 DB에서 불러온 데이터를 json으로 보여주기 위해 가공하는 기능

from rest_framework.serializers import ModelSerializer
from .models import mariadb


class TestDataSerializer(ModelSerializer):
    class Meta:
        model = mariadb  # mariadb에 있는 models.py
        fields = '__all__'
