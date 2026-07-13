from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == permissions.SAFE_METHODS:
            return True
        return obj.author == request.user or request.user.is_superuser
    
class CanPublishPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('articles.can_publish_article')