from analyzer.code_parser import CodeParser
from analyzer.relationship_extractor import extract_relationships
from graph.graph_builder import CodebaseGraph
from graph.query_engine import QueryEngine
from visualization.graph_visualizer import GraphVisualizer


project_path = "examples"

parser = CodeParser(project_path)
graph_builder = CodebaseGraph()

data = parser.parse_project()

for file_data in data:

    relationships = extract_relationships(file_data["file"])

    graph_builder.build_from_relationships(
        file_data["file"],
        relationships
    )

graph_builder.show_graph()

# visualization
visualizer = GraphVisualizer(graph_builder.graph)
visualizer.visualize()

# query engine
query = QueryEngine(graph_builder.graph)

print("\n--- Query Results ---")

print("\nFunctions calling database.save_user:")
print(query.find_callers("database.save_user"))

print("\nFunctions called by create_user:")
print(query.find_callees("create_user"))

print("\nFiles importing database:")
print(query.find_importers("database"))