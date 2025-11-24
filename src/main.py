from src import AppContainer


app_container = AppContainer()

blog_service = app_container.blog_service()
user_service = app_container.user_service()
