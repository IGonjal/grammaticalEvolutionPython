from math import sin, cos


class Grammar:
    chromosome = [0, 1, 0, 0, 1, 0, 1, 0, 0, 1]  # vale 2

    theVariable = 3.0

    maxGeneValue = 2
    maxGeneExpression = 4
    maxGeneUnary = 2
    maxGeneBinary = 3

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
    # def __init__(self):

    def grammar(self):
        return self.expr(-1)[1]

    def expr(self, i):
        i = i + 1
        switch = self.chromosome[i] % self.maxGeneExpression
        if switch == 0:
            return self.binary_op(i)
        elif switch == 1:
            return self.value(i)
        elif switch == 2:
            return self.variable(i)
        elif switch == 3:
            return self.unary_op(i)

    def binary_op(self, i):
        tmp = self.expr(i)
        expr1 = tmp[1]
        i = tmp[0] + 1
        switch = self.chromosome[i] % self.maxGeneExpression
        tmp = self.expr(i)
        expr2 = tmp[1]
        i = tmp[0]

        if switch == 0:
            return i, expr1 + expr2
        elif switch == 1:
            return i, expr1 - expr2
        elif switch == 2:
            return i, expr1 * expr2

    def unary_op(self, i):
        ret = self.expr(i)
        i = ret[0] + 1
        return {
            0: (i, sin(ret.second)),
            1: (i, cos(ret.second)),
            2: (i, ret.second ** 2)
        }.get(self.chromosome[i] % self.maxGeneUnary, (i, 0))

    def value(self, i):
        ret = self.number_generator(i)
        return ret[0], float(ret[1])

    def number_generator(self, i):
        i = i + 1
        tmp = self.integer_number_generator(i)
        if self.chromosome[i] % 2 == 0:
            return tmp[0], tmp[1]
        i = tmp[0]
        ret = tmp[1] + "."
        tmp = self.integer_number_generator(i)
        ret = ret + tmp[1]
        return tmp[0], ret

    def integer_number_generator(self, i):
        i = i + 1
        tmp = self.number_digit_generator(i)
        if self.chromosome[i] % 2 == 0:
            return tmp[0], tmp[1]
        ret = tmp[1]
        tmp = self.integer_number_generator(tmp[0])
        ret = ret + tmp[1]
        return tmp[0], ret

    def number_digit_generator(self, i):
        i = i + 1
        return i, str(self.chromosome[i] % 10)

    def variable(self, i):
        return i + 1, self.theVariable
