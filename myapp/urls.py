
from django.urls import path
from . import views
urlpatterns = [
#path('<int:id>/', views.list_notice_student, name='list_notices_student'),
path('<int:id>/', views.list_notice, name='list_notices'),
path('login/', views.login_view, name='login'),
path('register/', views.register_user, name='register'),
path('logout/', views.logout_view, name='logout'),
path('new/', views.create_notice, name='create_notices'),
path('update/<int:id>/', views.update_notice, name='update_notices'),
# path('board/',views.board),
path('delete/<int:id>/', views.delete_notice, name='delete_notices')
]