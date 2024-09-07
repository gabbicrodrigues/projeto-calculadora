#!/usr/bin/python3
from antlr4 import *
from CalculadoraLexer import CalculadoraLexer
from CalculadoraParser import CalculadoraParser
from CalculadoraVisitor import CalculadoraVisitor


class CalcVisitor(CalculadoraVisitor):
    def visitExpr(self, ctx:CalculadoraParser.ExprContext):
        result = self.visit(ctx.term(0))  # Processa o primeiro termo
        for i in range(1, len(ctx.term())):
            term = self.visit(ctx.term(i))
            op = ctx.getChild(2*i-1).getText()  # Obtém o operador (+ ou -)
            if op == '+':
                result += term
            elif op == '-':
                result -= term
        return result

    def visitTerm(self, ctx:CalculadoraParser.TermContext):
        result = self.visit(ctx.factor(0))  # Processa o primeiro fator
        for i in range(1, len(ctx.factor())):
            factor = self.visit(ctx.factor(i))
            op = ctx.getChild(2*i-1).getText()  # Obtém o operador (* ou /)
            if op == '*':
                result *= factor
            elif op == '/':
                if factor == 0:
                    print('Erro: divisao por zero!')
                    return 0
                result /= factor
        return result

    def visitFactor(self, ctx:CalculadoraParser.FactorContext):
        if ctx.INT():
            return float(ctx.INT().getText())
        elif ctx.FLOAT():
            return float(ctx.FLOAT().getText())
        elif ctx.ID():
            return 0  # Handle variable lookup if needed
        elif ctx.expr():
            return self.visit(ctx.expr())
        return 0


def calc(line) -> float:
    input_stream = InputStream(line)

    # lexing
    lexer = CalculadoraLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # parsing
    parser = CalculadoraParser(stream)
    tree = parser.expr()

    # use customized visitor to traverse AST
    visitor = CalcVisitor()
    return visitor.visit(tree)



if __name__ == '__main__':
    while True:
        print(">>> ", end='')
        line = input().strip()
        if line.lower() == 'exit':
            break
        if line:  # Only process non-empty input
            try:
                result = calc(line)
                print(result)
            except Exception as e:
                print(f"Error: {e}")