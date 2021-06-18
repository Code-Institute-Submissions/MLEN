from django.shortcuts import render


def tutorial(request):
    """ A view to return the tutorial page """

    return render(request, 'tutorial/tutorial.html')
