from django.conf.urls import url
from permits import views

urlpatterns = [
    url(r'^/', admin.site.urls),
    url(
        regex=r'^create/',
        view=views.FoodFacilityPermitsListView.as_view(),
        name='create_food_permits'
    ),
    url(
        regex=r'^/(?P<pk>\d+)',
        view=views.FoodFacilityPermitsUpdateView.as_view(),
        name='update_delete_food_permits'
    ),
]
