from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
import profiles.urls
import accounts.urls
from . import views

# Personalized admin site settings like title and header
admin.site.site_title = "Main Site Admin"
admin.site.site_header = "Main Administration"

urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    path("users/", include(profiles.urls)),
    path("admin/", admin.site.urls),
    path("", include(accounts.urls)),
    path("comments/", views.CommentsPage.as_view(), name="comments"),
    path("add_comment/", views.AddComment.as_view(), name="add_comment"),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
