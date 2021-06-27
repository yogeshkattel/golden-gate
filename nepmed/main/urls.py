from .views import *
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',Home.as_view(), name="home"),
    path('disease', BlogView.as_view(), name="diseaselist"),
    path('blog/<slug:slug>/detail', BlogDetailView.as_view(), name="blogdetail"),
    path('contactus/', contactus.as_view(), name="contactus"),
    path('queries/', ViewersProblemsView.as_view(), name="queries"),
    path('/blog/<slug:slug>/comment/<int:pk>/reply',CommentReplyView.as_view(), name="commentreply")
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)