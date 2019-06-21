# Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'snippets', views.SnippetViewSet)
# router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
from django.conf.urls import url
from django.urls import include
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),
]
urlpatterns = format_suffix_patterns(urlpatterns, allowed=["api", "json"])
