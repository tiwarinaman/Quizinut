from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
                  path('', views.home_page, name="home"),
                  path('student-signup/', views.student_signup, name="studentSignUp"),
                  path('teacher-signup/', views.teacher_signup, name="teacherSignUp"),
                  path('student-login/', views.student_login, name="studentLogin"),
                  path('teacher-login/', views.teacher_login, name="teacherLogin"),
                  path('logout/', views.logout, name="logout"),
                  path('student-dashboard/', views.student_dashboard, name="studentDashboard"),
                  path('teacher-dashboard/', views.teacher_dashboard, name="teacherDashboard"),
                  path('new-quiz/', views.create_new_quiz, name="createNewQuiz"),
                  path('create-quiz-open-trivial/', views.create_quiz_by_open_trivial, name="createQuizOpenTrivial"),
                  path('view-quizzes/', views.view_quizzes, name="viewQuizzes"),
                  path('add-question/<int:quiz_id>/', views.add_question, name="addQuestion"),
                  path('delete-quiz/<int:quiz_id>/', views.delete_quiz, name="deleteQuiz"),
                  path('start-quiz/<int:quiz_id>/', views.start_quiz, name="startQuiz"),
                  path('get-questions/<int:quiz_id>/', views.get_questions, name="getQuestions"),
                  path('submit-quiz/', views.submit_quiz, name="submitQuiz"),
                  path('quiz-result/<int:quiz_id>', views.quiz_result, name="quizResult"),
                  path('all-quizzes-result', views.show_quizzes_results, name="showQuizzesResult"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
