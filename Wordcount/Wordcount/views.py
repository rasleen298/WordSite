from django.http import HttpResponse
from django.shortcuts import render
import operator
from nltk.corpus import stopwords



def home(request):
    return render(request,"home.html")
def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['Text']
    print(fulltext)
    words = fulltext.split()
    worddictionary = {}

    for word in words:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    Sortedwords= sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)


    mydict = {"fulltext": fulltext, "count": len(words),"Sortedwords":Sortedwords}
    return render(request, "count.html", mydict)






