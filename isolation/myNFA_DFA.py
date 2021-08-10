from myNFA import *
from myDFA import *

import sys

def nfa_dfa(nfa: NFA) -> DFA:
    delta = dict()
    visited = dict()
    finalStates = []
    queue = []

    sink = -1

    initialE = nfa.epsilonClosure(nfa.initialState)
    queue.append(initialE)
    visited[frozenset(initialE)] = 0;

    for sf in nfa.finalStates:
        if sf in initialE:
            finalStates.append(0)

    i = 1

    while queue:
        s = queue.pop(0)
        pred = visited[frozenset(s)]
        for c in nfa.alphabet:
            reached = nfa.multipleStep(s,c)
            if reached == set():
                if sink == -1:
                    sink = i
                    #print("FOUND SINK: ",i)
                    i += 1
                    for c1 in nfa.alphabet:
                        delta[(sink,c1)] = sink
                delta[(pred,c)] = sink
                continue

            if frozenset(reached) not in visited.keys():
                queue.append(reached)
                visited[frozenset(reached)] = i
                delta[(pred,c)] = i
                for sf in nfa.finalStates:
                    if sf in reached:
                        finalStates.append(i)
                i += 1

            else:
                ri = visited[frozenset(reached)]
                delta[(pred, c)] = ri

    return DFA(i, nfa.alphabet, 0, finalStates, delta)

def main_convertor(nfa: NFA, outputFile):
    dfa = nfa_dfa(nfa)
    with open(outputFile, "w") as out:
        out.write(str(dfa))
        out.close()
    #dfa.graphvizDFA()
    # NFA.readNfaHW('tests/ref/normal_2.txt').graphvizNFA()
