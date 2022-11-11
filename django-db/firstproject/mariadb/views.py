from django.shortcuts import render
from .models import Kosdak000440M


def post_view(request):

    result = Kosdak000440M.objects.all()
    # Kosdak000440M 테이블의 모든 객체를 불러와서 result변수에 저장

    return render(request, 'index.html', {"result": result})
# Create your views here.
