# Training model (or fine-tuning)

from sentence_transformers import SentenceTransformer, InputExample, losses
from torch.utils.data import DataLoader
import torch

#Define the model. Either from scratch of by loading a pre-trained model
model = SentenceTransformer('paraphrase-distilroberta-base-v1')

#Define your train examples. You need more than just two examples...
train_examples = [InputExample(texts=['My first sentence', 'My second sentence'], label=0.8),
    InputExample(texts=['Another pair', 'Unrelated sentence'], label=0.3)]

#Define your train dataset, the dataloader and the train loss
train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=16)
train_loss = losses.CosineSimilarityLoss(model)

#Tune the model
model.fit(train_objectives=[(train_dataloader, train_loss)], epochs=1, warmup_steps=100)

model.save("./models/test1.pkl")
#model.eval()

# Evaluating training accuracy
# https://www.sbert.net/docs/training/overview.html#evaluators