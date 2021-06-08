from django.shortcuts import get_object_or_404
from requests.api import request
from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from api.serializers import (
    TargetSerializer,
    PlanSerializer,
    ListSerializer,
    ValueSerializer, AlgorithmSerializer, GoalSerializer)

from datetime import date, datetime
import requests
import arrow

from lists.models import ListType, MyList
from values.models import Value, ValueType, Algorithm, AlgorithmType
from goals.models import GoalType, MyGoals
User = get_user_model()

##############################################################################

# Начало блока Итогов

def get_results(user):

    m = datetime.now().month
    y = datetime.now().year
    ndays = (date(y, m+2, 1) - date(y, m+1, 1)).days
    start_date = date(y, m, 1)
    end_date = date(y, m+1, ndays)

    month_start_date = start_date
    month_end_date = date(y, m, (date(y, m+1, 1) - date(y, m, 1)).days)
    next_month_start_date = date(y, m+1, 1)
    next_month_end_date = date(
        y,
        m+1,
        (date(y, m+2, 1) - date(y, m+1, 1)).days
    )

    today = arrow.now()
    week_start_date = datetime.strptime(
        f'{today.floor("week"):YYYY-MM-DD}', "%Y-%m-%d"
    ).date()
    week_end_date = datetime.strptime(
        f'{today.ceil("week"):YYYY-MM-DD}', "%Y-%m-%d"
    ).date()
    next_week_start_date = datetime.strptime(
        f'{(today.shift(days=7)).floor("week"):YYYY-MM-DD}', "%Y-%m-%d"
    ).date()
    next_week_end_date = datetime.strptime(
        f'{(today.shift(days=7)).ceil("week"):YYYY-MM-DD}', "%Y-%m-%d"
    ).date()

    plans = user.plans.filter(date__range=[start_date, end_date])
    targets = user.targets.filter(date__range=[start_date, end_date])
    diaries = user.diaries.filter(date__range=[month_start_date, month_end_date])

    week_target, next_week_target, month_target, next_month_target = [], [], [], []
    week_plan, next_week_plan,  month_plan, next_month_plan = [], [], [], []
    month_diary, week_diary = [], []

    for plan in plans:
        if plan.date >= month_start_date and plan.date <= month_end_date:
            month_plan.append({
                "status": plan.done,
                "data": plan.title,
                "id": plan.id,
                "user_id": plan.author.id,
            })
        if plan.date >= next_month_start_date and plan.date <= next_month_end_date:
            next_month_plan.append({
                "status": plan.done,
                "data": plan.title,
                "id": plan.id,
                "user_id": plan.author.id,
                })
        if plan.date >= week_start_date and plan.date <= week_end_date:
            week_plan.append({
                "status": plan.done,
                "data": plan.title,
                "id": plan.id,
                "user_id": plan.author.id,
                })
        if plan.date >= next_week_start_date and plan.date <= next_week_end_date:
            next_week_plan.append({
                "status": plan.done,
                "data": plan.title,
                "id": plan.id,
                "user_id": plan.author.id,
            })

    for target in targets:
        if target.date >= month_start_date and target.date <= month_end_date:
            month_target.append({
                "status": target.done,
                "data": target.title,
                "id": target.id,
                "user_id": target.author.id,
            })
        if target.date >= next_month_start_date and target.date <= next_month_end_date:
            next_month_target.append({
                "status": target.done,
                "data": target.title,
                "id": target.id,
                "user_id": target.author.id,
            })
        if target.date >= week_start_date and target.date <= week_end_date:
            week_target.append({
                "status": target.done,
                "data": target.title,
                "id": target.id,
                "user_id": target.author.id,
            })
        if target.date >= next_week_start_date and target.date <= next_week_end_date:
            next_week_target.append({
                "status": target.done,
                "data": target.title,
                "id": target.id,
                "user_id": target.author.id,
            })

    for diary in diaries:
        if diary.date >= month_start_date and diary.date <= month_end_date:
            month_diary.append({
                "conclusion": diary.conclusion,
                "achievements": diary.achievements,
                "good_things": diary.good_things,
                "id": diary.id,
                "user_id": diary.author,
            })
        if diary.date >= week_start_date and diary.date <= week_end_date:
            week_diary.append({
                "conclusion": diary.conclusion,
                "achievements": diary.achievements,
                "good_things": diary.good_things,
                "id": diary.id,
                "user_id": diary.author,
            })

    result = {
        "week_plan": week_plan,
        "next_week_plan": next_week_plan,
        "month_plan": month_plan,
        "next_month_plan": next_month_plan,
        "week_target": week_target,
        "next_week_target": next_week_target,
        "month_target": month_target,
        "next_month_target": next_month_target,
        "month_diary": month_diary,
        "week_diary": week_diary,
    }

    return result


@api_view(['GET'])
def results(request):
    # user_id = int(request.POST["user_id"])
    # user = get_object_or_404(User, id=user_id)
    result = get_results(request.user)

    return Response(result)


class TargetViewSet(viewsets.ModelViewSet):
    serializer_class = TargetSerializer

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return user.targets.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PlanViewSet(viewsets.ModelViewSet):
    serializer_class = PlanSerializer

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return user.plans.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class DiaryViewSet(viewsets.ModelViewSet):
    serializer_class = PlanSerializer

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return user.diaries.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Конец блока Итогов

##############################################################################

# Начало блока Списков

def get_lists(user):
    my_lists = user.lists.all()

    books, films, travels, wishes  = [], [], [], []

    for my_list in my_lists:
        if my_list.type == ListType.objects.filter(slug="books")[0]:
            books.append({
                "id": my_list.id,
                "data": my_list.title,
                "status": my_list.done,
                "user_id": my_list.author.id,
                "title_list": my_list.title,
            })
        elif my_list.type == ListType.objects.filter(slug="films")[0]:
            films.append({
                "id": my_list.id,
                "data": my_list.title,
                "status": my_list.done,
                "user_id": my_list.author.id,
                "title_list": my_list.title,
            })
        elif my_list.type == ListType.objects.filter(slug="travels")[0]:
            travels.append({
                "id": my_list.id,
                "data": my_list.title,
                "status": my_list.done,
                "user_id": my_list.author.id,
                "title_list": my_list.title,
            })
        elif my_list.type == ListType.objects.filter(slug="wishes")[0]:
            wishes.append({
                "id": my_list.id,
                "data": my_list.title,
                "status": my_list.done,
                "user_id": my_list.author.id,
                "title_list": my_list.title,
            })

    result = {
        "books": books,
        "films": films,
        "travels": travels,
        "wishes": wishes,
    }

    return result


@api_view(['GET'])
def lists(request):
    user = get_object_or_404(User, username=request.user)
    result = get_lists(user)

    return Response(result)


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = ListSerializer

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return MyList.objects.filter(author=user, type=ListType.objects.filter(slug="books")[0])

    def perform_create(self, serializer):
        user = get_object_or_404(User, username=self.request.user)
        serializer.save(author=user, type=ListType.objects.filter(slug="books")[0])

class FilmViewSet(viewsets.ModelViewSet):
    serializer_class = ListSerializer

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return MyList.objects.filter(author=user, type=ListType.objects.filter(slug="films")[0])

    def perform_create(self, serializer):
        user = get_object_or_404(User, username=self.request.user)
        serializer.save(author=user, type=ListType.objects.filter(slug="films")[0])

class WishViewSet(viewsets.ModelViewSet):
    serializer_class = ListSerializer

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return MyList.objects.filter(author=user, type=ListType.objects.filter(slug="wishes")[0])

    def perform_create(self, serializer):
        user = get_object_or_404(User, username=self.request.user)
        serializer.save(author=user, type=ListType.objects.filter(slug="wishes")[0])

class TravelViewSet(viewsets.ModelViewSet):
    serializer_class = ListSerializer

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return MyList.objects.filter(author=user, type=ListType.objects.filter(slug="travels")[0])

    def perform_create(self, serializer):
        user = get_object_or_404(User, username=self.request.user)
        serializer.save(author=user, type=ListType.objects.filter(slug="travels")[0])

# Конец блока Списков

##############################################################################

# Начало блока Ценностей

def get_values(user):
    my_values = user.values.all()
    my_algorithms = user.algorithms.all()

    values_list, principles, quotes = [], [], []
    my_algorithms_business, my_algorithms_relationships = [], []

    for value in my_values:
        if value.type == ValueType.objects.filter(slug="values")[0]:
            values_list.append({
                "id": value.id,
                "data": value.title,
                "user_id": value.author.id,
            })
        elif value.type == ValueType.objects.filter(slug="principles")[0]:
            principles.append({
                "id": value.id,
                "data": value.title,
                "user_id": value.author.id,
            })
        elif value.type == ValueType.objects.filter(slug="quotes")[0]:
            quotes.append({
                "id": value.id,
                "data": value.title,
                "user_id": value.author.id,
            })

    for algorithm in my_algorithms:
        if algorithm.type == AlgorithmType.objects.filter(slug="business")[0]:
            my_algorithms_business.append({
                "id": algorithm.id,
                "data": algorithm.title,
                "user_id": algorithm.author.id,
            })
        elif algorithm.type == AlgorithmType.objects.filter(slug="relationships")[0]:
            my_algorithms_relationships.append({
                "id": algorithm.id,
                "data": algorithm.title,
                "user_id": algorithm.author.id,
            })


    result = {
        "values": values_list,
        "principles": principles,
        "quotes": quotes,
        "algorithms_business": my_algorithms_business,
        "algorithms_relationships": my_algorithms_relationships,
    }

    return result


@api_view(['GET'])
def values(request):
    user = get_object_or_404(User, username=request.user)
    result = get_values(user)

    return Response(result)


class ValueViewSet(viewsets.ModelViewSet):
    serializer_class = ValueSerializer

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return Value.objects.filter(author=user, type=ValueType.objects.filter(slug="values")[0])

    def perform_create(self, serializer):
        user = get_object_or_404(User, username=self.request.user)
        serializer.save(author=user, type=ValueType.objects.filter(slug="values")[0])


class PrincipleViewSet(viewsets.ModelViewSet):
    serializer_class = ValueSerializer

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return Value.objects.filter(author=user, type=ValueType.objects.filter(slug="principles")[0])

    def perform_create(self, serializer):
        user = get_object_or_404(User, username=self.request.user)
        serializer.save(author=user, type=ValueType.objects.filter(slug="principles")[0])


class QuoteViewSet(viewsets.ModelViewSet):
    serializer_class = ValueSerializer

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return Value.objects.filter(author=user, type=ValueType.objects.filter(slug="quotes")[0])

    def perform_create(self, serializer):
        user = get_object_or_404(User, username=self.request.user)
        serializer.save(author=user, type=ValueType.objects.filter(slug="quotes")[0])


class AlgorithmBusinessViewSet(viewsets.ModelViewSet):
    serializer_class = AlgorithmSerializer

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return Algorithm.objects.filter(author=user, type=AlgorithmType.objects.filter(slug="business")[0])

    def perform_create(self, serializer):
        user = get_object_or_404(User, username=self.request.user)
        serializer.save(author=user, type=AlgorithmType.objects.filter(slug="business")[0])


class AlgorithmRelationshipsViewSet(viewsets.ModelViewSet):
    serializer_class = AlgorithmSerializer

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return Algorithm.objects.filter(author=user, type=AlgorithmType.objects.filter(slug="relationships")[0])

    def perform_create(self, serializer):
        user = get_object_or_404(User, username=self.request.user)
        serializer.save(author=user, type=AlgorithmType.objects.filter(slug="relationships")[0])


# Конец блока Ценностей

##############################################################################

# Начало блока Мои цели

def get_goals(user):
    my_goals = user.my_goals.all()

    two_mounth, six_mounth, one_years = [], [], []
    for my_goal in my_goals:
        if my_goal.type == GoalType.objects.filter(slug="two_mounth")[0]:
            two_mounth.append({
                "id": my_goal.id,
                "data": my_goal.text,
                "image": my_goal.image,
                "user_id": my_goal.author.id,
            })
        elif my_goal.type == GoalType.objects.filter(slug="six_mounth")[0]:
            six_mounth.append({
                "id": my_goal.id,
                "data": my_goal.text,
                "image": my_goal.image,
                "user_id": my_goal.author.id,
            })
        elif my_goal.type == GoalType.objects.filter(slug="one_years")[0]:
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
    user = get_object_or_404(User, username=request.user)
    result = get_goals(user)

    return Response(result)


class Two_MViewSet(viewsets.ModelViewSet):
    serializer_class = GoalSerializer

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return MyGoals.objects.filter(
            author=user, type=GoalType.objects.filter(slug="two_mounth")[0])

    def perform_create(self, serializer):
        user = get_object_or_404(User, username=self.request.user)
        serializer.save(
            author=user, type=GoalType.objects.filter(slug="two_mounth")[0])


class Six_MViewSet(viewsets.ModelViewSet):
    serializer_class = GoalSerializer

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return MyGoals.objects.filter(
            author=user, type=GoalType.objects.filter(slug="six_mounth")[0])

    def perform_create(self, serializer):
        user = get_object_or_404(User, username=self.request.user)
        serializer.save(
            author=user, type=GoalType.objects.filter(slug="six_mounth")[0])


class One_yearsViewSet(viewsets.ModelViewSet):
    serializer_class = GoalSerializer

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return MyGoals.objects.filter(
            author=user, type=GoalType.objects.filter(slug="one_years")[0])

    def perform_create(self, serializer):
        user = get_object_or_404(User, username=self.request.user)
        serializer.save(
            author=user, type=GoalType.objects.filter(slug="one_years")[0])

# Конец блока Мои цели

##############################################################################
