import ast
import os


class CodeParser:
    def __init__(self, project_path):
        self.project_path = project_path

    def get_python_files(self):
        python_files = []

        for root, dirs, files in os.walk(self.project_path):
            for file in files:
                if file.endswith(".py"):
                    python_files.append(os.path.join(root, file))

        return python_files


    def parse_file(self, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            source = f.read()

        tree = ast.parse(source)

        classes = []
        functions = []
        imports = []

        for node in ast.walk(tree):

            if isinstance(node, ast.ClassDef):
                classes.append(node.name)

            elif isinstance(node, ast.FunctionDef):
                functions.append(node.name)

            elif isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(alias.name)

            elif isinstance(node, ast.ImportFrom):
                imports.append(node.module)

        return {
            "file": file_path,
            "classes": classes,
            "functions": functions,
            "imports": imports
        }


    def parse_project(self):
        results = []

        python_files = self.get_python_files()

        for file in python_files:
            parsed = self.parse_file(file)
            results.append(parsed)

        return results