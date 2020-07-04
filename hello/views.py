from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

#요청이 들어왔을 때 home.html 파일을 렌더링해서 화면에 띄워준다!