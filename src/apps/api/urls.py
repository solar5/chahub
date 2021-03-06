from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter
# from rest_framework_swagger.views import get_swagger_view
from api.views.producers import ProducerViewSet
from .views import competitions, data, profiles, search

# from .views.search import query


router = SimpleRouter()
router.register('producers', ProducerViewSet)
router.register('competitions', competitions.CompetitionViewSet)
router.register('submissions', competitions.SubmissionViewSet)

API_PREFIX = "v1"

urlpatterns = [
    url('^', include(router.urls)),
    # url('docs/', get_swagger_view(title='Codalab')),

    # Docs are on /api/schema
    # url(f'^', include('drf_openapi.urls')),

    url('query/', search.SearchView.as_view()),
    url('my_profile/', profiles.GetMyProfile.as_view()),

    url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
