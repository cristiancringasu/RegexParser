from functools import reduce
from typing import List, Tuple, Set, Dict

#import graphviz
#import os

State = int
Word = str
Configuration = Tuple[State, Word]
Transition = Tuple[State, Word, List[State]]
EPSILON = ""


class NFA:
    def __init__(self, numberOfStates: int, alphabet: Set[chr], finalStates: Set[State],
                 delta: Dict[Tuple[State, chr], Set[State]]):
        self.numberOfStates = numberOfStates
        self.states = set(range(self.numberOfStates))
        self.alphabet = alphabet
        self.initialState = 0
        self.finalStates = finalStates
        self.delta = delta

    def __str__(self):
        result = str(self.numberOfStates) + "\n"
        result += str(" ".join(list(map(str, self.finalStates)))) + "\n"
        for (s1, c), s2 in self.delta.items():
            if c == EPSILON:
                c = 'eps'
            result += str(s1) + " " + c + " " + str(" ".join(list(map(str, s2)))) + "\n"
        return result

    def step(self, configuration: Configuration) -> List[Configuration]:
        # result : Set[State] = set()
        # eclosure = self.epsilonClosure(configuration[0])
        # print("eC",eclosure)
        # for stateX in eclosure:
        #     if (stateX,configuration[1][0]) in self.delta:
        #         result |= (self.delta[stateX, configuration[1][0]])
        # return result
        result: Set[State] = set()
        if (configuration[0], configuration[1][0]) in self.delta:
            result |= (self.delta[configuration[0], configuration[1][0]])
        return result

    def epsilonClosure(self, state: State) -> Set[State]:
        visited = []
        queue = []

        queue.append(state)
        visited.append(state)

        while queue:
            s = queue.pop(0)
            for i in self.delta.get((s, EPSILON),[]):
                if i not in visited:
                    queue.append(i)
                    visited.append(i)

        return set(visited)

    def kstep(self, configuration: Configuration, k: int) -> List[Configuration]:
        states = self.epsilonClosure(configuration[0])
        word = configuration[1]

        while k > 0:
            newStates : Set[State] = set()
            #print("Aici")
            for stateX in states:
                #print("sX", stateX)
                newStates |= (self.step((stateX,word)))
            #print("nS: ",newStates)
            newEStates : Set[State] = set()
            for stateX in newStates:
                newEStates |= (self.epsilonClosure(stateX))
            word = word[1:]
            states = newEStates
            #print("nE: ", states)
            k -= 1
        return states

    def multipleStep(self, states: Set[State], c: chr) -> Set[State]:
        newStates : Set[State] = set()
        for stateX in states:
            newStates |= (self.step((stateX,c)))
        newEStates : Set[State] = set()
        for stateX in newStates:
            newEStates |= (self.epsilonClosure(stateX))
        return newEStates


    def accept(self, word: Word) -> bool:
        if list(filter(lambda stateX: stateX in self.finalStates, self.kstep((0,word), len(word)))):
            return True
        return False

    def graphAdj(self, state: State) -> Set[State]:
        result : Set[State] = set()
        wrapped = [stateX for (s, _), stateX in self.delta.items() if s == state]
        for i in wrapped:
            result |= i
        return result

    def emptyLanguage(self) -> bool:
        visited = [False] * self.numberOfStates
        queue = []
        queue.append(self.initialState)

        while queue:
            s = queue.pop(0)
            for i in self.graphAdj(s):
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

        for i in self.finalStates:
            if visited[i] == True:
                return True
        return False

    def graphvizNFA(self):
        if os.path.exists('graphviz/nfa.gv.pdf'):
            os.remove('graphviz/nfa.gv.pdf')

        node_attr = {
            'fontsize': '11',
            'shape': 'circle',
            'fontcolor': 'black'
        }
        edge_attr = {
            'shape': 'tee'
        }
        dot = graphviz.Digraph(comment='My Directed Graph', strict=False, node_attr=node_attr, edge_attr=edge_attr)

        for state in self.states:
            dot.node(str(state))

        for state in self.states:
            for char in self.alphabet | {EPSILON}:
                if (state, char) in self.delta:
                    for nextState in self.delta[(state, char)]:
                        if char == EPSILON:
                            label = "e"
                        else:
                            label = char
                        dot.edge(str(state), str(nextState), label=str(label))

        dot.render('graphviz/nfa.gv', view=True)


def readNfa(inputFile) -> NFA:
    with open(inputFile) as file:
        numberOfStates = int(file.readline().rstrip())
        alphabet = set(file.readline().rstrip().split(" "))
        finalStates = set(map(int, file.readline().rstrip().split(" ")))
        delta = dict()
        while True:
            transition = file.readline().rstrip().split(" ")
            if transition == ['']:
                break
            if transition[1] == "EPS":
                transition[1] = EPSILON

            delta[(int(transition[0]), transition[1])] = set(map(int, transition[2:]))

        nfa = NFA(
            numberOfStates=numberOfStates,
            alphabet=alphabet,
            finalStates=finalStates,
            delta=delta
        )
        return nfa

def readNfaHW(inputFile) -> NFA:
    with open(inputFile) as file:
        numberOfStates = int(file.readline().rstrip())
        alphabet = set()
        finalStates = set(map(int, file.readline().rstrip().split(" ")))
        delta = dict()
        while True:
            transition = file.readline().rstrip().split(" ")
            if transition == ['']:
                break
            if transition[1] == "eps":
                transition[1] = EPSILON
            else:
                alphabet.add(transition[1])
            delta[(int(transition[0]), transition[1])] = set(map(int, transition[2:]))
        file.close()
        nfa = NFA(
            numberOfStates=numberOfStates,
            alphabet=alphabet,
            finalStates=finalStates,
            delta=delta
        )
        return nfa

def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

def var_nfa(input) -> NFA:
    numberOfStates = 2
    alphabet = set(input)
    finalStates = set([1])
    delta = dict()
    delta[0,input] = set([1])
    nfa = NFA(
        numberOfStates=numberOfStates,
        alphabet=alphabet,
        finalStates=finalStates,
        delta=delta
    )
    return nfa

def kleen_nfa(nfa: NFA) -> NFA:
    for state in nfa.finalStates:
        if (state, EPSILON) in nfa.delta.keys():
            nfa.delta[(state, EPSILON)].add(nfa.initialState)
        else:
            nfa.delta[(state, EPSILON)] = set([nfa.initialState])
    nfa.finalStates.add(nfa.initialState)
    return nfa

def translate_nfa(nfa: NFA, tx):
    nfa.initialState += tx
    deltaTrans = dict()
    for key in nfa.delta:
        state = key[0]
        char = key[1]
        deltaTrans[(state + tx, char)] = nfa.delta[(state, char)]
        deltaTrans[(state + tx, char)] = set(map(lambda x: x + tx, deltaTrans[(state + tx, char)]))
    nfa.delta = deltaTrans
    nfa.finalStates = set(map(lambda x: x + tx, nfa.finalStates))

def union_nfa(nfa1: NFA, nfa2: NFA) -> NFA:
    translate_nfa(nfa1,1)
    translate_nfa(nfa2,nfa1.numberOfStates + 1)
    numberOfStates = nfa1.numberOfStates + nfa2.numberOfStates + 2
    alphabet = nfa1.alphabet | nfa2.alphabet
    finalStates = set([numberOfStates - 1])
    delta = merge_two_dicts(nfa1.delta, nfa2.delta)
    delta[(0,EPSILON)] = set([nfa1.initialState, nfa2.initialState])
    for state in nfa1.finalStates:
        if (state, EPSILON) in delta.keys():
            delta[(state, EPSILON)].add(numberOfStates - 1)
        else :
            delta[(state, EPSILON)] = set([numberOfStates - 1])
    for state in nfa2.finalStates:
        if (state, EPSILON) in delta.keys():
            delta[(state, EPSILON)].add(numberOfStates - 1)
        else:
            delta[(state, EPSILON)] = set([numberOfStates - 1])
    nfa = NFA(
        numberOfStates=numberOfStates,
        alphabet=alphabet,
        finalStates=finalStates,
        delta=delta
    )
    return nfa

def concat_nfa(nfa1: NFA, nfa2: NFA) -> NFA:
    translate_nfa(nfa2,nfa1.numberOfStates)
    numberOfStates = nfa1.numberOfStates + nfa2.numberOfStates
    alphabet = nfa1.alphabet | nfa2.alphabet
    finalStates = nfa2.finalStates
    delta = merge_two_dicts(nfa1.delta, nfa2.delta)
    for state in nfa1.finalStates:
        if (state, EPSILON) in delta.keys():
            delta[(state, EPSILON)].add(nfa2.initialState)
        else:
            delta[(state, EPSILON)] = set([nfa2.initialState])
    nfa = NFA(
        numberOfStates=numberOfStates,
        alphabet=alphabet,
        finalStates=finalStates,
        delta=delta
    )
    return nfa