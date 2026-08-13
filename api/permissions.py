from rest_framework.permissions import BasePermission , SAFE_METHODS


class IsSuperUser(BasePermission):
        def has_permission(self, request, view):
            # if request.method in SAFE_METHODS :
            #     return True
            # return False
        
                return request.methos in SAFE_METHODS
            
            
        def has_object_permission(self, request, view, obj):
                return request.user.is_staff and request.user.is_superuser