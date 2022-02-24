from math import floor

from numpy import true_divide
from person import Person

class Project:

	def __init__(self, info : str):
		info = info.split()
		self._requirements = dict()
		self._assigned = dict()
		self._name = info[0]
		self._duration = int(info[1])
		self._score = int(info[2])
		self._expiryDate = int(info[3])
		self._num_roles = int(info[4])

	def __str__(self):
		return self._name

	@property
	def num_roles(self):
		return self._num_roles

	def addRole(self, role : str):
		roleName, level = role.split()
		level = int(level)
		self._requirements[roleName] = level

	def assign(self, person : Person, role: str) -> bool:
		if not role in self._requirements:
			return False

		self._assigned[role] = person
		return True

	def run(self, startTime):
		"""returns score"""
		for role in self._requirements:
			pass
		finish = self._duration + startTime
		delta = self._expiryDate - finish
		if delta >= 1:
			return self._score
		else:
			return floor(0, self._score + delta)

