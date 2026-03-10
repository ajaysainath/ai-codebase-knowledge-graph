import networkx as nx


class CodebaseGraph:

    def __init__(self):
        self.graph = nx.DiGraph()

    def add_import(self, file_name, module):
        self.graph.add_node(file_name, type="file")
        self.graph.add_node(module, type="module")
        self.graph.add_edge(file_name, module, relationship="imports")

    def add_call(self, caller, callee):
        self.graph.add_node(caller, type="function")
        self.graph.add_node(callee, type="function")
        self.graph.add_edge(caller, callee, relationship="calls")

    def build_from_relationships(self, file_name, relationships):

        for imp in relationships["imports"]:
            self.add_import(file_name, imp)

        for caller, callee in relationships["calls"]:
            self.add_call(caller, callee)

    def show_graph(self):

        print("\nGraph Relationships:\n")

        for source, target, data in self.graph.edges(data=True):
            print(f"{source} → {data['relationship']} → {target}")