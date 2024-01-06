from rest_framework import permissions


class IsOwnerOrReadOnlyPermission(permissions.BasePermission):
    message = 'You don\'t have permission to access this resource.'

    def has_object_permission(self, request, view):
        if (
                view.action == 'update' or
                view.action == 'partial_update' or
                view.action == 'update_image' or
                view.action == 'create'
        ):
            return request.user.is_staff
        return True
