"""monkey_garden URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework import routers
from root.views import root, mypage

from accounts.views import FacebookLogin, UserDeviceViewSet, UserViewSet
from garden.views import MessageViewSet, MessageHistoryViewSet

router = routers.SimpleRouter()
router.register(r'user', UserViewSet)
router.register(r'device', UserDeviceViewSet)
router.register(r'message', MessageViewSet)
router.register(r'message_history', MessageHistoryViewSet),

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', root),
    url(r'mypage/^$', mypage, name="mypage"),
    url(r'api/v1/', include(router.urls)),
    url(r'^api/v1/rest-auth/', include('rest_auth.urls')),
    url(r'^api/v1/rest-auth/facebook/$', FacebookLogin.as_view(), name="fb_login"),
    url(r'^fcm/', include('fcm.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
