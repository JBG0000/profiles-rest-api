from django.urls import path, include   #APIView는 path만으로도 충분하지만 Viewsets 사용하면 include도 import

from rest_framework.routers import DefaultRouter    #Viewset 라우터

from profiles_api import views  #API View가 포함된 view 혹은 vies모듈 임포트

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset') #URL 사용하여 필요시 라우터에서 URL 검색
router.register('profile', views.UserProfileViewSet)    #UseProfileViewSet 클래스 라우팅, 할당된 모델에서 이름 알아낼 수 있으므로 base_name 작성 안해도 됨

urlpatterns = [ #View에 매핑되는 경로
    path('hello-view/', views.HelloApiView.as_view()),  #경로, 호출 : APiView
    path('login/', views.UserLoginApiView.as_view()), #로그인 APIView 경로, 호출

    path('',  include(router.urls)),    #ViewSets 경로
    #첫 인수가 빈 문자열인 이유는 이 URL에 접두사를 추가하고 싶지 않기 때문에
]
#URL을 먼저 확인하고 일치하는 URL API로 모든걸 전달
