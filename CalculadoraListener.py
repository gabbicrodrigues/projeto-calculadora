# Generated from Calculadora.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalculadoraParser import CalculadoraParser
else:
    from CalculadoraParser import CalculadoraParser

# This class defines a complete listener for a parse tree produced by CalculadoraParser.
class CalculadoraListener(ParseTreeListener):

    # Enter a parse tree produced by CalculadoraParser#expr.
    def enterExpr(self, ctx:CalculadoraParser.ExprContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#expr.
    def exitExpr(self, ctx:CalculadoraParser.ExprContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#term.
    def enterTerm(self, ctx:CalculadoraParser.TermContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#term.
    def exitTerm(self, ctx:CalculadoraParser.TermContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#factor.
    def enterFactor(self, ctx:CalculadoraParser.FactorContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#factor.
    def exitFactor(self, ctx:CalculadoraParser.FactorContext):
        pass



del CalculadoraParser