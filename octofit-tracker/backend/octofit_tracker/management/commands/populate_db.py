from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Users
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel)
        captain = User.objects.create(email='captain@marvel.com', name='Captain America', team=marvel)
        batman = User.objects.create(email='batman@dc.com', name='Batman', team=dc)
        superman = User.objects.create(email='superman@dc.com', name='Superman', team=dc)

        # Activities
        Activity.objects.create(name='Running', user=ironman, duration=30, date='2025-10-01')
        Activity.objects.create(name='Swimming', user=captain, duration=45, date='2025-10-02')
        Activity.objects.create(name='Cycling', user=batman, duration=60, date='2025-10-03')
        Activity.objects.create(name='Flying', user=superman, duration=120, date='2025-10-04')

        # Workouts
        Workout.objects.create(name='Pushups', description='Upper body', user=ironman, date='2025-10-01')
        Workout.objects.create(name='Situps', description='Core', user=captain, date='2025-10-02')
        Workout.objects.create(name='Squats', description='Legs', user=batman, date='2025-10-03')
        Workout.objects.create(name='Bench Press', description='Strength', user=superman, date='2025-10-04')

        # Leaderboard
        Leaderboard.objects.create(name='Marvel Leaderboard', team=marvel, score=100)
        Leaderboard.objects.create(name='DC Leaderboard', team=dc, score=120)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
