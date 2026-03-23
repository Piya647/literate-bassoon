from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Team, Activity, Workout, LeaderboardEntry

User = get_user_model()

class APITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_api_root(self):
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('workouts', response.data)
        self.assertIn('leaderboard', response.data)

    def test_create_team(self):
        response = self.client.post(reverse('team-list'), {'name': 'Team A'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_activity(self):
        response = self.client.post(reverse('activity-list'), {
            'activity_type': 'Running',
            'duration': 30,
            'user': self.user.id
        })
        self.assertIn(response.status_code, [status.HTTP_201_CREATED, status.HTTP_400_BAD_REQUEST])

    def test_create_workout(self):
        response = self.client.post(reverse('workout-list'), {
            'name': 'Morning Workout',
            'user': self.user.id
        })
        self.assertIn(response.status_code, [status.HTTP_201_CREATED, status.HTTP_400_BAD_REQUEST])

    def test_leaderboard(self):
        LeaderboardEntry.objects.create(user=self.user, score=100)
        response = self.client.get(reverse('leaderboardentry-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
