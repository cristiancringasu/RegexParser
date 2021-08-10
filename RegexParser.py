# Generated from Regex.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
        buf.write("\67\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\7\2\25\n\2\f\2\16\2\30\13\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\7\3\37\n\3\f\3\16\3\"\13\3\3\4\3\4\6")
        buf.write("\4&\n\4\r\4\16\4\'\3\4\5\4+\n\4\3\5\3\5\5\5/\n\5\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\2\4\2\4\b\2\4\6\b\n\f\2\2\2\65")
        buf.write("\2\16\3\2\2\2\4\31\3\2\2\2\6*\3\2\2\2\b.\3\2\2\2\n\60")
        buf.write("\3\2\2\2\f\62\3\2\2\2\16\17\b\2\1\2\17\20\5\4\3\2\20\26")
        buf.write("\3\2\2\2\21\22\f\3\2\2\22\23\7\4\2\2\23\25\5\4\3\2\24")
        buf.write("\21\3\2\2\2\25\30\3\2\2\2\26\24\3\2\2\2\26\27\3\2\2\2")
        buf.write("\27\3\3\2\2\2\30\26\3\2\2\2\31\32\b\3\1\2\32\33\5\6\4")
        buf.write("\2\33 \3\2\2\2\34\35\f\3\2\2\35\37\5\6\4\2\36\34\3\2\2")
        buf.write("\2\37\"\3\2\2\2 \36\3\2\2\2 !\3\2\2\2!\5\3\2\2\2\" \3")
        buf.write("\2\2\2#%\5\b\5\2$&\7\3\2\2%$\3\2\2\2&\'\3\2\2\2\'%\3\2")
        buf.write("\2\2\'(\3\2\2\2(+\3\2\2\2)+\5\b\5\2*#\3\2\2\2*)\3\2\2")
        buf.write("\2+\7\3\2\2\2,/\5\n\6\2-/\5\f\7\2.,\3\2\2\2.-\3\2\2\2")
        buf.write("/\t\3\2\2\2\60\61\7\b\2\2\61\13\3\2\2\2\62\63\7\5\2\2")
        buf.write("\63\64\5\2\2\2\64\65\7\6\2\2\65\r\3\2\2\2\7\26 \'*.")
        return buf.getvalue()


class RegexParser ( Parser ):

    grammarFileName = "Regex.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'|'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "KLEEN", "UNION", "OPEN", "CLOSE", "WHITESPACE", 
                      "VAR" ]

    RULE_expr = 0
    RULE_simple_expr = 1
    RULE_basic_expr = 2
    RULE_atom = 3
    RULE_variable = 4
    RULE_inner_expr = 5

    ruleNames =  [ "expr", "simple_expr", "basic_expr", "atom", "variable", 
                   "inner_expr" ]

    EOF = Token.EOF
    KLEEN=1
    UNION=2
    OPEN=3
    CLOSE=4
    WHITESPACE=5
    VAR=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_expr(self):
            return self.getTypedRuleContext(RegexParser.Simple_exprContext,0)


        def expr(self):
            return self.getTypedRuleContext(RegexParser.ExprContext,0)


        def UNION(self):
            return self.getToken(RegexParser.UNION, 0)

        def getRuleIndex(self):
            return RegexParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RegexParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.simple_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 20
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RegexParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 15
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 16
                    self.match(RegexParser.UNION)
                    self.state = 17
                    self.simple_expr(0) 
                self.state = 22
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Simple_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basic_expr(self):
            return self.getTypedRuleContext(RegexParser.Basic_exprContext,0)


        def simple_expr(self):
            return self.getTypedRuleContext(RegexParser.Simple_exprContext,0)


        def getRuleIndex(self):
            return RegexParser.RULE_simple_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_expr" ):
                return visitor.visitSimple_expr(self)
            else:
                return visitor.visitChildren(self)



    def simple_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RegexParser.Simple_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_simple_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.basic_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 30
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RegexParser.Simple_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_simple_expr)
                    self.state = 26
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 27
                    self.basic_expr() 
                self.state = 32
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Basic_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(RegexParser.AtomContext,0)


        def KLEEN(self, i:int=None):
            if i is None:
                return self.getTokens(RegexParser.KLEEN)
            else:
                return self.getToken(RegexParser.KLEEN, i)

        def getRuleIndex(self):
            return RegexParser.RULE_basic_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_expr" ):
                return visitor.visitBasic_expr(self)
            else:
                return visitor.visitChildren(self)




    def basic_expr(self):

        localctx = RegexParser.Basic_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_basic_expr)
        try:
            self.state = 40
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.atom()
                self.state = 35 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 34
                        self.match(RegexParser.KLEEN)

                    else:
                        raise NoViableAltException(self)
                    self.state = 37 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.atom()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(RegexParser.VariableContext,0)


        def inner_expr(self):
            return self.getTypedRuleContext(RegexParser.Inner_exprContext,0)


        def getRuleIndex(self):
            return RegexParser.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = RegexParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_atom)
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RegexParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.variable()
                pass
            elif token in [RegexParser.OPEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.inner_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(RegexParser.VAR, 0)

        def getRuleIndex(self):
            return RegexParser.RULE_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = RegexParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(RegexParser.VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Inner_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self):
            return self.getToken(RegexParser.OPEN, 0)

        def expr(self):
            return self.getTypedRuleContext(RegexParser.ExprContext,0)


        def CLOSE(self):
            return self.getToken(RegexParser.CLOSE, 0)

        def getRuleIndex(self):
            return RegexParser.RULE_inner_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInner_expr" ):
                return visitor.visitInner_expr(self)
            else:
                return visitor.visitChildren(self)




    def inner_expr(self):

        localctx = RegexParser.Inner_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_inner_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(RegexParser.OPEN)
            self.state = 49
            self.expr(0)
            self.state = 50
            self.match(RegexParser.CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expr_sempred
        self._predicates[1] = self.simple_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def simple_expr_sempred(self, localctx:Simple_exprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




