**AI Codebase Knowledge Graph**
---
An interactive developer tool that analyzes a Python codebase and converts it into a knowledge graph showing relationships between files, functions, and modules. The system visualizes software architecture, detects dependencies, and provides AI-assisted exploration of the codebase.

This tool helps developers understand large projects quickly, explore dependencies, and analyze the impact of code changes.

## Key Capabilities

- Static code analysis using Python AST
- Knowledge graph generation for code relationships
- Interactive dependency visualization
- Architecture explanation and risk analysis
- Circular dependency detection
- Dependency heatmap and architecture layers
- AI-assisted codebase queries
- Code change impact analysis

## Demo Workflow

1. Upload a Python project or provide a project path.
2. Click **Analyze Codebase**.
3. The system builds a knowledge graph of the codebase.
4. Explore the architecture using the interactive graph.
5. Use the AI assistant to query the codebase.
6. Inspect dependencies, risks, and architecture layers.

Example analysis output:

sample.py → imports → database  
create_user → calls → database.save_user

**Overview**

Modern software systems contain many interconnected modules. Understanding how components interact can be difficult when reading raw source code.

This project analyzes a Python codebase using the Abstract Syntax Tree (AST) and converts it into a graph representation.

In the graph:

Nodes represent code components:

files
modules
classes
functions

Edges represent relationships such as:

imports
function calls
dependencies

The tool then provides an interactive dashboard to explore and analyze this graph.

**Key Features**

*Codebase Parsing*

The system scans a Python project folder and extracts structural elements such as:

modules
classes
functions
imports
function calls

This is done using Python's AST (Abstract Syntax Tree) module.

**Knowledge Graph Generation**

*All extracted components are converted into a directed graph using NetworkX.*

Example relationships:

sample.py → imports → database
create_user → calls → database.save_user

This graph represents the architecture of the project.

**Interactive Dependency Visualization**

The graph is visualized using PyVis, allowing users to:

explore dependencies visually
drag nodes
inspect relationships
understand architecture instantly

**Graph Search and Highlighting**

Users can search for a specific component such as:

database
create_user

Matching nodes are automatically highlighted in the graph.

**Node Inspector**

Developers can inspect a specific node and see:

functions it calls
functions that call it
modules it imports
modules that import it

Example:

Node: create_user

Calls:
database.save_user

Called by:
sample.py

**Architecture Explanation**

The tool automatically generates natural language explanations of the architecture.

Example:

The file sample.py imports the module database.
The function create_user calls database.save_user.

This helps developers quickly understand system structure.

**Circular Dependency Detection**

The system detects circular dependencies such as:

moduleA → moduleB → moduleC → moduleA

These cycles can cause architectural problems and are highlighted in the dashboard.

**Architecture Layer Detection**

The system automatically detects architectural layers based on dependency order.

Example:

Layer 0
sample.py
create_user

Layer 1
database
database.save_user

This reveals how application logic flows through the system.

**Dependency Heatmap**

The tool calculates which components are most depended upon.

Example:

database → 8 dependencies
auth → 5 dependencies
user_service → 3 dependencies

This helps identify critical modules in the system.

**Architecture Risk Analysis**

Components with the highest connectivity are identified as architectural risks.

Example:

database is the most depended component

This helps developers locate potential bottlenecks.

**AI Codebase Assistant**

Users can ask questions about the codebase.

Example questions:

Which functions call the database?
What modules import database?
Explain the architecture.

The assistant answers using the knowledge graph.

**Interactive Dependency Explorer**

Developers can focus on a single component and view a focused dependency graph around it.

Example:

create_user
   ↓
database.save_user

This is useful for exploring large codebases.

**Code Change Impact Analysis**

The tool can analyze what parts of the system might break if a component changes.

Example:

If database changes → affected components:

create_user
sample.py

This helps developers understand the impact of code modifications.

**System Architecture**

The pipeline of the system works as follows:

User uploads project
        ↓
Code parser scans Python files
        ↓
AST extracts functions, classes, imports
        ↓
Relationships are detected
        ↓
Knowledge graph is built using NetworkX
        ↓
Graph is visualized using PyVis
        ↓
Streamlit dashboard provides exploration tools

**Project Structure**

ai-codebase-knowledge-graph/

analyzer/
    code_parser.py
    relationship_extractor.py

graph/
    graph_builder.py
    query_engine.py
    ai_query_engine.py
    dependency_analyzer.py
    dependency_heatmap.py
    dependency_explorer.py
    architecture_explainer.py
    architecture_layers.py
    risk_analyzer.py
    impact_analyzer.py

visualization/
    graph_visualizer.py

ui/
    streamlit_app.py

examples/
    sample.py
    database.py

requirements.txt
README.md

**Technologies Used**

Python

*Key libraries:*

1.AST (code parsing)
2.NetworkX (graph modeling)
3.PyVis (graph visualization)
4.Streamlit (interactive dashboard)

**Installation**

*Clone the repository.*

git clone https://github.com/your-username/ai-codebase-knowledge-graph.git

*Navigate into the project.*

cd ai-codebase-knowledge-graph

*Install dependencies.*

pip install -r requirements.txt

**Running the Application**

*Start the Streamlit dashboard.*

python -m streamlit run ui/streamlit_app.py --server.port 1804

*Open your browser and go to:*

http://localhost:1804

**Example Usage**

*Upload a Python project or specify a project folder.*

Click Analyze *Codebase.*

*The system will:*

generate the knowledge graph
display architecture visualization
detect dependencies
provide AI insights

*You can then explore the system using:*
1.graph search
2.node inspector
3.dependency explorer
4.AI assistant
5.impact analysis

**Example Output**
*Example relationships detected:*

sample.py → imports → database
create_user → calls → database.save_user

*Example architecture layers:*

Layer 0
sample.py

Layer 1
create_user

Layer 2
database.save_user
database
Future Improvements

*Possible extensions:*
1.support for multiple programming languages
2.clickable graph node inspector
3.advanced AI architecture explanations
4.integration with GitHub repositories
5.automated architecture diagrams

**Why This Project Matters**
*Understanding large codebases is a major challenge in software development.*
*This project demonstrates how static code analysis and graph modeling can be used to:*

1.visualize architecture
2.detect hidden dependencies
3.analyze change impact
4.assist developers in exploring complex systems

**Author**
Ajay Sainath

AI Codebase Knowledge Graph
Static analysis and software architecture exploration tool.

## Why This Project

Understanding large codebases is a common challenge in software development.

This project demonstrates how static code analysis and graph modeling can help developers:

- visualize architecture
- detect hidden dependencies
- analyze the impact of code changes
- explore complex systems interactively

The tool combines AST parsing, graph algorithms, and interactive visualization to provide insights into software architecture.

## Future Improvements

Possible future enhancements include:

- support for multiple programming languages
- advanced AI architecture explanations
- clickable node inspection in the graph
- GitHub repository integration
- architecture pattern detection
