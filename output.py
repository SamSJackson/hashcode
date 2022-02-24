from typing import List
from person import Person


def outputFile(projects: List[Person], filename: str):
    with open(filename, 'w+') as f:
        f.write(str(len(projects)) + '\n')
        for i in range(len(projects)):
            f.write(str(projects[i]) + '\n')
            names = ""
            for role, name in projects[i]._assigned.items():
                names += str(name) + " "
            f.write(names + '\n')
