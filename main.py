from person import Person
from project import Project
from formula import formula_func

def read(path):
    f =  open(path)
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
    
    return people, projects


people, projects = read("a_an_example.in.txt")


def run_file(people : list, projects : list, coefficients : list) -> float:
    # Get value for each project
    # Run first project
    values = [(formula_func(coefficients, project), project) 
                    for project in projects]
    
    values = values.sort(lambda x : x[0])

    projects = [each[1] for each in values]

    days = 0
    

    # Loop
    # Run until a project finishes
    # Check if can assign, assign if worth
    # Remove people assigned



