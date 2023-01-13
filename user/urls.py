from rest_framework.routers import DefaultRouter

from user.views import UserViewSet


router = DefaultRouter()

router.register(
    prefix='users',
    viewset=UserViewSet
)

urlpatterns = router.urls
