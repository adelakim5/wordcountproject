from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    # split(여기에 쪼개고 샆은 거 쓰면 됨. ',' 쓰면 ',' 대로 쪼개줌/ 디폴트가 띄어쓰기라서 작동한 것.)
    word_dictionary = {} 
    # {} : 배열 

    for word in words:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    return render(request, 'result.html', {'full': text, 'total': len(words), 'dictionary': word_dictionary.items()})
    