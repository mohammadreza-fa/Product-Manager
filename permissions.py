from rest_framework.permissions import BasePermission


class IsAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)


class IsManagerUser(BasePermission):
    """
    Allows access only to manager users.
    """
    def has_permission(self, request, view):
        return (
            request.user and
            request.user.is_admin and
            request.user.is_authenticated and
            request.user.role == 'manager'
        )


class IsManagerOrDistributorUser(BasePermission):
    """
    Allows access only to manager users or distributor user.
    """
    def has_permission(self, request, view):
        return (
                request.user and
                request.user.is_authenticated and
                request.user.is_staff and
                request.user.role == 'manager' or request.user.role == 'distributor'
        )
