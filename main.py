import sys
from myNFA import *
from myDFA import *
from myNFA_DFA import *
from antlr4 import *
from RegexLexer import RegexLexer
from RegexParser import RegexParser
from RegexShowVisitor import RegexShowVisitor
from RegexComputeVisitor import RegexComputeVisitor

input = FileStream(sys.argv[1])
lexer = RegexLexer(input)
stream = CommonTokenStream(lexer)
parser = RegexParser(stream)

tree = parser.expr()

computeVisitor = RegexComputeVisitor()

nfa_regex = computeVisitor.visit(tree)
with open(sys.argv[2], "w") as out:
    out.write(str(nfa_regex))
    out.close()
main_convertor(nfa_regex, sys.argv[3])

