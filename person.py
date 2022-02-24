class Person:
	def __init__(self, name : str):
		self._name = name
		self._skills = dict()

	def __str__(self):
		return self._name

	@property
	def name(self):
		return self._name	

	def addSkills(self, skill : str):
		skillName, level = skill.split()
		level = int(level)
		self._skills[skillName] = level

	def upgradeSkill(self, skillname : str):
		self._skills[skillname] = self._skills.get(skillname, 0) + 1


