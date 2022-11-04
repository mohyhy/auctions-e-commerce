from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("<int:pk>", views.product, name="pro"),
    path("watchlist",views.watch,name="watchlist"),
    path("cate",views.cate,name="cate"),
    path("create",views.create,name="create"),
    path("comment",views.comments,name="com"),
    path("close",views.close,name="close")
]
