# myapp/views.py
from django.http import JsonResponse
import datetime
import pytz

def get_info(request):
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')

    current_day = datetime.datetime.now(pytz.utc).strftime('%A')

    utc_time = datetime.datetime.now(pytz.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    github_file_url = "https://github.com/Crewseefix/HNG-Backend-Stage-One-Task/blob/main/app/views.py"
    github_repo_url = "https://github.com/Crewseefix/HNG-Backend-Stage-One-Task"

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return JsonResponse(response_data)
