from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Team, Activity, Workout, LeaderboardEntry
from bson import ObjectId

# Helper to convert ObjectId to string
class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value) if isinstance(value, ObjectId) else value
    def to_internal_value(self, data):
        return ObjectId(data)

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    id = ObjectIdField(source='_id', read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class TeamSerializer(serializers.ModelSerializer):
    id = ObjectIdField(source='_id', read_only=True)
    members = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Team
        fields = ['id', 'name', 'members', 'created_at']

class ActivitySerializer(serializers.ModelSerializer):
    id = ObjectIdField(source='_id', read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration', 'distance', 'calories', 'date']

class WorkoutSerializer(serializers.ModelSerializer):
    id = ObjectIdField(source='_id', read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Workout
        fields = ['id', 'user', 'name', 'description', 'date']

class LeaderboardEntrySerializer(serializers.ModelSerializer):
    id = ObjectIdField(source='_id', read_only=True)
    user = UserSerializer(read_only=True)
    team = TeamSerializer(read_only=True)
    class Meta:
        model = LeaderboardEntry
        fields = ['id', 'user', 'score', 'team']
