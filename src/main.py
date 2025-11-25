from src.app_container import AppContainer


app_container = AppContainer()

blog_service = app_container.blog_service()
user_service = app_container.user_service()

# Call the services directly from the api endpoints
