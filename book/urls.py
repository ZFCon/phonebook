from django.urls import path, include
from rest_framework.routers import DefaultRouter
from book.views import ContactViewSet, PhoneNumberViewSet

router = DefaultRouter()
router.register(r'contacts', ContactViewSet)
router.register(r'phonenumbers', PhoneNumberViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
