import sys
from antlr4 import *
from myNFA import *
from RegexVisitor import RegexVisitor
from RegexParser import RegexParser

class RegexComputeVisitor(RegexVisitor):

    def visitExpr(self, ctx:RegexParser.ExprContext):
        s = ctx.simple_expr()
        e = ctx.expr()
        if e:
            v1 = self.visit(s)
            v2 = self.visit(e)
            return union_nfa(v1,v2)
        else:
            return self.visit(s)

    def visitSimple_expr(self, ctx:RegexParser.Simple_exprContext):
        s = ctx.simple_expr()
        b = ctx.basic_expr()
        if s:
            v1 = self.visit(s)
            v2 = self.visit(b)
            return concat_nfa(v1, v2)
        else:
            return self.visit(b)


    def visitBasic_expr(self, ctx:RegexParser.Basic_exprContext):
        a = ctx.atom()
        k = ctx.KLEEN()
        v = self.visit(a)
        if k:
            return kleen_nfa(v)
        else:
            return v


    def visitAtom(self, ctx:RegexParser.AtomContext):
        v = ctx.variable()
        inner = ctx.inner_expr()
        if v:
            return self.visit(v)
        if inner:
            return self.visit(inner)

    def visitVariable(self, ctx: RegexParser.VariableContext):
        return var_nfa(str(ctx.VAR()))

    def visitInner_expr(self, ctx:RegexParser.Inner_exprContext):
        return self.visit(ctx.expr())




del RegexParser