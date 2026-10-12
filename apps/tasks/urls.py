from rest_framework import routers
from .views import TasksViewsets

router=routers.DefaultRouter()

router.register("tasks",TasksViewsets,basename='tasks')

urlpatterns=router.urls
