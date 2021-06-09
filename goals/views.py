
from django.shortcuts import get_object_or_404

from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from .serializers import GoalSerializer
import calendar
from datetime import date, datetime
import requests



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

    for my_goal in my_goals:
        if my_goal.date >= today and my_goal.date <= two_month_date:
            two_mounth.append({
                "id": my_goal.id,
                "data": my_goal.text,
                "status": my_goal.done,
                "date": my_goal.date,
                "user_id": my_goal.author.id,
            })
        if my_goal.date >= two_month_date and my_goal.date <= six_month_date:
            six_mounth.append({
                "id": my_goal.id,
                "data": my_goal.text,
                "status": my_goal.done,
                "date": my_goal.date,
                "user_id": my_goal.author.id,
                })
        if my_goal.date >= six_month_date and my_goal.date <= year_end_date:
            one_years.append({
                "id": my_goal.id,
                "data": my_goal.text,
                "status": my_goal.done,
                "date": my_goal.date,
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
    result = get_goals(request.user)

    return Response(result)


class MyGoalsViewSet(viewsets.ModelViewSet):
    serializer_class = GoalSerializer

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return user.my_goals.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
