from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, redirect

from quiz.permission import *
from .models import Student, Teacher, Quiz, Question

User = get_user_model()


# View to render howe page

def home_page(request):
    if request.user.is_authenticated:
        if request.user.role == "student":
            return redirect('studentDashboard')
        elif request.user.role == "teacher":
            return redirect('teacherDashboard')
    else:
        return render(request, 'common/home.html')


def student_signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname', False)
        last_name = request.POST.get('lname', False)
        username = request.POST.get('uname', False)
        email = request.POST.get('email', False)
        passwd = request.POST.get('pass', False)
        cPasswd = request.POST.get('confirmPass', False)
        image = request.FILES.get('imageFile', False)

        if first_name == '' or last_name == '' or username == '' or email == '' or passwd == '' \
                or cPasswd == '' or image == '':
            messages.error(request, "All fields are required")
            return redirect("studentSignUp")
        else:
            if passwd != cPasswd:
                messages.error(request, "Password must be matched")
                return redirect("studentSignUp")
            elif not image:
                messages.error(request, "Please upload your image")
                return redirect('studentSignUp')
            elif User.objects.filter(username=username).exists():
                messages.warning(request, "Username Already In Use !!!")
                return redirect('studentSignUp')
            elif User.objects.filter(email=email).exists():
                messages.warning(request, "Email Already In Use !!!")
                return redirect('studentSignUp')
            else:
                user = User.objects.create(first_name=first_name, last_name=last_name,
                                           username=username, email=email, role="student")
                user.set_password(passwd)
                student = Student.objects.create(uname=user, student_image=image)
                user.save()
                student.save()

                messages.success(request, "Thank you for registering with us")
                return redirect('teacherSignUp')

    return render(request, 'student/student_signup.html')


def teacher_signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname', False)
        last_name = request.POST.get('lname', False)
        username = request.POST.get('uname', False)
        email = request.POST.get('email', False)
        passwd = request.POST.get('pass', False)
        cPasswd = request.POST.get('confirmPass', False)
        image = request.FILES.get('imageFile', False)

        if first_name == '' or last_name == '' or username == '' or email == '' or passwd == '' \
                or cPasswd == '' or image == '':
            messages.error(request, "All fields are required")
            return redirect("studentSignUp")
        else:
            if passwd != cPasswd:
                messages.error(request, "Password must be matched")
                return redirect("studentSignUp")
            elif not image:
                messages.error(request, "Please upload your image")
                return redirect('studentSignUp')
            elif User.objects.filter(username=username).exists():
                messages.warning(request, "Username Already In Use !!!")
                return redirect('studentSignUp')
            elif User.objects.filter(email=email).exists():
                messages.warning(request, "Email Already In Use !!!")
                return redirect('studentSignUp')
            else:
                user = User.objects.create(first_name=first_name, last_name=last_name,
                                           username=username, email=email, role="teacher")
                user.set_password(passwd)
                teacher = Teacher.objects.create(uname=user, teacher_image=image)
                user.save()
                teacher.save()

                messages.success(request, "Thank you for registering with us")
                return redirect('teacherSignUp')
    return render(request, 'teacher/teacher_signup.html')


def student_login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname', False)
        passwd = request.POST.get('passwd', False)

        if uname == '' or passwd == '':
            messages.info(request, "All Fields are required !!!")
            return redirect('studentLogin')
        elif not User.objects.filter(username=uname).exists():
            messages.error(request, "User doesn't exists !!!")
            return redirect('studentLogin')
        else:
            user = auth.authenticate(username=uname, password=passwd)
            if user:
                try:
                    if user.role == "student":
                        auth.login(request, user)
                        return redirect('studentDashboard')
                    else:
                        messages.warning(request, "Not a student, please try with another credentials !!!")
                        return redirect('studentLogin')
                except:
                    messages.error(request, "Something went wrong !!!")
                    return redirect('studentLogin')
            else:
                messages.error(request, "Invalid credentials, please try again !!!")
                return redirect('studentLogin')

    return render(request, 'student/student_login.html')


def teacher_login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname', False)
        passwd = request.POST.get('passwd', False)

        if uname == '' or passwd == '':
            messages.info(request, "All Fields are required !!!")
            return redirect('teacherLogin')
        elif not User.objects.filter(username=uname).exists():
            messages.error(request, "User doesn't exists !!!")
            return redirect('teacherLogin')
        else:
            user = auth.authenticate(username=uname, password=passwd)
            if user:
                try:
                    if user.role == "teacher":
                        auth.login(request, user)
                        return redirect('teacherDashboard')
                    else:
                        messages.warning(request, "Not a teacher, please try with another credentials !!!")
                        return redirect('teacherLogin')
                except:
                    messages.error(request, "Something went wrong !!!")
                    return redirect('teacherLogin')
            else:
                messages.error(request, "Invalid credentials, please try again !!!")
                return redirect('teacherLogin')
    return render(request, 'teacher/teacher_login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


@login_required(login_url='/student-login')
@user_is_student
def student_dashboard(request):
    quizzes = Quiz.objects.all()
    context = {
        'quizzes': quizzes
    }
    return render(request, 'student/student_dashboard.html', context)


@login_required(login_url='/teacher-login')
@user_is_teacher
def teacher_dashboard(request):
    return render(request, 'teacher/teacher_dashboard.html')


@login_required(login_url='/teacher-login')
@user_is_teacher
def create_new_quiz(request):
    if request.method == 'POST':
        quiz_name = request.POST.get('quiz_name', False)
        total_questions = request.POST.get('total_questions', False)
        total_marks = request.POST.get('total_marks', False)
        time_duration = request.POST.get('time_duration', False)

        if quiz_name == '' or total_questions == '' or total_marks == '' or time_duration == '':
            messages.error(request, "Please fill all the details")
            return redirect('createNewQuiz')
        else:
            try:
                teacher = Teacher.objects.get(uname=request.user)
                quiz = Quiz.objects.create(teacher=teacher, quiz_name=quiz_name, total_question=total_questions,
                                           added_question=0, total_marks=total_marks, time_duration=time_duration)
                quiz.save()
                messages.success(request, "Quiz created successfully")
                return redirect('viewQuizzes')
            except Exception as e:
                messages.error(request, f"Something went wrong {e}")
                return redirect('createNewQuiz')

    return render(request, 'teacher/create_new_quiz.html')


@login_required(login_url='/teacher-login')
@user_is_teacher
def view_quizzes(request):
    quizzes = Quiz.objects.all().order_by('-timestamp')
    context = {
        'quizzes': quizzes
    }
    return render(request, 'teacher/view_quizzes.html', context)


@login_required(login_url='/teacher-login')
@user_is_teacher
def add_question(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    if request.method == 'POST':
        question = request.POST.get('question', False)
        marks = request.POST.get('marks', False)
        option1 = request.POST.get('option1', False)
        option2 = request.POST.get('option2', False)
        option3 = request.POST.get('option3', False)
        option4 = request.POST.get('option4', False)
        correct_answer = request.POST.get('correct_answer', False)

        if question == '' or marks == '' or option1 == '' or option2 == '' \
                or option3 == '' or option4 == '' or correct_answer == '':
            messages.error(request, "Please fill all the fields")
            return redirect('addQuestion', quiz_id)
        elif correct_answer == '-':
            messages.error(request, "Please provide the correct answer")
            return redirect('addQuestion', quiz_id)
        else:
            try:
                teacher = Teacher.objects.get(uname=request.user)
                add = Question.objects.create(quiz=quiz, teacher=teacher, question=question, marks=marks,
                                              option1=option1, option2=option2, option3=option3,
                                              option4=option4, correct_answer=correct_answer)
                add.save()
                quiz.added_question += 1
                quiz.save()
                remaining_questions = quiz.total_question - quiz.added_question
                messages.success(request, f"Question added successfully. {remaining_questions} more left.")
                return redirect('addQuestion', quiz_id)
            except Exception as e:
                messages.error(request, e)
                return redirect('addQuestion', quiz_id)

    context = {
        'quiz': quiz
    }
    return render(request, 'teacher/add_question.html', context)


@login_required(login_url='/teacher-login')
@user_is_teacher
def delete_quiz(request, quiz_id):
    try:
        quiz = Quiz.objects.get(id=quiz_id)
        quiz.delete()
        messages.success(request, "Quiz successfully deleted")
        return redirect('viewQuizzes')
    except Exception as e:
        messages.error(request, "Something went wrong")
        return redirect('viewQuizzes')


@login_required(login_url='/student-login')
@user_is_student
def quiz_info(request, quiz_id):
    quiz_detail = Quiz.objects.get(id=quiz_id)

    context = {
        'quiz_detail': quiz_detail
    }
    return render(request, 'student/quiz_info.html', context)


@login_required(login_url='/student-login')
@user_is_student
def start_quiz(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = Question.objects.filter(quiz=quiz)

    paginator = Paginator(questions, 1)

    try:
        page = request.GET.get('page', 1)
    except:
        page = 1

    try:
        questions = paginator.page(page)
    except(EmptyPage, InvalidPage):
        questions = paginator.page(paginator.num_pages)

    context = {
        'questions': questions
    }
    return render(request, 'student/start_quiz.html', context)
