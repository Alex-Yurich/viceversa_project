from django.shortcuts import render


def home(request):
    # if request.method == 'POST':
    #     text = request#.GET['usertext']
    #     print(text)
    return render(request, 'home.html')


def rev(request):
    text = request.GET['usertext']
    print(text)
    return render(request, 'rev.html', {'cont': text[::-1]})
