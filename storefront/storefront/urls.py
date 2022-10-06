"""storefront URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import account
from playground import urls
from account import urls
import playground
from crud import views
# import debug_toolbar

urlpatterns = [
    path('admin/',admin.site.urls),
    path('playground/',include(playground.urls)),
    path('api/user/', include(account.urls)),
    path('__debug__/', include('debug_toolbar.urls')),
    # path('studentapi/',view=views.get_student),     # it is called when we use normal crud operation
    # """ functon based crud operation is called here """
    # path('studentapi/',view=views.function_based_student_api),
    # path('studentapi/<int:pk>',view=views.function_based_student_api),

    # """ class based operation is called here """
    path('studentapi/',view=views.StudentAPI.as_view()),
    path('studentapi/<int:pk>',view=views.StudentAPI.as_view())

]
