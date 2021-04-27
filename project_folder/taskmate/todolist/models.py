from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TaskList(models.Model):
    # you pass the maximum length of characters
    task = models.CharField(max_length=300)
    # you pass the default value
    done = models.BooleanField(default=False)
    # we add a column to the task row in the database table,
    # it takes values for Users field that's why it's a Foreign key
    # here we say that an owner is a User that creates the task
    # and that all the tasks created by the user needs to be deleted
    # if we delete a user
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.task + ' - ' + str((self.done))
