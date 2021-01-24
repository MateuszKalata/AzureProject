import json
import numpy as np
import os
from sentence_transformers import SentenceTransformer


def init():
    global model
    model_path = os.path.join(os.getenv("AZUREML_MODEL_DIR"), "test1.pkl")
    model = SentenceTransformer(model_path)

def run(data):
    try:
        data = np.array(json.loads(data))
        embeddings = model.encode(sentences)

        cos_sim = util.pytorch_cos_sim(embeddings, embeddings)
        all_sentence_combinations = []
        for i in range(len(cos_sim)-1):
            for j in range(i+1, len(cos_sim)):
                all_sentence_combinations.append([cos_sim[i][j], i, j])

        return all_sentence_combinations
        
    except Exception as e:
        error = str(e)
        return error