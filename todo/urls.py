from rest_framework.routers import DefaultRouter

from todo.views import TodoViewSet

router = DefaultRouter()
router.register(
    prefix='todo',
    viewset=TodoViewSet
)

urlpatterns = router.urls
