from rest_framework import permissions

#사용자 스스로 자신 프로필 편집 가능하도록 하는 permissions class
class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    #사용자 권한 클래스 정의 : has 사용
    def has_object_permission(self, request, view, obj):    #obj : 업데이트되는 객체(데이터)인듯
        #사용자가 자신의 데이터를 수정 시도하는지 확인
        #이곳에서 일어나는건 django rest framework를 요청할때마다 발생
        """Check user is trying to edit their own profile"""
        # SAFE_METHODS : HTTP 메서드?(GET, PUT, PATCH, DELETE)
        if request.method in permissions.SAFE_METHODS:  #요청메서드가 SAFE_METHODS라면 True 반환
            return True

        #업데이트할 객체(obj)의 id와 요쳥하는 유저의 id를 비교해서 bool 반환
        return obj.id == request.user.id

        #위 두가지가 모두 true인 경우에 허가...내리는 클래스인 것으로 일단 이해
