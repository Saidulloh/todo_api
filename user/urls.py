from rest_framework.routers import DefaultRouter

from user.views import UserViewSet


router = DefaultRouter()

router.register(
    prefix='user',
    viewset=UserViewSet
)

urlpatterns = router.urls
