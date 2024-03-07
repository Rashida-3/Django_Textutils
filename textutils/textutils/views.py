# i have created this file -Rashida
from django.http import HttpResponse

from django.shortcuts import render

# code for video 6
# def index(request):
#     return HttpResponse('''<h1>hello Rashida</h1> <a href='https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7'> Django Code with Rashida</a>''')

# def about(request):
#     return HttpResponse('about hello Rashida')

# code for video 7

def index(request):
    # params={'name':'Rashida','place':'mumbai'}
    return render(request,'index.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    # print(djtext)

    # check checkbox values
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')

    # check which checkbox is on


    # print(djtext)
    if removepunc=='on':
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char

        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        # return render(request,'analyze.html',params)
        djtext=analyzed

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed=analyzed+char.upper()

        params={'purpose':'Changed to Uppercase','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)
    if(extraspaceremover=='on'):
        analyzed=""
        for index, char in enumerate (djtext):
            if not (djtext[index] == " " and djtext[index+1]==" "):
               analyzed=analyzed+char

        params={'purpose':'Removed NewLines','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)
    
    if(newlineremover=='on'):
        analyzed=""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed=analyzed+char
        #     else:
        #         print('no')
        # print('pre',analyzed)    
        params={'purpose':'Removed NewLines','analyzed_text':analyzed}
        # print(params)
    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)
  
 
# def capfirst(request):
#     return HttpResponse('capitalize first')

# def newlineremove(request):
#     return HttpResponse('newline remove')

# def spaceremove(request):
#     return HttpResponse('space remove')

# def charcount(request):
#     return HttpResponse('charcount')
