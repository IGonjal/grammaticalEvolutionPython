from math import sin, cos


class Grammar:
    valor = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    theVariable = 3.0

    maxGeneValue = 2
    maxGeneExpression = 4
    maxGeneUnary = 2
    maxGeneBinary = 3
    valor2 = [0, 1, 1, 0, 1, 1]  # vale 2

    """
    s::= <expr>
    
    <expr> ::=
          (<expr> <op> <expr>       (0)
        | <val>                     (1)
        | <var>                     (2)
        | <unop> <expr>             (3)
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
          0
        | 1
        | 2
        | 3
        | 4
        | 5
        | 6
        | 7
        | 8
        | 9
    <var> ::=
        x                           (0)
    
    """
    # def __init__(self):

    def grammar(self, var):
        self.theVariable = var
        return self.expr(0).second

    def expr(self, i):
        switch = i % self.maxGeneExpression
        i = i+1
        if switch == 0:
            ret = self.binary_op(i)
            return ret.first + 1, ret.second
        elif switch == 1:
            ret = self.value(i)
            return ret.first + 1, ret.second
        elif switch == 2:
            ret = self.variable(i)
            return ret.first + 1, ret.second
        elif switch == 3:
            ret = self.unary_op(i)
            return ret.first + 1, ret.second

        else:
            ret = self.value(i)
            return ret.first + 1, ret.second

    def binary_op(self, i):
        expr1 = self.expr(i+1).first
        i = expr1.first + 1
        expr2 = self.expr(i + 1)
        switch = i % self.maxGeneBinary
        i = expr2.first + 1
        expr2 = expr2.second
        return {
            0: (i, expr1 + expr2),
            1: (i, expr1 - expr2),
            2: (i, expr1 * expr2)

        }.get(self.value[switch], (i, 1.0))

    def unary_op(self, i):
        ret = self.expr(self, i)
        i = ret.first+1
        return {
            0: (i, sin(ret.second)),
            1: (i, cos(ret.second)),
        }.get(self.value[ret.first] % self.maxGeneUnary, (i, 0))

    def value(self, i):
        ret = self.number_expr_generator(i)
        return ret.first + 1, float(ret.second)
        # if (i % self.maxGeneValue) == 0:
        #     return i+1, 1.0
        # return i+1, 0.1

    def number_expr_generator(self, i):
        i = i+1
        tmp = self.integer_number_generator(i)
        if i == 0:
            return tmp.first + 1, tmp.second
        i = tmp.first + 1
        ret = tmp.second + "."
        tmp = self.integer_number_generator(i)
        ret = ret + tmp.second()
        return tmp.first, ret



    def integer_number_generator(self,i):
        i = i + 1
        tmp = self.number_digit_generator(i)
        i = tmp.first + 1
        if self.valor[i] == 1:
            ret = tmp.first, tmp.second
        tmp = self.numberExprGenerator(tmp.first + 1)
        ret = ret + tmp.second
        return tmp.first, ret

    def number_digit_generator(self, i):
        i = i + 1
        return {
            0: (i, "0"),
            1: (i, "1"),
            2: (i, "2"),
            3: (i, "3"),
            4: (i, "4"),
            5: (i, "5"),
            6: (i, "6"),
            7: (i, "7"),
            8: (i, "8"),
            9: (i, "9")
        }.get(self.value[i] % 10)

    def variable(self, i):
        return i+1, self.theVariable
