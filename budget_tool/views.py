from django.shortcuts import render


def home_view(request):
    """
    Here we define our home view. 
    """
    return render(request, 'generic/home.html', {'message': 'I know you are a Book Lover!'})
