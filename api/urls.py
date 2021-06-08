from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import (
    results,
    lists,
    values,
    goals,
    TargetViewSet,
    PlanViewSet,
    DiaryViewSet,
    BookViewSet,
    FilmViewSet,
    WishViewSet,
    TravelViewSet,
    ValueViewSet,
    PrincipleViewSet,
    QuoteViewSet,
    AlgorithmBusinessViewSet,
    AlgorithmRelationshipsViewSet
from goals.views import MyGoalsViewSet
)
from . import views
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )


router = DefaultRouter()
router.register("results/targets", TargetViewSet, basename="targets")
router.register("results/plans", PlanViewSet, basename="plans")
router.register("results/diaries", DiaryViewSet, basename="diaries")

router.register("lists/books", BookViewSet, basename="books")
router.register("lists/films", FilmViewSet, basename="films")
router.register("lists/wishes", WishViewSet, basename="wishes")
router.register("lists/travels", TravelViewSet, basename="travels")

router.register("goals/goals", MyGoalsViewSet, basename="goals")

router.register("values/values", ValueViewSet, basename="values")
router.register("values/principles", PrincipleViewSet, basename="principles")
router.register("values/quotes", QuoteViewSet, basename="quotes")
router.register("values/algorithm_business", AlgorithmBusinessViewSet, basename="algorithm_business")
router.register("values/algorithm_relationships", AlgorithmRelationshipsViewSet, basename="algorithm_relationships")

urlpatterns = [
    path("v1/lists/", lists),
    path("v1/goals/", goals),
    path("v1/results/", results),
    path("v1/values/", values),
    path("v1/", include(router.urls)),
    path(
        "v1/token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair"
    ),
    path(
        "v1/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh"
    ),
]
