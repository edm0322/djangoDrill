from django.shortcuts import render
from burgers.models import Burger

def main(request):
    return render(request, "main.html")
    #return HttpResponse("Hi")


def burger_list(request):
    burgers = Burger.objects.all()
    print("전체 햄버거 목록", burgers)

    # Template를 이용하기 위해선 context Dict Type을 이용한다.
    context = {
        "burgers": burgers,
    }
    return render(request, "burger_list.html", context)
    #return HttpResponse("햄버거몇개")

def burger_search(request):
    keyword = request.GET.get("keyword")

    if keyword is not None:
        burgers = Burger.objects.filter(name__contains=keyword)
    else:
        burgers = Burger.objects.none() #Keyword가 없을 경우 None 처리로 안전하게 API 처리

    context = {
        "burgers": burgers
    }

    return render(request, "burger_search.html", context)