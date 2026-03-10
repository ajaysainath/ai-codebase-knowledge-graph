class RiskAnalyzer:

    def __init__(self, graph):
        self.graph = graph

    def most_depended_nodes(self):

        dependency_count = {}

        for source, target, data in self.graph.edges(data=True):

            dependency_count[target] = dependency_count.get(target, 0) + 1

        sorted_nodes = sorted(
            dependency_count.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return sorted_nodes

    def most_connected_nodes(self):

        connection_count = {}

        for source, target in self.graph.edges():

            connection_count[source] = connection_count.get(source, 0) + 1
            connection_count[target] = connection_count.get(target, 0) + 1

        sorted_nodes = sorted(
            connection_count.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return sorted_nodes