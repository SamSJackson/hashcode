from typing import List

import main
from project import Project
from person import Person


def outputFile(projects: List[Person], filename: str):
    with open('outputz.txt', 'x+') as f:
        f.write(str(len(projects)) + '\n')
        for i in range(len(projects)):
            f.write(str(projects[i]) + '\n')
            names = ""
            for role, name in projects[i]._assigned.items():
                names += name + " "
            f.write(names + '\n')
