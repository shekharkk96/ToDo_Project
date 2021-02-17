"""ToDo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from ToDo_app import views
import rest_framework
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('update_item/<str:pk>/',views.updatetask,name="updatetask"),
    path('delete_item/<str:pk>/',views.deletetask,name="deletetask"),
    path('api-admin/', include('rest_framework.urls', namespace='rest_framework')),
    path('list/',views.appList_list, name = 'appListList'),
    path('detail/<int:pk>/',views.list_detail, name='listdetail'),
    path('classlist/', views.ListList.as_view()),
    path('classdetail/<int:pk>', views.ListDetail.as_view()),
    path('genericlist/',views.GenericList.as_view()),
    path('genericlist/<int:id>',views.GenericDetail.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
