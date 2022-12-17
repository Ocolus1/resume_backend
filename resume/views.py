from django.shortcuts import render



def toronto(request):
    content = { }
    return render(request, "resume/toronto.html", content)

