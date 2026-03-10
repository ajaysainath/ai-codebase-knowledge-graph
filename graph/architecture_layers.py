import networkx as nx

class ArchitectureLayerDetector:

    def __init__(self, graph):
        self.graph = graph

    def detect_layers(self):

        layers = []

        try:
            order = list(nx.topological_sort(self.graph))
        except:
            # if cycles exist, fallback to nodes
            order = list(self.graph.nodes())

        layer_map = {}

        for node in order:

            predecessors = list(self.graph.predecessors(node))

            if not predecessors:
                layer_map[node] = 0
            else:
                layer_map[node] = max(layer_map[p] for p in predecessors) + 1

        for node, layer in layer_map.items():

            while len(layers) <= layer:
                layers.append([])

            layers[layer].append(node)

        return layers