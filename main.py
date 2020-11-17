# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from grammar.Chromosome import Chromosome
from grammar.Grammar import Grammar
from grammar.Population import Population


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    pop = Population()
    pop.chromosomes[0]

    print(Grammar(Chromosome(pop.chromosomes[0].get_array(), "X", pop.chromosomes[0].size), 3, "X").grammar())
    pop.generation()
    print(Grammar(Chromosome(pop.chromosomes[0].get_array(), "X", pop.chromosomes[0].size), 3, "X").grammar())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
