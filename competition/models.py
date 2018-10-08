from django.db import models


GAME_TYPES = (
	('TT', 'TT'),
	('FS', 'foosball'),
)

LOCATION_CHOICES = (
	('H', 'Hostle'),
	('O', 'Office'),
)


class Player(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Competition(models.Model):
	title = models.CharField(max_length=50,null=True,blank=True)
	type = models.CharField(max_length=10, choices=GAME_TYPES)
	place = models.CharField(max_length=10,choices=LOCATION_CHOICES)


class Team(models.Model):
	player1 = models.ForeignKey(Player,on_delete=models.CASCADE, related_name="first")
	player2 = models.ForeignKey(Player,on_delete=models.CASCADE, related_name="second")
	tt_points = models.IntegerField(default=0,blank=True,null=True)
	foosball_points = models.IntegerField(default=0,blank=True,null=True)

	def __str__(self):
		return self.player1.__str__() + ',' + self.player2.__str__()


class Match(models.Model):
	team1 = models.ForeignKey(Team,on_delete=models.CASCADE, related_name="team1")
	team2 = models.ForeignKey(Team,on_delete=models.CASCADE, related_name="team2")
	team1_score = models.IntegerField(default=0)
	team2_score = models.IntegerField(default=0)

	game = models.CharField(max_length=10,choices=GAME_TYPES)
	comptn = models.ForeignKey(Competition,on_delete=models.CASCADE,blank=True,null=True,default=None)

