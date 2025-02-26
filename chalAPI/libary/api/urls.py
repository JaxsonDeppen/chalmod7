from django.urls import path, include
from rest_framework.routers import DefaultRouter
from libary.api.views import AuthorListCreate, AuthorDetail, BookListCreate, BookDetail, LoanViewSet

router = DefaultRouter()
router.register(r'loans', LoanViewSet)

urlpatterns = [
    path('authors/', AuthorListCreate.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('', include(router.urls)),
]
