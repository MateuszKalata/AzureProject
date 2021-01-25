import sqlite3
from sentence_transformers import SentenceTransformer, util
from sample_data.initial_insert import INITIAL_DATA
model = SentenceTransformer('paraphrase-distilroberta-base-v1')

conn = sqlite3.connect("azure_project_test.db")
cursor = conn.cursor()

index = 0
for article in INITIAL_DATA:
    emb = model.encode(article)

    insert_query = """
        INSERT INTO embeddings (
            source_file
    """

    for i in range(768):
        insert_query += ",v" + str(i)

    insert_query += (") VALUES ('article" + str(index) + "'")
    index += 1

    for i in range(768):
        insert_query += ("," + str(emb[i]))

    insert_query += ")"
    cursor.execute(insert_query)

    # with open("query" + str(index) + ".txt", "w") as f:
    #     f.write(insert_query)
    
conn.commit()

conn.close()