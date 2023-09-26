from django.urls import path
from .views import SignUpView
from .views import LoginView
from . import views


# schema_view = get_swagger_view(title='Pastebin API')
urlpatterns = [
    # path(r'docs/', include_docs_urls(title='BuyMed')),
    path('register/', SignUpView.as_view(), name='auth_register'),
    path('login/', LoginView.as_view(), name='login')
]