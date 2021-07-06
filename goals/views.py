from django.shortcuts import get_object_or_404

from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from .serializers import GoalSerializer, MissionSerializer
import calendar
from datetime import date, datetime
from django_filters.rest_framework import DjangoFilterBackend
from calendars.models import Sphere

User = get_user_model()


def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    print(year, month, day)
    return date(year, month, day)


def get_goals(user):
    today = date.today()
    two_month_date = add_months(today, 2)
    six_month_date = add_months(today, 6)
    year_end_date = add_months(today, 12)

    m = datetime.now().month
    y = datetime.now().year
    ndays = calendar.monthrange(y, m)[1]
    start_date = date(y, m, 1)
    end_date = date(y, m, ndays)

    print(year_end_date)
    print(start_date, end_date)

    my_goals = user.my_goals.filter(date__range=[today, year_end_date])

    two_mounth, six_mounth, one_years = [], [], []
    (family_and_love, personal_growth, charity, investment,
        environment_and_friends, brightness_of_life, health_and_sports,
        business_and_career) = [], [], [], [], [], [], [], []

    for my_goal in my_goals:
        data = {
                "id": my_goal.id,
                "data": my_goal.text,
                "date": my_goal.date,
                "user_id": my_goal.author.id,
                "image": my_goal.image,
            }

        if my_goal.date >= today and my_goal.date <= two_month_date:
            two_mounth.append(data)
        elif my_goal.date >= two_month_date and my_goal.date <= six_month_date:
            six_mounth.append(data)
        elif my_goal.date >= six_month_date and my_goal.date <= year_end_date:
            one_years.append(data)

        if my_goal.sphere == Sphere.objects.get(slug="family_and_love"):
            family_and_love.append(data)
        elif my_goal.sphere == Sphere.objects.get(slug="personal_growth"):
            personal_growth.append(data)
        elif my_goal.sphere == Sphere.objects.get(slug="charity"):
            charity.append(data)
        elif my_goal.sphere == Sphere.objects.get(slug="investment"):
            investment.append(data)
        elif my_goal.sphere == Sphere.objects.get(slug="environment_and_friends"):
            environment_and_friends.append(data)
        elif my_goal.sphere == Sphere.objects.get(slug="brightness_of_life"):
            brightness_of_life.append(data)
        elif my_goal.sphere == Sphere.objects.get(slug="health_and_sports"):
            health_and_sports.append(data)
        elif my_goal.sphere == Sphere.objects.get(slug="business_and_career"):
            business_and_career.append(data)

    result = {
        "two_mounth": two_mounth,
        "six_mounth": six_mounth,
        "one_years": one_years,
        "family_and_love": family_and_love,
        "personal_growth": personal_growth,
        "charity": charity,
        "investment": investment,
        "environment_and_friends": environment_and_friends,
        "brightness_of_life": brightness_of_life,
        "health_and_sports": health_and_sports,
        "business_and_career": business_and_career,
    }

    return result


@api_view(['GET'])
def goals(request):
    result = get_goals(request.user)

    return Response(result)


class MyGoalsViewSet(viewsets.ModelViewSet):
    serializer_class = GoalSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['done', 'favorite']

    def get_queryset(self):
        user = get_object_or_404(User, email=self.request.user)
        return user.my_goals.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class MyMissionViewSet(viewsets.ModelViewSet):
    serializer_class = MissionSerializer

    def get_queryset(self):
        user = get_object_or_404(User, email=self.request.user)
        return user.my_mission.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
