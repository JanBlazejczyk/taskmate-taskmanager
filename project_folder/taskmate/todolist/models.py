from django.db import models


# Create your models here.
class TaskList(models.Model):
    # you pass the maximum length of characters
    task = models.CharField(max_length=300)
    # you pass the default value
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task + ' - ' + str((self.done))
