from django.shortcuts import render



def toronto(request):
    content = { }
    return render(request, "resume/toronto.html", content)

def toronto_test(request):
    content = { }
    return render(request, "resume/wu.html", content)

