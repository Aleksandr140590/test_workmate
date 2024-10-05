from drf_spectacular.utils import extend_schema, OpenApiParameter

USERS_API_SCHEMA_EXTENSIONS = {
    "list": extend_schema(
        tags=["Пользователи"], summary="Получить список пользователей"
    ),
    "create": extend_schema(
        tags=["Пользователи"], summary="Создать нового пользователя"
    ),
    "me": extend_schema(
        tags=["Пользователи"], summary="Данные о пользователе"
    ),
    "set_password": extend_schema(
        tags=["Пользователи"], summary="Изменение пароля пользователя"
    ),
    "set_username": extend_schema(
        tags=["Пользователи"], summary="Изменения ника пользователя"
    ),
}

CATS_API_SCHEMA_EXTENSIONS = {
    "list": extend_schema(
        tags=["Кошки"],
        summary="Получить список кошек",
        parameters=[
            OpenApiParameter(
                name="breed",
                description="Фильтр по части названия породы кошек",
            )
        ],
    ),
    "create": extend_schema(
        tags=["Кошки"], summary="Создать запись о новой кошке"
    ),
    "retrieve": extend_schema(
        tags=["Кошки"], summary="Получить информацию о кошке"
    ),
    "update": extend_schema(
        tags=["Кошки"], summary="Изменить информацию о кошке"
    ),
    "partial_update": extend_schema(
        tags=["Кошки"], summary="Изменить частично информацию о кошке"
    ),
    "destroy": extend_schema(
        tags=["Кошки"], summary="Удалить запись о новой кошке"
    ),
}

BREEDS_API_SCHEMA_EXTENSIONS = {
    "list": extend_schema(
        tags=["Породы кошек"], summary="Получить список кошек"
    ),
}

TOKEN_API_SCHEMA_EXTENSIONS = {
    "create": extend_schema(
        tags=["Авторизация"],
        summary="Создать токен авторизации",
        methods=["POST"],
    ),
    "refresh": extend_schema(
        tags=["Авторизация"],
        summary="Обновить токен авторизации",
        methods=["POST"],
    ),
    "verify": extend_schema(
        tags=["Авторизация"],
        summary="Проверить токен авторизации",
        methods=["POST"],
    ),
}
