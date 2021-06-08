from django.shortcuts import get_object_or_404

from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from api.serializers import GoalSerializer

from datetime import date, datetime
import requests

from goals.models import GoalType, MyGoals


User = get_user_model()


def get_goals(user):
    m = datetime.now().month
    f = lambda m: m-12 if m>12 else m
    y = datetime.now().year
    ndays = (date(y, m+2, 1) - date(y, m+1, 1)).days
    start_date = date(y, m, 1)
    end_date = date(y, f(m+1), ndays)

    month_start_date = start_date
    month_end_date = date(y, f(m+1), (date(y, m+2, 1) - date(y, m+1, 1)).days)
    six_month_start_date = date(y, f(m+2), 1)
    six_month_end_date = date(
        y,
        f(m+6),
        (date(y, m+2, 1) - date(y, m+1, 1)).days
    )
    year_start_date = date(y, f(m+6), 1)
    year_end_date = date(
        y,
        f(m+12),
        (date(y, m+2, 1) - date(y, m+1, 1)).days
    )
    
    my_goals = user.my_goals.filter(date__range=[start_date, end_date])

    two_mounth, six_mounth, one_years = [], [], []

    for my_goal in my_goals:
        if my_goal.date >= month_start_date and my_goal.date <= month_end_date:
            two_mounth.append({
                "id": my_goal.id,
                "data": my_goal.text,
                "image": my_goal.image,
                "user_id": my_goal.author.id,
            })
        if my_goal.date >= six_month_start_date and my_goal.date <= six_month_end_date:
            six_mounth.append({
                "id": my_goal.id,
                "data": my_goal.text,
                "image": my_goal.image,
                "user_id": my_goal.author.id,
                })
        if my_goal.date >= year_start_date and my_goal.date <= year_end_date:
            one_years.append({
                "id": my_goal.id,
                "data": my_goal.text,
                "image": my_goal.image,
                "user_id": my_goal.author.id,
                })

    result = {
        "two_mounth": two_mounth,
        "six_mounth": six_mounth,
        "one_years": one_years,
    }

    return result


@api_view(['GET'])
def goals(request):
    result = get_results(request.user)

    return Response(result)


class MyGoalsViewSet(viewsets.ModelViewSet):
    serializer_class = GoalSerializer

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return user.targets.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
