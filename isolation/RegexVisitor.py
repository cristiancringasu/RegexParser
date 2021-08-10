# Generated from Regex.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RegexParser import RegexParser
else:
    from RegexParser import RegexParser

# This class defines a complete generic visitor for a parse tree produced by RegexParser.

class RegexVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RegexParser#expr.
    def visitExpr(self, ctx:RegexParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#simple_expr.
    def visitSimple_expr(self, ctx:RegexParser.Simple_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#basic_expr.
    def visitBasic_expr(self, ctx:RegexParser.Basic_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#atom.
    def visitAtom(self, ctx:RegexParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#variable.
    def visitVariable(self, ctx:RegexParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#inner_expr.
    def visitInner_expr(self, ctx:RegexParser.Inner_exprContext):
        return self.visitChildren(ctx)



del RegexParser