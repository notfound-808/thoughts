from django.shortcuts import render
from .models import thoughts

# Create your views here.
def main(request):
    thoughtspost = thoughts.objects.all()

    return render(request, 'engine/main.html', context={'thoughts' : thoughtspost})

def search(request):
    return render(request, 'engine/search.html', context={})
