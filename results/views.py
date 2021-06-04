from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
import requests

User = get_user_model()


@login_required
def index(request):
    user = get_object_or_404(User, username=request.user)
    params = {
        "user_id": user.id,
    }

    result = requests.get(
        "http://localhost:8000/api/v1/all/",
        data=params,
    ).json()
    

    return render(
         request,
         "index.html",
         {
             "month_plan": result.get("month_plan"),
             "next_month_plan": result.get("next_month_plan"),
             "week_plan": result.get("week_plan"),
             "next_week_plan": result.get("next_week_plan"),
             "month_target": result.get("month_target"),
             "next_month_target": result.get("next_month_target"),
             "week_target": result.get("week_target"),
             "next_week_target": result.get("next_week_target"),
         }
     )