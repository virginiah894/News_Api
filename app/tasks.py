from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import *

import time


@shared_task
def refresh_upvote(upvotes):
    upvotes = Post.count_upvotes