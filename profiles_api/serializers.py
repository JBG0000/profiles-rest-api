from rest_framework import serializers


class HelloSerializer(serializers.Serializer):  #Serializer 클리스 이름
    """Serializes a name field for testing out APIView"""
    #APi view의 게시기능을 테스트하는데 사용됨 : django 형식과 매우 유사하게 작동

    #serializer에서 허용할 필드 지정
    name=serializers.CharField(max_length=10) #이름의 길이가 10을 넘는지 검수
