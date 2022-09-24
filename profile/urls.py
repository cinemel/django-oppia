from django.contrib.auth import views as django_contrib_auth_views
from django.urls import path
from django.views import i18n as django_views_i18n
from django.views.generic import TemplateView

from profile import views as profile_views

app_name = 'profile'

urlpatterns = [
    path('register/', profile_views.RegisterView.as_view(), name="register"),
    path('register/thanks/', TemplateView.as_view(template_name="oppia/thanks.html"), name="register_thanks"),
    path('login/', profile_views.LoginView.as_view(), name="login"),
    path('logout/',
         django_contrib_auth_views.LogoutView.as_view(),
         {'template_name': 'oppia/logout.html', },
         name="logout"),
    path('setlang/', django_views_i18n.set_language, name="set_language"),

    path('edit/', profile_views.EditView.as_view(), name="edit"),
    path('edit/<int:user_id>/', profile_views.EditView.as_view(), name="edit_user"),

    path('points/', profile_views.PointsView.as_view(), name="points"),
    path('badges/', profile_views.BadgesView.as_view(), name="badges"),

    path('<int:user_id>/activity/', profile_views.UserScorecard.as_view(), name="user_activity"),
    path('<int:user_id>/activity/detail/',
         profile_views.UserActivityDetailList.as_view(),
         name="user_activity_detail"),
    path('<int:user_id>/<int:course_id>/activity/',
         profile_views.UserCourseScorecard.as_view(),
         name="user_course_activity"),
    path('<int:user_id>/quizattempts/', profile_views.UserAttemptsList.as_view(), name="user_all_attempts"),
    path('<int:user_id>/<int:course_id>/quiz/<int:quiz_id>/attempts/',
         profile_views.QuizAttemptsList.as_view(),
         name="user_quiz_attempts"),
    path('<int:user_id>/<int:course_id>/quiz/<int:quiz_id>/attempts/<int:pk>',
         profile_views.QuizAttemptDetail.as_view(),
         name="quiz_attempt_detail"),
    path('<int:user_id>/feedback/',
         profile_views.UserFeedbackResponsesList.as_view(),
         name="user_all_feedback_responses"),
    path('<int:user_id>/regeneratecertificates/',
         profile_views.RegenerateCertificatesView.as_view(),
         name="user_regenerate_certificates"),
    path('<int:user_id>/regeneratecertificates/success/',
         TemplateView.as_view(template_name="profile/certificates/success.html"),
         name="user_regenerate_certificates_success"),

    path('regeneratecertificates/',
         profile_views.RegenerateCertificatesView.as_view(),
         name="user_regenerate_certificates"),
    path('regeneratecertificates/success/',
         TemplateView.as_view(template_name="profile/certificates/success.html"),
         name="user_regenerate_certificates_success"),

    path('upload/', profile_views.UploadUsers.as_view(), name="upload"),
    path('search/', profile_views.UserList.as_view(), name="users_list"),
    path('export/', profile_views.export_users, name="export"),
    path('list/', profile_views.list_users, name="list"),
    path('add/', profile_views.AddUserView.as_view(), name="add"),

    path('delete/<int:user_id>/', profile_views.delete_account_view, name="delete"),
    path('delete/complete/', profile_views.DeleteAccountComplete.as_view(), name="delete_complete"),
    path('export/mydata/<data_type>', profile_views.ExportDataView.as_view(), name="export_mydata"),
]
