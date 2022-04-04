from .models import *
def my_cron_job():
    unvote = UpVote.unvote()
    