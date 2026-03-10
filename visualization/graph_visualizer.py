from pyvis.network import Network


class GraphVisualizer:

    def __init__(self, graph):
        self.graph = graph

    def visualize(self, highlight_node=None):

        net = Network(height="750px", width="100%", directed=True)

        # add nodes
        for node, data in self.graph.nodes(data=True):

            label = node
            node_type = data.get("type", "node")

            color = "#97c2fc"

            if node_type == "file":
                color = "#ffcc00"
            elif node_type == "function":
                color = "#97c2fc"
            elif node_type == "module":
                color = "#ff9999"

            # highlight search
            if highlight_node and highlight_node.lower() in node.lower():
                color = "red"

            net.add_node(node, label=label, color=color)

        # edges code continues here...

        # add edges
        for source, target, data in self.graph.edges(data=True):

            relation = data.get("relationship", "")

            net.add_edge(
                source,
                target,
                label=relation
            )

        net.write_html("codebase_graph.html")