from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# first value is stored in the DB and second displayed to user
CONDITIONS = (
	(0, 'Ecstatic'),
	(5, 'Passionate'),
	(10, 'Happy'),
	(15, 'Bored'),
	(20, 'Pessimistic'),
	(25, 'Frustated'),
	(26, 'Tired'),
	(27, 'Hungry'),
	(30, 'Disappointed'),
	(35, 'Pessimistic'),
	(40, 'Angry'),
	(45, 'Guilty'),
	(50, 'Fear'),
	(55, 'Grief'),
	(60, 'Despair'),
	(65, 'Jealous'),
	(70, 'Pessimistic'),
	(75, 'Worried'),
	(75, 'Paranoid'),
)


class Thought(models.Model):
	user = models.ForeignKey(User, related_name='thoughts', on_delete=models.CASCADE)
	recorded_at = models.DateTimeField(default=timezone.now, editable=False)
	condition = models.IntegerField(choices=CONDITIONS)
	notes = models.TextField(default='', blank=True)

	def __str__(self):
		return '{}: {}'.format(self.recorded_at.strftime("%Y-%m-%d %H:%M:%S"), self.get_condition_display())