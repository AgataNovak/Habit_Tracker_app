from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Класс определяет права для группы пользователей владельцев/создателей объекта"""

    message = "Not allowed to retrieve, update or destroy not owner's habits"

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
