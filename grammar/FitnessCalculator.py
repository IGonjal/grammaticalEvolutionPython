import math
import json

from grammar.Population import Population
from grammar.Grammar import Grammar


class FitnessCalculator:
    __population = None
    __variable_value = None
    __variable_name = None
    __dataset = None

    def __init__(self, population, variable_value, variable_name="X", dataset="./datasets/XX"):
        self.__variable_value = variable_value
        self.__variable_name = variable_name
        self.__dataset = json.loads(open(dataset, "r").read())
        if isinstance(population, Population):
            self.__population = population

    def set_population(self, population):
        if isinstance(population, Population):
            self.__population = population

    def set_variable_value(self, variable_value):
        self.__variable_value = variable_value

    def calculate_result(self):
        for v in self.__population.chromosomes:
            Grammar(v, self.__variable_value, self.__variable_name).grammar()

    def get_expected_result(self, index):
        print(self.__dataset["values"][str(index)])
        return self.__dataset["values"][str(index)]

    def calculate_fitness(self):
        for v in self.__population.chromosomes:
            v.set_fitness(math.sqrt(v.get_result ** 2 + self.get_expected_result(self.__variable_value) ** 2))
