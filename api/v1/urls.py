from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import include, path

urlpatterns = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "schema/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("", include("api.v1.users.urls")),
    path("", include("api.v1.cats.urls")),
]
