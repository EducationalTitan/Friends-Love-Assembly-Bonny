from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from members import views
from members.views import blog_view
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('register/success/', views.registration_success, name='registration_success'),
    path('about-us/', views.about_us, name='about_us'),
    path('gallery/', views.gallery, name='gallery'),
    path('upcoming-events/', views.upcoming_events, name='upcoming_events'),
    path('blog/new/', views.create_blog_post, name='create_blog_post'),
    path('blog/', blog_view, name='blog'),
    path('success/', views.success, name='success'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
