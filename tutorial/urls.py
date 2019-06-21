from django.conf.urls import include, url
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

# API_TITLE = 'Pastebin API'
# API_DESCRIPTION = 'A Web API for creating and viewing highlighted code snippets.'
# schema_view = get_schema_view(title=API_TITLE)

urlpatterns = [
    url(r'^', include('snippets.urls')),
]