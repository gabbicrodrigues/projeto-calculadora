# Generated from Calculadora.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalculadoraParser import CalculadoraParser
else:
    from CalculadoraParser import CalculadoraParser

# This class defines a complete generic visitor for a parse tree produced by CalculadoraParser.

class CalculadoraVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculadoraParser#expr.
    def visitExpr(self, ctx:CalculadoraParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#term.
    def visitTerm(self, ctx:CalculadoraParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#factor.
    def visitFactor(self, ctx:CalculadoraParser.FactorContext):
        return self.visitChildren(ctx)



del CalculadoraParser