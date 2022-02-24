from person import Person
from project import Project

def element_wise_multiply(l1, l2):
	return [l1[i] * l2[i] for i in range(len(l1))]

def formula_func(coefficients : list, project : Project):
	values = element_wise_multiply(coefficients, [project.score, project.minStartDate, 
												project.duration, project.averageLevel, 
												project.num_roles])
	return (values[0] + values[1]) / (values[2] + values[3] + values[4])
	