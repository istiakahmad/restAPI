from django.contrib import admin
from django.urls import path, include


from .views import (
        # StatusListSearchAPIView,
        StatusAPIView,
        # StatusCreateAPIView,
        # StatusDetailAPIView,
        # StatusUpdateAPIView,
        # StatusDeleteAPIView,
)

urlpatterns = [
    # path('', StatusListSearchAPIView.as_view()),
    path('', StatusAPIView.as_view()),
    # path('create/', StatusCreateAPIView.as_view()),
    # #path('<int:id>/create', StatusCreateAPIView.as_view()), # if define a function (get_object()) which return a id
    # path('<pk>', StatusDetailAPIView.as_view()),
    # path('update/<pk>', StatusUpdateAPIView.as_view()),
    # path('delete/<pk>', StatusDeleteAPIView.as_view()),

]
