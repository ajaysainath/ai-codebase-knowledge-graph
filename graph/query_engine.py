class QueryEngine:

    def __init__(self, graph):
        self.graph = graph

    # Which functions call a specific function
    def find_callers(self, function_name):

        callers = []

        for source, target, data in self.graph.edges(data=True):
            if data.get("relationship") == "calls" and target == function_name:
                callers.append(source)

        return callers


    # Which functions a function calls
    def find_callees(self, function_name):

        callees = []

        for source, target, data in self.graph.edges(data=True):
            if data.get("relationship") == "calls" and source == function_name:
                callees.append(target)

        return callees

    # Which files import a module
    def find_importers(self, module_name):

        importers = []

        for source, target, data in self.graph.edges(data=True):
            if data.get("relationship") == "imports" and target == module_name:
                importers.append(source)

        return importers