import random
import sys


class Chromosome:

    mutationRatio = 0.1
    maxInt = 511
    __chromosome = []
    result = 0.0
    fitness = sys.float_info.max
    humanGrammar= ""

    def __init__(self, chromosome=[], var_name="X", size_for_new_chromosome=255):
        self.__theVariableName = var_name
        self.fitness = sys.float_info.max
        if len(chromosome) > 2:
            self.__chromosome = chromosome
        else:
            chromosome = [None] * size_for_new_chromosome
            for a in range(len(chromosome)):
                chromosome[a] = random.randint(0, 254)
            self._chromosome = chromosome

    def get_array(self):
        return self.__chromosome

    def mutate(self):
        if random.random() < self.mutationRatio:
            self.__chromosome[random.randint(0, len(self.__chromosome) - 1)] =  \
                random.randint(0, self.maxInt)

    def crossover(self, other, init_point=None):
        if isinstance(other, Chromosome):
            if init_point is None:
                init_point = random(1, len(self.__chromosome) - 1)
            for i in range(init_point, len(self.__chromosome) - 1, 1):
                aux = self.__chromosome[i]
                self.__chromosome[i] = other.__chromosome[i]
                other.__chromosome[i] = aux

    def set_fitness(self, fitness):
        self.fitness = fitness

    def get_fitness(self):
        return self.fitness

    def set_result(self, result):
        self.result = result

    def get_result(self):
        return self.result

    def get_human_grammar(self):
        return self.humanGrammar

    def set_human_grammar(self, human=""):
        self.humanGrammar = human
