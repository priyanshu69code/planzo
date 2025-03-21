from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, UpdateUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import BasePermission
from rest_framework.decorators import api_view, permission_classes

class IsVerified(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_verified

MyUser = get_user_model()


class RegisterView(CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": UserSerializer(user).data
        })


class UserDetailView(RetrieveAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsVerified]

    def get_object(self):
        return self.request.user


class UpdateUserView(UpdateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = [IsAuthenticated, IsVerified]

    def get_object(self):
        return self.request.user


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=204)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def verify_user(request, verification_secret):
    user = MyUser.objects.get(verification_secret=verification_secret)
    user.is_verified = True
    user.save()
    return Response({"message": "User Verified"})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def send_verification_link(request):
    user = request.user
    return Response({"message": "Verification Link Sent"})
