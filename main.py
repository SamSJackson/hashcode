from typing import List

from person import Person
from project import Project
from formula import formula_func
from output import outputFile


def read(path):
    f = open(path)
    num_people, num_projects = map(int, f.readline().split())
    people = []
    projects = []
    for _ in range(num_people):
        line = f.readline()
        name, languages = line.split()
        person = Person(name)
        for _ in range(int(languages)):
            person.addSkills(f.readline())
        people.append(person)

    for _ in range(num_projects):
        line = f.readline()
        project = Project(line)
        for _ in range(project.num_roles):
            project.addRole(f.readline())
        projects.append(project)

    f.close()
    return people, projects


people, projects = read("a_an_example.in.txt")


def run_file(people: list, projects: list) -> float:
    # Get value for each project
    # Run first project
    coefficients = [1] * 5
    values = [(formula_func(coefficients, project), project)
              for project in projects]
    values.sort(key=lambda x: x[0])

    projects: List[Project] = [each[1] for each in values]
    for p in projects:
        peeps = people.copy()
        for skill, level in p._requirements.items():
            for person in peeps:
                if person.hasSkill(skill, level):
                    p.assign(person, skill)
                    peeps.remove(person)
                    break

    stillToRun = projects.copy()
    running = []
    finished = []
    days = 0
    i = 0
    while not all([p.finished for p in projects]):
        for each in stillToRun:
            if each.canRun():
                each.start()
                stillToRun.remove(each)
                running.append(each)

        for each in running:
            done = each.nextDay()
            if done:
                print(each._name)
            if done:
                running.remove(each)
                finished.append(each)
    print(len(finished))
    return finished


if __name__ == '__main__':
    people, projects = read("c_collaboration.in.txt")
    finished = run_file(people, projects)
    outputFile(finished, "c.txt")

    # Loop
    # Run until a project finishes
    # Check if can assign, assign if worth
    # Remove people assigned
