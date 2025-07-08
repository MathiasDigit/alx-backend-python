from rest_framework.permissions import BasePermission
class IsOwner(BasePermission):
    """The user can only access his own messages/conversations."""
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
    