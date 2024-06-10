from rest_framework import permissions

class UserPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'update','retrieve','destroy', 'del_dish', 'add_to_dish']:
            return request.user.is_authenticated and request.user.is_staff
        elif view.action=='create':
            return True
        else:
            return False
        
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if view.action in ['list', 'update','retrieve','destroy', 'del_dish', 'add_to_dish']:
            return obj == request.user or request.use.is_staff
        else:
            return False
        