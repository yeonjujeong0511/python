from .serializer import TestDataSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import mariadb


@api_view(['GET'])
def getTestDatas(request):
    datas = mariadb.object.all()
    serializer = TestDataSerializer(datas, many=True)
    return Response(serializer.data)

  # 앞서만든 serializers를 불어온다.
  #  @api_view는 데코레이션을 의미하며, get 메소드를 사용하는 것을 볼 수 있다.
  #  mariadb.object.all() mariadb에 있는 테이블에 있는 모든 데이터를 모두 읽어들이겠다.

  # 이렇게 데이터를 읽어오고, serializer를 이용해 데이터 직렬화를 통해 마지막으로 response를 이용해 결과를 보여준다.

# Create your views here.
