from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    # ===WEB urls==
    # Main urls.
    path("", Web.index, name="index"),

    path("api/create_user/<int:user_id>/<str:username>/<str:first_name>/<str:last_name>",
         API.CreateUser.as_view(), name="create_user"),
    path("api/run_attack/<int:user_id>/<int:phone>",
         API.RunAttack.as_view(), name="run_attack"),
    path("api/stop_attack/<str:pk>", API.StopAttack.as_view(), name="stop_attack"),
    path("api/get_statistic", API.Statistic.as_view(), name="get_statistic"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
