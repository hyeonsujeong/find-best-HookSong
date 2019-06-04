from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")
        
def about(request):
    return render(request, "about.html")

def result(request):
    title = request.GET['title']
    full_text = request.GET['fulltext']
    word_list = full_text.split()
    word_dic = {}
    for word in word_list :
        if word in word_dic : 
            word_dic[word] += 1
        else : 
            word_dic[word] = 1
    import operator
    sort = sorted(word_dic.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'result.html', 
        {'top_word' : sort[0][0], 'top_val' : sort[0][1], 'title' : title})
