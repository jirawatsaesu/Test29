from django.shortcuts import redirect, render
from quiz.models import Quiz

# Create your views here.
def home_page(request):
    return render(request, 'home.html')


def quiz_page(request):
    if request.method == 'POST':
        ques = request.POST.get('quiz')
        ans = request.POST.get('answer')
        Quiz(question=ques, answer=ans).save()
        return redirect('/quiz/')
    return render(request, 'quiz.html')


def answer_page(request):
    if request.method == 'POST':
        quiz_id = request.POST.get('quiz_id')
        ans = request.POST.get('answer')
        current_quiz = Quiz.objects.get(id=quiz_id)

        # Point Collected
        if ans == str(current_quiz.answer):
            current_quiz.correct_ans += 1
        else:
            current_quiz.wrong_ans += 1
        current_quiz.save()

        return redirect('/answer/')

    # Show all questions
    questions = Quiz.objects.all()
    return render(request, 'answer.html', { 'questions': questions })


def result_page(request):
    questions = Quiz.objects.all()
    return render(request, 'result.html', { 'questions': questions })
