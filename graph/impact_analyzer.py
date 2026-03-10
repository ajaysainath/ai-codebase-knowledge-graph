class ImpactAnalyzer:

    def __init__(self, graph):
        self.graph = graph

    def analyze_impact(self, node_name):

        affected = []

        for source, target in self.graph.edges():

            if node_name in target:
                affected.append(source)

        return list(set(affected))