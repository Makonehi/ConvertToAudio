from django.shortcuts import render
from django.views.generic import ListView
from .models import Ads


# Create your views here.


def test(request):
    variables = {
            "boards": Ads.object.all()
        }
    return render(request, 'board/home_board.html', variables)







# class HomeAppBoard(ListView):
#     model = Ads
#     template_name = 'board/home_board.html'