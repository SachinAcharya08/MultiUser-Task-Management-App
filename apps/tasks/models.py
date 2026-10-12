from django.db import models
from config import settings
import uuid

class Tasks(models.Model):

    class Status(models.TextChoices):
        TODO = "TODO", "To Do"
        IN_PROGRESS = "IN_PROGRESS", "In Progress"
        COMPLETED = "COMPLETED", "Completed"
        CANCELLED = "CANCELLED", "Cancelled"

    class Priority(models.TextChoices):
        LOW="LOW", "low"
        MEDIUM="MEDIUM", "medium"
        HIGH="HIGH", "high"
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title=models.CharField(max_length=100)
    desc=models.TextField(blank=True,max_length=250)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True)
    status=models.CharField(max_length=20,choices=Status.choices,default=Status.TODO)
    priority=models.CharField(max_length=10,choices=Priority.choices,default=Priority.MEDIUM)
    due_at=models.DateTimeField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["status"]),
            models.Index(fields=["priority"]),
            models.Index(fields=["due_at"])
        ]
        db_table= "Tasks"
    def __str__(self):
        return f"{self.title} ({self.status})"
