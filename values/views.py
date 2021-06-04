from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
import requests

User = get_user_model()


@login_required
def values(request):
    user = get_object_or_404(User, username=request.user)
    params = {
        "user_id": user.id,
    }

    result = requests.get(
        "http://localhost:8000/api/v1/values/",
        data=params,
        headers={'Authorization': 'Bearer ' + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI0ODg2MzkwLCJqdGkiOiI3ZTIxZGZmY2YzOGU0YmJlYjNmOWM4NGUxYzYxNWQ2ZCIsInVzZXJfaWQiOjF9._I8CimQyZ2vjcIWwpPfsAZdPfm36_slqDy9fDJ3Cbic'}
    ).json()
    

    return render(
         request,
         "values.html",
         {
             "test": "test"
         }
     )