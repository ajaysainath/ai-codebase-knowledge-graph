import ast


class RelationshipExtractor(ast.NodeVisitor):

    def __init__(self):
        self.calls = []
        self.imports = []
        self.current_function = None

    def visit_FunctionDef(self, node):
        self.current_function = node.name
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Attribute):
            call_name = f"{self.get_name(node.func.value)}.{node.func.attr}"
        elif isinstance(node.func, ast.Name):
            call_name = node.func.id
        else:
            call_name = "unknown"

        if self.current_function:
            self.calls.append((self.current_function, call_name))

        self.generic_visit(node)

    def visit_Import(self, node):
        for alias in node.names:
            self.imports.append(alias.name)

    def visit_ImportFrom(self, node):
        if node.module:
            self.imports.append(node.module)

    def get_name(self, node):
        if isinstance(node, ast.Name):
            return node.id
        return "unknown"


def extract_relationships(file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source)

    extractor = RelationshipExtractor()
    extractor.visit(tree)

    return {
        "imports": extractor.imports,
        "calls": extractor.calls
    }