#i have created this file - tejas

from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter


def index(request):
    #return HttpResponse("Home")
     #params = {'name':'Tejas', 'place':'Pune'}
     return render(request, 'index.html')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'off')

    #check checkbox values
    djrmvpunc = request.POST.get('removepunc', 'off')
    djfullcaps = request.POST.get('fullcaps', 'off')
    djnewlinermr = request.POST.get('newlineremover', "off")
    extraspacecrm = request.POST.get('extraspaceremover', "off")
    djcharcounter = request.POST.get('charcounter', "off")

    if djrmvpunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        #return render(request, 'analyze.html', params)

    if(djfullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Change to UPPERCASE', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        #return render(request, 'analyze.html', params)

    if(djnewlinermr == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
             analyzed = analyzed + char

        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        #return render(request, 'analyze.html', params)


    if (extraspacecrm == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed Extra Space', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        #return render(request, 'analyze.html', params)

    if (djcharcounter == "on"):
        analyzed = Counter(djtext)
        params = {'purpose': 'Removed Extra Space', 'analyzed_text': analyzed}

    if(djrmvpunc != "on" and djfullcaps != "on" and djnewlinermr != "on" and extraspacecrm != "on" and djcharcounter != "on"):
        return HttpResponse("Please select the operation which wants to perform on the given text")


    return render(request, 'analyze.html', params)



