from djongo import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Additional fields can be added here
    pass

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField('User', related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=100)
    duration = models.FloatField()  # in minutes
    distance = models.FloatField(null=True, blank=True)  # in km
    calories = models.FloatField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.activity_type}"

class Workout(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='workouts')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.name}"

class LeaderboardEntry(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='leaderboard_entries')
    score = models.FloatField(default=0)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='leaderboard_entries', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.score}"
