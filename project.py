from person import Person

class Project:

	def __init__(self, info : str):
		info = info.split()
		self._roles = dict()
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
		self._roles[roleName] = level

	def assign(self, person : Person):
		self._assigned[person.name] = person


