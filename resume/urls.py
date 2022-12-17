from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import ResumeModelViewSet
from .views import toronto

router = DefaultRouter()
router.register(r'resume', ResumeModelViewSet, basename='user-api')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('resume/toronto', toronto),
]
