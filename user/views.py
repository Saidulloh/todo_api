from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from user.models import User
from user.serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DeactivateTokenApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            tokens = OutstandingToken.objects.filter(user_id=request.user.id)
            for token in tokens:
                t, _ = BlacklistedToken.objects.get_or_create(token=token)
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST)
