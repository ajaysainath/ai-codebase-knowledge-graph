import streamlit as st
import zipfile
import os

from graph.impact_analyzer import ImpactAnalyzer
from graph.dependency_explorer import DependencyExplorer
from graph.dependency_heatmap import DependencyHeatmap
from graph.architecture_layers import ArchitectureLayerDetector
from graph.ai_query_engine import AIQueryEngine
from graph.risk_analyzer import RiskAnalyzer
from graph.dependency_analyzer import DependencyAnalyzer
from graph.architecture_explainer import ArchitectureExplainer
from analyzer.code_parser import CodeParser
from analyzer.relationship_extractor import extract_relationships
from graph.graph_builder import CodebaseGraph
from graph.query_engine import QueryEngine
from visualization.graph_visualizer import GraphVisualizer


st.title("AI Codebase Knowledge Graph")

st.write("Upload a Python project or enter a folder path to analyze its architecture.")

# ----------------------------
# Upload project
# ----------------------------

uploaded_file = st.file_uploader("Upload Python Project (.zip)", type="zip")

project_path = st.text_input("Or enter project folder path", "examples")

if uploaded_file is not None:

    extract_path = "uploaded_project"

    with zipfile.ZipFile(uploaded_file, "r") as zip_ref:
        zip_ref.extractall(extract_path)

    project_path = extract_path

    st.success("Project uploaded and extracted.")

# ----------------------------
# Analyze Codebase
# ----------------------------

if st.button("Analyze Codebase"):

    parser = CodeParser(project_path)
    graph_builder = CodebaseGraph()

    data = parser.parse_project()

    for file_data in data:

        relationships = extract_relationships(file_data["file"])

        graph_builder.build_from_relationships(
            file_data["file"],
            relationships
        )

    st.session_state.graph = graph_builder.graph

    st.success("Codebase analyzed successfully")


# ----------------------------
# Use stored graph
# ----------------------------

if "graph" in st.session_state:

    graph = st.session_state.graph

    st.subheader("Project Summary")

    num_nodes = graph.number_of_nodes()
    num_edges = graph.number_of_edges()

    st.write(f"Total components: {num_nodes}")
    st.write(f"Total relationships: {num_edges}")

    st.divider()


    st.subheader("Search in Graph")

    search_node = st.text_input("Enter function/module name")

    visualizer = GraphVisualizer(graph)
    visualizer.visualize(search_node)

    # ----------------------------
    # Graph Visualization
    # ----------------------------

    visualizer = GraphVisualizer(graph)
    visualizer.visualize(search_node)

    st.subheader("Codebase Dependency Graph")

    with open("codebase_graph.html", "r", encoding="utf-8") as f:
        html_content = f.read()

    st.components.v1.html(html_content, height=800, scrolling=True)

    st.divider()

    st.divider()

    st.subheader("Node Inspector")

    node_name = st.text_input("Enter node name to inspect")

    if node_name:

        st.write(f"Inspecting node: {node_name}")

        node_name = node_name.lower()

        called = []
        callers = []
        imports = []
        imported_by = []

        for source, target, data in graph.edges(data=True):

            relation = data.get("relationship")

            if relation == "calls":

                if source.lower() == node_name:
                    called.append(target)

                if target.lower() == node_name:
                    callers.append(source)

            elif relation == "imports":

                if source.lower() == node_name:
                    imports.append(target)

                if target.lower() == node_name:
                    imported_by.append(source)

        st.write("### Calls")
        st.write(called if called else "None")

        st.write("### Called By")
        st.write(callers if callers else "None")

        st.write("### Imports")
        st.write(imports if imports else "None")

        st.write("### Imported By")
        st.write(imported_by if imported_by else "None")

    # ----------------------------
    # Architecture Explanation
    # ----------------------------

    explainer = ArchitectureExplainer(graph)

    st.subheader("Architecture Explanation")

    explanations = explainer.generate_explanation()

    for line in explanations:
        st.write(line)

    st.divider()

    # ----------------------------
    # Dependency Analysis
    # ----------------------------

    analyzer = DependencyAnalyzer(graph)

    st.subheader("Dependency Analysis")

    cycles = analyzer.detect_circular_dependencies()

    if cycles:
        st.error("Circular dependencies detected")

        for cycle in cycles:
            st.write(" → ".join(cycle))

    else:
        st.success("No circular dependencies detected")

    st.divider()

    # ----------------------------
    # Architecture Risk Analysis
    # ----------------------------

    risk = RiskAnalyzer(graph)

    st.subheader("Architecture Risk Analysis")

    most_depended = risk.most_depended_nodes()
    most_connected = risk.most_connected_nodes()

    st.write("Most depended components:")

    for node, count in most_depended[:5]:
        st.write(f"{node} (depended on {count} times)")

    st.write("Most connected components:")

    for node, count in most_connected[:5]:
        st.write(f"{node} ({count} connections)")

    st.divider()

    top_node = most_depended[0][0] if most_depended else None

    if top_node:
        st.info(f"Most critical component in this project: {top_node}")

    st.divider()

    st.subheader("Auto Architecture Diagram")

    layer_detector = ArchitectureLayerDetector(graph)

    layers = layer_detector.detect_layers()

    for i, layer in enumerate(layers):

        st.write(f"### Layer {i}")

        for node in layer:
            st.write(node)

    st.divider()

    st.subheader("Dependency Heatmap")

    heatmap_analyzer = DependencyHeatmap(graph)

    heatmap = heatmap_analyzer.compute_heatmap()

    for node, count in heatmap:

        st.write(f"{node} → {count} dependencies")

    st.divider()

    st.subheader("Interactive Dependency Explorer")

    node_to_explore = st.text_input("Enter node to explore")

    if node_to_explore:

        explorer = DependencyExplorer(graph)

        subgraph = explorer.extract_subgraph(node_to_explore)

        if len(subgraph.nodes()) == 0:
            st.write("No dependencies found.")
        else:

            explorer_visualizer = GraphVisualizer(subgraph)
            explorer_visualizer.visualize()

            with open("codebase_graph.html", "r", encoding="utf-8") as f:
                html_content = f.read()

            st.components.v1.html(html_content, height=600)

    st.divider()

    st.subheader("Code Change Impact Analysis")

    impact_node = st.text_input("Enter component to analyze impact")

    if impact_node:

        analyzer = ImpactAnalyzer(graph)

        affected_nodes = analyzer.analyze_impact(impact_node)

        if affected_nodes:

            st.write("Components affected if this changes:")

            for node in affected_nodes:
                st.write(node)

        else:
            st.write("No dependent components found.")

    # ----------------------------
    # AI Codebase Assistant
    # ----------------------------

    st.subheader("AI Codebase Assistant")

    question = st.text_input("Ask a question about the codebase")

    if st.button("Ask AI"):

        ai_engine = AIQueryEngine(graph)

        answers = ai_engine.answer_question(question)

        for ans in answers:
            st.write(ans)

    st.divider()

    # ----------------------------
    # Query Engine
    # ----------------------------

    query_engine = QueryEngine(graph)

    st.subheader("Query the Codebase")

    query_type = st.selectbox(
        "Select Query",
        [
            "Who calls a function?",
            "What functions does a function call?",
            "Which files import a module?"
        ]
    )

    user_input = st.text_input("Enter name")

    if st.button("Run Query"):

        if query_type == "Who calls a function":
            result = query_engine.find_callers(user_input)

        elif query_type == "What functions does a function call":
            result = query_engine.find_callees(user_input)

        else:
            result = query_engine.find_importers(user_input)

        st.write("Result:")
        st.write(result)

st.divider()
st.caption("AI Codebase Knowledge Graph — Static analysis tool for exploring software architecture.")