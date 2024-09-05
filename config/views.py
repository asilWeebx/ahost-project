from django.shortcuts import render
def logout_view(request):
    return render(request, 'home.html')