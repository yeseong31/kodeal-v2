from rest_framework import permissions


class CustomReadOnly(permissions.BasePermission):
    """커스텀 권한: 데이터 접근"""

    def has_object_permission(self, request, view, obj):
        """전체 객체에 대한 권한"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user

    def has_permission(self, request, view):
        """객체별 권한"""
        if request.method == 'GET':
            return True
        return request.user.is_authenticated
