import networkx as nx

class DependencyAnalyzer:

    def __init__(self, graph):
        self.graph = graph

    def detect_circular_dependencies(self):

        cycles = list(nx.simple_cycles(self.graph))

        return cycles