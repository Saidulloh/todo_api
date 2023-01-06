from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken


class IsActiveToken(BasePermission):
    def has_permission(self, request, view):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        black_list_queryset = BlacklistedToken.objects.all()
        for token in tokens:
            if token in black_list_queryset: 
                return True
        return False
