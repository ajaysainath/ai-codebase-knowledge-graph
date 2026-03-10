class ArchitectureExplainer:

    def __init__(self, graph):
        self.graph = graph

    def generate_explanation(self):

        explanation = []

        for source, target, data in self.graph.edges(data=True):

            relation = data.get("relationship")

            if relation == "imports":
                explanation.append(
                    f"The file '{source}' imports the module '{target}'."
                )

            elif relation == "calls":
                explanation.append(
                    f"The function '{source}' calls '{target}'."
                )

        return explanation