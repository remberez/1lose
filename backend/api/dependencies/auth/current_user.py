from .fastapi_users import fastapi_users

# Зависимости для получения авторизированного пользователя
current_user = fastapi_users.current_user()
current_user_optional = fastapi_users.current_user(optional=True)
current_active_user = fastapi_users.current_user(active=True)
current_active_verify_user = fastapi_users.current_user(active=True, verified=True)
