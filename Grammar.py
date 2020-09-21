from math import sin, cos


class Grammar:
    chromosome = [3, 2, 1, 0, 0, 2, 2]  # vale 4
    # [0, 1, 0, 0, 0, 0, 1, 0, 0, 9]  # vale 2

    theVariable = 3.0
    theVariableName = "X"

    maxGeneValue = 2
    maxGeneExpression = 4
    maxGeneUnary = 3
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
        ret = self.expr(-1)
        return ret[1], ret[2]

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
        str1 = tmp[2]
        i = tmp[0] + 1
        switch = self.chromosome[i] % self.maxGeneBinary
        tmp = self.expr(i)
        expr2 = tmp[1]
        str2 = tmp[2]
        i = tmp[0]

        if switch == 0:
            return i, expr1 + expr2, "( " + str1 + " + " + str2 + " )"
        elif switch == 1:
            return i, expr1 - expr2, "( " + str1 + " - " + str2 + " )"
        elif switch == 2:
            return i, expr1 * expr2, "( " + str1 + " * " + str2 + " )"

    def unary_op(self, i):
        i = i + 1
        switch = self.chromosome[i] % self.maxGeneUnary
        ret = self.expr(i)
        if switch == 0:
            return ret[0], sin(ret[1]), "sin(" + ret[2] + ")"
        elif switch == 1:
            return ret[0], cos(ret[1]), "cos(" + ret[2] + ")"
        elif switch == 2:
            return ret[0], ret[1] ** 2, "(" + ret[2] + " ^ 2)"

    def value(self, i):
        ret = self.number_generator(i)
        return ret[0], float(ret[1]), ret[1]

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
        return i + 1, self.theVariable, self.theVariableName
