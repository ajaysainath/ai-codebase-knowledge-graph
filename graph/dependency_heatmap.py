class DependencyHeatmap:

    def __init__(self, graph):
        self.graph = graph

    def compute_heatmap(self):

        heatmap = {}

        for source, target in self.graph.edges():

            heatmap[target] = heatmap.get(target, 0) + 1

        sorted_nodes = sorted(
            heatmap.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return sorted_nodes