from rest_framework.views import APIView    #APIView 클래스 가져오기
from rest_framework.response import Response    #Response object 가져옴


class HelloApiView(APIView):    #문서 문자열 테스트 API 보기
    """Test API View"""


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
