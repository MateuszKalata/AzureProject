import sqlite3

conn = sqlite3.connect("azure_project_test.db")

cursor = conn.cursor()

create_query = '''
    CREATE TABLE embeddings (
        source_file TEXT
'''

for i in range(768):
    create_query += ",v" + str(i) + " REAL"

create_query += ")"
cursor.execute(create_query)
conn.close()

# with open("query.txt", "w") as f:
#     f.write(create_query)