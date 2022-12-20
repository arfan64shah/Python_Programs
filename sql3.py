import sqlite3
import pydot

# Connect to the database
conn = sqlite3.connect('hr')

# Retrieve the schema information
cursor = conn.cursor()
cursor.execute("SELECT name, sql FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

table_names = []
column_names = {}

for table in tables:
    name, sql = table
    table_names.append(name)

    # Extract the column names from the CREATE TABLE statement
    column_names[name] = []
    for line in sql.split('\n'):
        line = line.strip()
        if line.startswith('`'):
            column_names[name].append(line.split('`')[1])

graph = pydot.Dot(graph_type='graph')

for table in table_names:
    # Create a node for the table
    node = pydot.Node(table, shape='plaintext')
    graph.add_node(node)

    # Add the columns as labels to the table node
    label = '\n'.join(column_names[table])
    node.set_label(label)

# Query the database for the foreign key constraints
cursor.execute("""
    SELECT
        sql
    FROM
        sqlite_master
    WHERE
        type='table' AND
        sql LIKE '%FOREIGN KEY%';
""")
fks = cursor.fetchall()
# Extract the table names and column names from the FOREIGN KEY constraints
for fk in fks:
    sql = fk[0]
    parent_table, parent_column = None, None
    child_table, child_column = None, None
    for line in sql.split('\n'):
        line = line.strip()
        if line.startswith('FOREIGN KEY'):
            _, columns, _, _, _, _, table, _ = line.split()
            child_column = columns.strip('()')
            child_table = table.strip('`')
        elif line.startswith('REFERENCES'):
            _, table, columns, _ = line.split()
            parent_column = columns.strip('()')
            parent_table = table.strip('`')

    # Add an edge between the parent and child table
    edge = pydot.Edge(parent_table, child_table, label=f'{parent_column} -> {child_column}')
    graph.add_edge(edge)
    graph.write_png("hr_diagram.png")