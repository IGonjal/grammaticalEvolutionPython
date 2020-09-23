from math import sin, cos
import sys
import Chromosome


class Grammar:

    __wholeChromosome = None
    _chromosome =[]  # [3, 2, 1, 0, 0, 2, 2]  # vale 4
    # [0, 1, 0, 0, 0, 0, 1, 0, 0, 9]  # vale 2

    __theVariable = 3.0
    __theVariableName = "X"

    __maxGeneExpression = 4
    __maxGeneUnary = 3
    __maxGeneBinary = 3

    """
    s::= <expr>
    
    <expr> ::=
          (<expr> <op> <expr>       (0)
        | <val>                     (1)
        | <var>                     (2)
        | <unary_op> <expr>         (3)
    -----------------------------------
    <unary_op> ::=
          sin <exp>
        | cos <exp>
        | <exp> ^2
    -----------------------------------
    <op> ::=
          +                         (0)
        | -                         (1)
        | *                         (2)
    -----------------------------------
    <val> ::=
          <int>                     (0)
        | <int> . <int>             (1)
    -----------------------------------
    <int> ::=
          <num> |                   (0)
          <num> <int>               (1)
    -----------------------------------
    <num> ::= 
          0                         (0)
        | 1                         (1)
        | 2                         (2)
        | 3                         (3)
        | 4                         (4)
        | 5                         (5)
        | 6                         (6)
        | 7                         (7)
        | 8                         (8)
        | 9                         (9)
    <var> ::=
        x                           (0)
    """

    def __init__(self, chromosome=Chromosome(), the_var=3, var_name="X"):
        self.__theVariable = the_var
        self.__theVariableName = var_name
        if isinstance(chromosome, Chromosome):
            self.__wholeChromosome = chromosome
            self.__chromosome = chromosome.get_array()
        elif isinstance(chromosome, list) \
                and all(isinstance(chromosome, int)) \
                and len(chromosome) > 2:
            self.__wholeChromosome = Chromosome(chromosome)
            self.__chromosome = chromosome
        else:
            self.__wholeChromosome = Chromosome()
            self._chromosome = self.__wholeChromosome.get_array()

    def grammar(self):
        try:
            ret = self._expr(-1)
            self.__wholeChromosome.set_result(ret[1])
            self.__wholeChromosome.set_human_grammar(ret[2])
            return ret[1], ret[2]
        except ValueError as error:
            return sys.float_info.max, "**Error, chromosome too big**"

    def _expr(self, i):
        i = i + 1
        if i >= len(self._chromosome):
            raise ValueError('the chromosome is too big')
        switch = self._chromosome[i] % self.__maxGeneExpression
        if switch == 0:
            return self._binary_op(i)
        elif switch == 1:
            return self._value(i)
        elif switch == 2:
            return self._variable(i)
        elif switch == 3:
            return self._unary_op(i)

    def _binary_op(self, i):
        if i + 1 >= len(self._chromosome):
            raise ValueError('the chromosome is too big')
        tmp = self._expr(i)
        expr1 = tmp[1]
        str1 = tmp[2]
        i = tmp[0] + 1
        switch = self._chromosome[i] % self.__maxGeneBinary
        tmp = self._expr(i)
        expr2 = tmp[1]
        str2 = tmp[2]
        i = tmp[0]

        if switch == 0:
            return i, expr1 + expr2, "( " + str1 + " + " + str2 + " )"
        elif switch == 1:
            return i, expr1 - expr2, "( " + str1 + " - " + str2 + " )"
        elif switch == 2:
            return i, expr1 * expr2, "( " + str1 + " * " + str2 + " )"

    def _unary_op(self, i):
        i = i + 1
        if i >= len(self._chromosome):
            raise ValueError('the chromosome is too big')
        switch = self._chromosome[i] % self.__maxGeneUnary
        ret = self._expr(i)
        if switch == 0:
            return ret[0], sin(ret[1]), "sin(" + ret[2] + ")"
        elif switch == 1:
            return ret[0], cos(ret[1]), "cos(" + ret[2] + ")"
        elif switch == 2:
            return ret[0], ret[1] ** 2, "(" + ret[2] + " ^ 2)"

    def _value(self, i):
        ret = self._number_generator(i)
        return ret[0], float(ret[1]), ret[1]

    def _number_generator(self, i):
        i = i + 1
        if i >= len(self._chromosome):
            raise ValueError('the chromosome is too big')
        tmp = self._integer_number_generator(i)
        if self._chromosome[i] % 2 == 0:
            return tmp[0], tmp[1]
        i = tmp[0]
        ret = tmp[1] + "."
        tmp = self._integer_number_generator(i)
        ret = ret + tmp[1]
        return tmp[0], ret

    def _integer_number_generator(self, i):
        i = i + 1
        if i >= len(self._chromosome):
            raise ValueError('the chromosome is too big')
        tmp = self._number_digit_generator(i)
        if self._chromosome[i] % 2 == 0:
            return tmp[0], tmp[1]
        ret = tmp[1]
        tmp = self._integer_number_generator(tmp[0])
        ret = ret + tmp[1]
        return tmp[0], ret

    def _number_digit_generator(self, i):
        i = i + 1
        if i >= len(self._chromosome):
            raise ValueError('the chromosome is too big')
        return i, str(self._chromosome[i] % 10)

    def _variable(self, i):
        if i + 1 >= len(self._chromosome):
            raise ValueError('the chromosome is too big')
        return i + 1, self.__theVariable, self.__theVariableName
