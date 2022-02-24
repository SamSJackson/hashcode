from math import floor
from typing import List, Dict
from typing import Dict
from person import Person


class Project:

    def __init__(self, info: str):
        info = info.split()
        self._requirements: Dict[str, int] = dict()
        self._assigned: Dict[str, Person] = dict()
        self._name = info[0]
        self._duration = int(info[1])
        self._score = int(info[2])
        self._expiryDate = int(info[3])
        self._num_roles = int(info[4])
        self._remaining = self._duration

    def __str__(self):
        return self._name

    @property
    def finished(self):
        return self._remaining == 0

    @property
    def averageLevel(self):
        total = 0
        for _, level in self._requirements.items():
            total += level
        return total / len(self._requirements)

    @property
    def score(self):
        return self._score

    @property
    def duration(self):
        return self._duration

    @property
    def importance(self):
        return (self._score / self._duration) - self.minStartDate

    @property
    def minStartDate(self):
        return self._expiryDate - self._duration

    @property
    def num_roles(self):
        return self._num_roles

    def addRole(self, role: str):
        roleName, level = role.split()
        level = int(level)
        self._requirements[roleName] = level

    def assign(self, person: Person, role: str) -> bool:
        if not role in self._requirements:
            return False

        self._assigned[role] = person
        return True

    def start(self):
        self._remaining -= 1
        for each in self._assigned.values():
            each.toggleUnavailable()

    def nextDay(self):
        self._remaining -= 1
        if self._remaining == 0:
            for each in self._assigned.values():
                each.toggleUnavailable()
            return True
        return False

    def meetsRequirements(self) -> bool:
        for skill, level in self._requirements.items():
            if not skill in self._assigned:
                return False

        person = self._assigned[skill]
        has_skill = person.hasSkill(skill, level)
        if has_skill == "no":
            return False
        elif has_skill == "yes":
            pass
        else:
            # they need a mentor
            mentor_available = [person.hasSkill(skill, level) == "yes" for person in self._assigned].any()
            if not mentor_available:
                return False

        return True
    def canRun(self):
        return all([each.available for each in self._assigned.values()])
