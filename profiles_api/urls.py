from django.urls import path

from profiles_api import views  #API View가 포함된 view 혹은 vies모듈 임포트


urlpatterns = [ #View에 매핑되는 경로
    path('hello-view/', views.HelloApiView.as_view()),  #경로, 호출
]

#URL을 먼저 확인하고 일치하는 URL API로 모든걸 전달
