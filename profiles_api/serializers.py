from rest_framework import serializers

from profiles_api import models #Profiles API에 사용


class HelloSerializer(serializers.Serializer):  #Serializer 클래스 이름
    """Serializes a name field for testing out APIView"""
    #APi view의 게시기능을 테스트하는데 사용됨 : django 형식과 매우 유사하게 작동

    #serializer에서 허용할 필드 지정
    name=serializers.CharField(max_length=10) #이름의 길이가 10을 넘는지 검수

class UserProfileSerializer(serializers.ModelSerializer):   #ModelSerializer 사용
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile  #model 변수 새로 정의
        #관리하려는 필드 목록
        fields = ('id', 'email', 'name', 'password')    #패스워드는 추가키워드 사용
        extra_kwargs = {
            'password': {
                'write_only': True, #True는 새 개체를 만들거나 업데이트하는데만 사용가능함을 뜻함
                'style': {'input_type': 'password'} #사용자정의 스타일추가:입력하는동안 입력 볼 ㅅ ㅜ없음
            }
        }

        #create 함수 재정의 : 이전에 정의한 사용자 생성기능 호출,기반으로 DB에 검증된 새 사용 생성
    def create(self, validated_data):   #새 사용자 생성하고 검증된 데이터를 반환하는 text문자열 제공
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            # 검증된 데이터 값들을 변수에 저장
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user #검증된 새 사용자 반환

    #46 버그 수정
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
