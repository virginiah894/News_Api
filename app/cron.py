from .models import *
def my_cron_job():
    UpVote.objects.all().update(rego_update=UpVote().rego_update)

    