class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self,request,view):
        if request.metod in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff


class IsCuratorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.metod in permissions.SAFE_METHODS:
            return True
    qs = Curator.objects
    qs = qs.filter(user = request.user)
    qs = qs.exists()
    return qs