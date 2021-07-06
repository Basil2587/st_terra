from main_page.views import main_page
from django.urls import include, path
from rest_framework.routers import DefaultRouter


from results.views import *
from lists.views import *
from values.views import *
from users.views import *
from calendars.views import *
from goals.views import *
from analytics.views import *


router = DefaultRouter()
router.register("results/targets", TargetViewSet, basename="targets")
router.register("results/plans", PlanViewSet, basename="plans")
router.register("results/week_diaries",
                WeekDiaryViewSet, basename="week_diaries")
router.register("results/month_diaries",
                MonthDiaryViewSet, basename="month_diaries")

router.register("lists/books", BookViewSet, basename="books")
router.register("lists/films", FilmViewSet, basename="films")
router.register("lists/wishes", WishViewSet, basename="wishes")
router.register("lists/travels", TravelViewSet, basename="travels")

router.register("values/values", ValueViewSet, basename="values")
router.register("values/principles", PrincipleViewSet, basename="principles")
router.register("values/quotes", QuoteViewSet, basename="quotes")
router.register("values/algorithm_business", AlgorithmBusinessViewSet,
                basename="algorithm_business")
router.register("values/algorithm_relationships",
                AlgorithmRelationshipsViewSet,
                basename="algorithm_relationships")

router.register("calendar/day", DayViewSet, basename="day")
router.register("calendar/week", WeekViewSet, basename="week")
router.register("calendar/month", MonthViewSet, basename="month")

router.register("sphere_preset", SpherePresetViewSet, basename="sphere_preset")

router.register("goals/goals", MyGoalsViewSet, basename="goals")
router.register("goals/mission", MyMissionViewSet, basename="mission")

# router.register("")

urlpatterns = [
    path('v1/user/', UserRetrieveUpdateAPIView.as_view()),
    path('v1/users/', RegistrationAPIView.as_view()),
    path('v1/users/login/', LoginAPIView.as_view()),
    path("v1/lists/", lists),
    path("v1/results/", results),
    path("v1/values/", values),
    path("v1/goals/", goals),  
    path("v1/main_page/", main_page),
    path("v1/analytics/", analytics),
    path('v1/diary/', include('diaries.urls')),
    path("v1/", include(router.urls)),
]
