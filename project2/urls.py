from django.urls import path,include

urlpatterns = [
    path('',include("a_app.urls"))
]
