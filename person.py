class Person:
	def __init__(self, name : str):
		self._name = name
		self._skills = dict()

	def __str__(self):
		return self._name

	@property
	def name(self):
		return self._name

	@property
	def skills(self):
		return self._skills

	def hasSkill(self, skill, level):
		cur_level = self._skills.get(skill, 0)
		if cur_level < level-1:
			return "no"
		elif cur_level == level-1:
			return "mentor"
		else:
			return "yes"

	def addSkills(self, skill : str):
		skillName, level = skill.split()
		level = int(level)
		self._skills[skillName] = level

	def upgradeSkill(self, skillname : str):
		self._skills[skillname] = self._skills.get(skillname, 0) + 1


