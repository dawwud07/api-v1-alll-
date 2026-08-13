from django.urls import path , include
from . import views
from . import cb_view
from rest_framework.routers import DefaultRouter
from . import viewsets as daud

router = DefaultRouter()
router.register("appartments" , daud.AppartmentViewSet , basename="appartments")
router.register("objects" , daud.ObjectViewSet , basename="objects")
router.register("blocks" , daud.BlockViewSet , basename="blocks")

urlpatterns = [
    path('', include(router.urls)),
    path('cb-apartments/', cb_view.ApartmentListCreateAPIView.as_view()),
    path('cb-apartments/<int:pk>/', cb_view.ApartmentRetrieveUpdateDestroyAPIView.as_view()),
]






