import networkx as nx

class DependencyExplorer:

    def __init__(self, graph):
        self.graph = graph

    def extract_subgraph(self, node_name):

        nodes = set()

        for source, target in self.graph.edges():

            if node_name in source or node_name in target:
                nodes.add(source)
                nodes.add(target)

        subgraph = self.graph.subgraph(nodes)

        return subgraph