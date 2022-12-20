import sqlite3
import pydot

# Connect to the database
conn = sqlite3.connect("hr")
cursor = conn.cursor()

# Get the list of tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Create a new graph
graph = pydot.Dot(rankdir="LR", size="8,5")

# Add each table as a node in the graph
for table in tables:
    node = pydot.Node(table[0], shape="plaintext")
    graph.add_node(node)

# Add edges between tables for foreign key relationships
cursor.execute("PRAGMA foreign_key_list(employees)")
for row in cursor.fetchall():
    source_table = "employees"
    target_table = row[2]
    edge = pydot.Edge(source_table, target_table)
    graph.add_edge(edge)

cursor.execute("PRAGMA foreign_key_list(departments)")
for row in cursor.fetchall():
    source_table = "departments"
    target_table = row[2]
    edge = pydot.Edge(source_table, target_table)
    graph.add_edge(edge)

# Save the graph to a file
graph.write_png("hr_diagram.png")
