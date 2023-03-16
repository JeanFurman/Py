from rest_framework.routers import DefaultRouter

from .views import LivrosViewSet

router = DefaultRouter()
router.register(r'', LivrosViewSet, basename='livros')

livros_urls = router.urls