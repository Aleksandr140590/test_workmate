from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenVerifyView,
    TokenRefreshView,
)

from api.v1.schema_extensions import TOKEN_API_SCHEMA_EXTENSIONS
from api.v1.users.views import CustomUserViewSet

router = routers.DefaultRouter()
router.register("users", CustomUserViewSet, basename="users")


def is_route_selected(url_pattern):
    """Фильтр для ручек пользователя"""
    urls = [
        "users/activation/",
        "users/reset_password/",
        "users/change_password/",
        "users/change_email/",
        "users/reset_password_confirm/",
        "users/reset_password_complete/",
        "users/resend_activation/",
        "users/reset_username/",
        "users/reset_username_confirm/",
    ]

    for u in urls:
        match = url_pattern.resolve(u)
        if match:
            return False
    return True


selected_user_routes = list(filter(is_route_selected, router.urls))

# Декораторы документации SWAGGER
decorated_jwt_create_view = TOKEN_API_SCHEMA_EXTENSIONS["create"](
    TokenObtainPairView
)
decorated_jwt_verify_view = TOKEN_API_SCHEMA_EXTENSIONS["verify"](
    TokenVerifyView
)

decorated_jwt_refresh_view = TOKEN_API_SCHEMA_EXTENSIONS["refresh"](
    TokenRefreshView
)

urlpatterns = [
    path(
        "auth/jwt/create/",
        decorated_jwt_create_view.as_view(),
        name="jwt-create",
    ),
    path(
        "auth/jwt/refresh/",
        decorated_jwt_refresh_view.as_view(),
        name="jwt-refresh",
    ),
    path(
        "auth/jwt/verify/",
        decorated_jwt_verify_view.as_view(),
        name="jwt-verify",
    ),
] + selected_user_routes
