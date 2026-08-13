from django.urls  import path , include

urlpatterns = [
    path('estate/', include("apps.estate.urls")),
    path('accounts/', include("apps.accounts.urls")),
    path("", include("api.yasg")),
] 