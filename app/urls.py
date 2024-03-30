from django.urls import path
from app.views import index, search, filme, infouser
from app.userform import register, loginview, logoutview, updateview, deleteview
from app.reviewform import create, update, delete
app_name = 'app'

urlpatterns = [
    path('', index, name='index'),
    path('search/', search, name='search'),
    path('filme/<int:filme_id>/', filme, name='filme'),

    path('review/create/', create, name='create'),
    path('review/<int:review_id>/update/', update, name='update'),
    path('review/<int:review_id>/delete/', delete, name='delete'),


    path('user/create/', register, name='register'),
    path('user/login/', loginview, name='login'),
    path('user/logout/', logoutview, name='logout'),
    path('user/update/', updateview, name='userupdate'),
    path('user/delete/', deleteview, name='userdelete'),
    path('user/info/', infouser, name='userinfo'),
]

