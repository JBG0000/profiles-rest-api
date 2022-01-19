from rest_framework.views import APIView    #APIView 클래스 가져오기
from rest_framework import viewsets #Viewsets 클래스 가져오기

from rest_framework.response import Response    #Response object 가져옴
from rest_framework import status   #API에서 응답 바나환할 때 사용할 수 있는 HTTP status code
from rest_framework.authentication import TokenAuthentication   #사용자 API로 자신을 인증하는데 사용하는 토큰
from rest_framework import filters  #profile API에서 검색 기능 추가 시 사용 filters

from profiles_api import permissions    #작성한 permissions.py 참조
from profiles_api import serializers, models    #작성한 serializers, models 임포트

class HelloApiView(APIView):    #문서 문자열 테스트 APIView
    """Test API View"""
    serializer_class = serializers.HelloSerializer  #serializers 클래스가 포함된 API View
    #serializers는 정의한대로, 게시물 추가 패치 요청을 보낼 때마다 이름값을 요구함
    #여기에 전역으로 정의해두면 밑에 정의한 함수들에서 갖다다가 씀(POST)


    #일반덕으로 djangorestframework가 get이라 부르는 함수 정의
    #self : 모든것에 쓰임, request : django rest framework에 의해 전달, format : request의 세부정보 포함, 엔드포인트 url에 접미사 추가
    def get(self, request, format=None):    #API에 대한 HTTP GET 요청을 수락
        """Returns a list of APIView features"""
        #GET 함수는 API view가 분리되는 방식이므로 HTTP GET 요청을 위해 뷰에 만들 수 있는 다양한 HTTP 요청을 위한 함수가 필요함
        #View는 GET함수를 호출하고 정의한 로직 실행
        #이 get함수에서는 APIView의 모든 기능을 설명하는 목록 정

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        #response object를 json으로 변환
        #json으로 변환하기 위해서는 리스트나 딕셔너리가 필요
        #여기서는 딕셔너리 반환, 중괋호 열어서 message 키 : 문자열 hello!할당, an_apiview 키 :an_apiview 할당
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})


    #POST 함수 정의
    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)       #API view에 대한 요청은 request 데이터로 요청, serializer 입력을 검증하는 djangorestframework의 serializer

        #serializer로 유효성이 검증 되었다면
        if serializer.is_valid():
            name = serializer.validated_data.get('name')    #검증된 데이터 가져오기
            message = f'Hello {name}'  #앞에 f를 넣으면 문자열에 변수 삽입 가능
            return Response({'message' : message})  #메세지 출력
        #아니라면
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST  #HTTP 400대 에러 출력, 정상동작시 200
            )

    #전체 개체를 업데이트할 때 쓰는 PUT 함수 정의
    def put(self, request, pk=None):    #pk 없음 : 특정한 URL 기본 키로 put 수행... PK를 가지고 있으나 원하지 않는 경우를 대비해 기본적으로 없음 설정
        """Handle updating an object""" #업트하려는 개체의 ID로 URL에 넣기 수행, 객체의 ID를 실제로 객체를 업데이트 하지 않을 예쩡인 putㅇ요청으로 업데이트됨

        return Response({'method': 'PUT'})

    #개체의 부분 업데이트 할 떄 쓰이는 patch : 이전에 있었던 필드만 업데이트
    def patch(self, request, pk=None):
        """Handle partial update of object"""

        return Response({'method': 'PATCH'})

    #put은 기본적으로 객체를 제공된 객체로 대체하는것..? patch는 요청에 재공된 필드만 업데이트


    #삭제 메서드인 delete
    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method': 'DELETE'})



#위에는 APIView 클래스고 밑에는 Viewsets 클래스
class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer  #serializers 클래스가 포함된 ViewSets

    #APiView와 추가하는 기능이 다름

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})


    #생성
    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)   #위에서 똑같이 씀

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    #검색
    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    #HTTP 매핑 전체 업데이트
    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    #부분 업데이트
    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    #HTTP Delete 호출
    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})

#######################################################################

#profile viewset 정의
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer    #UserProfileSerializer 사용해서 검증
    queryset = models.UserProfile.objects.all() #..?viewsets 함수들 이용하는데 사용하는듯

    authentication_classes = (TokenAuthentication,) # 사용자 인증 방법 설정, 특정 작업 수행 및 특정 API 사용 권한에 대한 것, 단일 항목이 아닌 튜플로 생성
    permission_classes = (permissions.UpdateOwnProfile,)    #permissions.py에서 작성한 권한에 대한 코드(유저 확인 및 메소드 확인)

    filter_backends = (filters.SearchFilter,)   #백엔드에서 filter하겠다는 코드, 단일 항목이 아닌 튜플
    search_fields = ('name', 'email',)  #search_fields는 지정한 필드에서 검색가능하게 한다는것을 의미..?
