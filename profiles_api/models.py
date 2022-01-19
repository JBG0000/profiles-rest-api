from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

#부모 클래스 BaseUserManager로 지정
class UserProfileManager(BaseUserManager):
    """Manager for user profiles""" #관리자가 사용하는 모델, 관리자 작업 방식은 사용자가 지정함

    #커맨드라인에서 사용자 생성 함수
    def create_user(self, email, name, password=None):  #패스워드 기본값 없음 : 비밀번호 없으면 기본적으로 사용자 인증 불가능
        """Create a new user profile"""
        if not email:   #이메일 없을 시 아래 에러 출력
            raise ValueError('User must have an email address')

        email = self.normalize_email(email) #이메일 정규화
        user = self.model(email=email, name=name)

        user.set_password(password) #비밀번호 암호화
        user.save(using=self._db)   #추후에 여러 데이터베이스 지원해야하는 경우 self._db사용

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given detaiils"""
        user=self.create_user(email, name, password)

        user.is_superuser = True    #수퍼유저 맞음
        user.is_staff = True    #직원 맞음
        user.save(using=self._db)   #여러 데베 접근 가능?

        return user


#데이터베이스에 email, name, is_active, is_staff 열 생성
class UserProfile(AbstractBaseUser, PermissionsMixin): #카멜 케이스로 작성
    """Database model for users in the system"""    #클래스 목적
    email = models.EmailField(max_length=255, unique=True)  #이메일 받기 : 255자 이내, 값은 고유해야함
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)   #사용자 활성화 비활성화 여부
    is_staff = models.BooleanField(default=False)   #사용자 관리자 액세스 권한 여부(true: 관리자, false: 사용자)

    objects = UserProfileManager()  #관리나 클래스를 생성할 예정, 아직 생성하지 않았지만 추후 만들것

    #유저네임필드를 email로 지정했다
    #최소한 사용자가 이메일과 이름을 지정해야함
    USERNAME_FIELD = 'email'    #사용자 이름 필드 대체, 이메일 필드를 사용해 사용자 이름과 비밀번호 제공할 것
    REQUIRED_FIELDS = ['name']

    def get_full_name(self): #전체 이름 검색 기능, 클래스ㅔ서 함수를 정의하고 있기 때문에 self를 첫번째로 지정
        """Retrieve full name for user"""
        return self.name    #이름 반환

    def get_short_name(self): #짧은 이름 검색 가져오기
        """Retrieve short name of user"""
        return self.name   #이름 반환

    def __str__(self):  #사용자 프로필 개체를 python에서 문자열로 변환
        """Return string representation of user"""
        return self.email   #이메일 주소 반환
