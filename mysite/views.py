from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def analyze(request):
    djtext = request.POST.get("text", "default")

    removepunc = request.POST.get("removepunc", "off")

    allcaps = request.POST.get("allcaps", "off")

    newlineremover = request.POST.get("newlineremover", "off")

    extraspaceremover = request.POST.get("extraspaceremover", "off")

    if removepunc == "on":
        analyzed = removepunct(djtext)
        params = {"purpose": "Removing Punctuations", "analyzed_text": analyzed}
        djtext = analyzed
       

    if allcaps == "on":
        analyzed = allcap(djtext)
        params = {"purpose": "Changed to uppercase", "analyzed_text": analyzed}
        djtext = analyzed
       
    if extraspaceremover == "on":
        analyzed = extraspaceremove(djtext)
        params = {"purpose": "Removed ExtraSpaces", "analyzed_text": analyzed}
        djtext = analyzed
        
    if newlineremover == "on":
        analyzed = newlineremove(djtext)
        params = {"purpose": "Removed ExtraLines", "analyzed_text": analyzed}
        djtext = analyzed

    if (
        newlineremover != "on"
        and extraspaceremover != "on"
        and allcaps != "on"
        and removepunc != "on"
    ):
        return HttpResponse("Error")
    
    return render(request, "analyze.html", params)


def removepunct(djtext):
    punctuations = """!()-[]{};:'"\,<>./?@#$%^&*_~"""
    analyzed = ""
    for char in djtext:
        if char not in punctuations:
            analyzed = analyzed + char
    return analyzed


def allcap(djtext):
    analyzed = ""
    for char in djtext:
        analyzed = analyzed + char.upper()
    return analyzed


def newlineremove(djtext):
    analyzed = ""
    for char in djtext:
        if char != "\n" and char != "\r":
            analyzed = analyzed + char
    return analyzed


def extraspaceremove(djtext):
    analyzed = ""
    for index, char in enumerate(djtext):
        if not (djtext[index] == " " and djtext[index + 1] == " "):
            analyzed = analyzed + char
    return analyzed
