class AIQueryEngine:

    def __init__(self, graph):
        self.graph = graph

    def answer_question(self, question):

        question = question.lower()

        if "call" in question:

            results = []

            for source, target, data in self.graph.edges(data=True):
                if data.get("relationship") == "calls":
                    results.append(f"{source} calls {target}")

            return results

        elif "import" in question:

            results = []

            for source, target, data in self.graph.edges(data=True):
                if data.get("relationship") == "imports":
                    results.append(f"{source} imports {target}")

            return results

        elif "architecture" in question:

            results = []

            for source, target, data in self.graph.edges(data=True):
                relation = data.get("relationship")
                results.append(f"{source} {relation} {target}")

            return results

        else:
            return ["I could not understand the question."]