
from . import views


app_name = "flight"

urlpatterns = [
    path("", views.index, name="index")
]
