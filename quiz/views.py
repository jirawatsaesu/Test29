from django.shortcuts import render
from quiz.models import Quiz

# Create your views here.
def home_page(request):
    return render(request, 'home.html')


def quiz_page(request):
    if request.method == 'POST':
        ques = request.POST.get('quiz')
        ans = request.POST.get('answer')
        Quiz(question=ques, answer=ans).save()
    return render(request, 'quiz.html')


def answer_page(request):
    return render(request, 'answer.html')
