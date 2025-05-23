from django.db import models

from .models_base import *
from django.contrib.auth.models import User
from helpers.common import *

# Create your models here.

class GeneratedApp(BaseModel):
    
    user          = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    user_ip       = models.CharField(max_length=256, blank=True, null=True, default=None)
    task_id       = models.CharField(max_length=256)
    backend       = models.CharField(max_length=256, blank=True, null=True)
    task_log      = models.TextField(blank=True, null=True, default=None)

    api_key       = models.CharField(max_length=512, blank=True, null=True, default=None)

    task_state    = models.CharField(max_length=256, default=COMMON.STARTING)
    task_result   = models.CharField(max_length=256, default=COMMON.STARTING)
    
    generated_at  = models.DateTimeField(auto_now_add=True)
    downloaded_at = models.DateTimeField(null=True, blank=True)
    deleted_at    = models.DateTimeField(null=True, blank=True)
    gh_repo       = models.CharField(max_length=512, blank=True, null=True, default=None)
    deleted       = models.BooleanField(default=False)

    def __str__(self):
        if self.user:
            return f"{self.id} - {self.backend}, user={ str(self.user.username) } - {self.task_result}: {str(self.task_id)}, REPO: {self.gh_repo}" 
        else:
            return f"{self.id} - {self.backend}, IP={ str(self.user_ip) } - {self.task_result}: {str(self.task_id)}, REPO: {self.gh_repo}" 