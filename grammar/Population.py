from grammar.Chromosome import Chromosome
from grammar.Grammar import Grammar

import random


class Population:
    chromosomes = [None]
    var = 13

    def __init__(self, size=512):

        self.chromosomes = [None] * size
        for i in range(size):
            self.chromosomes[i] = Chromosome()

    def generation(self):
        # elitismo
        # seleccion
            # Ruleta
            # Torneo
        self.tournament()

        # cruce
        self.crossover()
        # mutación y descifrado
        self.mutation_and_decipher()
        # calcula fitness
        self.fitness()
        # ordenación
        self.chromosomes.sort(key=lambda ch: ch.get_fitness())

        return self.chromosomes[0]

    def crossover(self):
        random.shuffle(self.chromosomes)
        for i in range(0, len(self.chromosomes) - 1, 2):
            self.chromosomes[i].crossover(self.chromosomes[i + 1])
        random.shuffle(self.chromosomes)

    def mutation_and_decipher(self):
        for chromosome in self.chromosomes:
            chromosome.mutate()
            Grammar(chromosome, self.var, "X")

    def selection(self):
        random.shuffle(self.chromosomes)
        for i in range(0, len(self.chromosomes) - 1, 2):
            self.chromosomes[i]




