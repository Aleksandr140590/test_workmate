from djoser.views import UserViewSet
from drf_spectacular.utils import extend_schema_view

from api.v1.schema_extensions import USERS_API_SCHEMA_EXTENSIONS


@extend_schema_view(**USERS_API_SCHEMA_EXTENSIONS)
class CustomUserViewSet(UserViewSet):
    pass
