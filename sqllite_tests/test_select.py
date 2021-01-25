import sqlite3
from sentence_transformers import SentenceTransformer, util

search = "Bieg dystansowy 800 metrów"

model = SentenceTransformer('paraphrase-distilroberta-base-v1')
conn = sqlite3.connect("azure_project_test.db")

emb = model.encode(search)

cursor = conn.cursor()

#cursor.execute("""SELECT e.source_file, ABS(e.v0 - 1) + ABS(e.v1 - 1) AS 'distance', e.v0, e.v1 FROM embeddings e""")
#cursor.execute("""SELECT * FROM embeddings""")

select_query = """
    SELECT e.source_file,
"""

for i in range(768):
    if i != 0:
        select_query += ("+ABS(e.v" + str(i) + "-(" + str(emb[i]) + "))")
    else:
        select_query += ("ABS(e.v" + str(i) + "-(" + str(emb[i]) + "))")

select_query += "AS 'distance' FROM embeddings e"

with open("select_query.txt", "w") as f:
    f.write(select_query)

cursor.execute(select_query)

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()