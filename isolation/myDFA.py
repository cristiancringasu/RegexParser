#import graphviz
#import os

# K - multimea de stari
# Sigma - Alfabet
# s_i = starea initiala
# F = multimea de stari finale
# delta = tranzitiile -- dictionar


class State:
    def __init__(self, id):
        self.id: int = id
        self.delta = {}

    def __str__(self):
        return str(self.id)

    def add_transition(self, c, q2):
        self.delta[c] = q2

    def step(self, c):
        return self.delta[c]


class DFA:
    def __init__(self, number_of_states, sigma, initial_state, final_states, delta):
        self.K = [State(i) for i in range(0, number_of_states)]
        self.sigma = sigma
        self.s_i = self.K[initial_state]
        self.final_states = list(map(lambda state_id: self.K[state_id], final_states))
        self.delta = delta
        for (s1, c), s2 in delta.items():
            self.K[s1].add_transition(c, self.K[s2])

    def accept(self, word: str):
        s = self.s_i
        for i in range(0, len(word)):
            s = s.step(word[i])
        if s in self.final_states:
            return True
        return False

    def next_step(self, sid, word: str):
        return self.K[sid].step(word[0]), word[1:]

    def graphvizDFA(self):
        if os.path.exists('graphviz/dfa.gv.pdf'):
            os.remove('graphviz/dfa.gv.pdf')
        node_attr = {
            'fontsize': '11',
            'shape': 'circle',
            'fontcolor': 'black'
        }
        edge_attr = {
            'shape': 'tee'
        }
        dot = graphviz.Digraph(comment='My Directed Graph', strict=False, node_attr=node_attr, edge_attr=edge_attr)

        for state in self.K:
            dot.node(str(state))

        for state in self.K:
            for char in self.sigma:
                if (state.id, char) in self.delta:
                    nextState = self.delta[(state.id, char)]
                    label = char
                    dot.edge(str(state), str(nextState), label=str(label))

        dot.render('graphviz/dfa.gv', view=True)

    def __str__(self):
        result = str(len(self.K)) + "\n"
        result += str(" ".join(list(map(str, self.final_states)))) + "\n"
        for (s1, c), s2 in self.delta.items():
            result += str(s1) + " " + c + " " + str(s2) + "\n"
        return result
