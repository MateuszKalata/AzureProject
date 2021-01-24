from sentence_transformers import SentenceTransformer, InputExample, losses
from torch.utils.data import DataLoader
import torch
from azureml.core import Workspace
from azureml.core.authentication import AzureCliAuthentication
from azureml.core.model import Model

interactive_auth = AzureCliAuthentication(cloud="AzureCloud")

#Define the model. Either from scratch of by loading a pre-trained model
# model = SentenceTransformer('paraphrase-distilroberta-base-v1')

# model.save("./models/test1.pkl")

#auth = ServicePrincipalAuthentication(tenant_id="3b50229c-cd78-4588-9bcf-97b7629e2f0f", service_principal_id="278664e7-3a93-48c1-b3bf-6e06d99e13cb", service_principal_password="1Qaz3Edc5Tgb")
ws = Workspace.get(name="Machine-Learning", subscription_id="ecadfaca-baf6-4554-b903-5d4de6dea911", resource_group="Projekt-Azure", auth=interactive_auth)
#ws = Workspace.from_config(path="./config/ws_config.json", auth=interactive_auth)
#ws.write_config(path="./config", file_name="ws_config.json")

model = Model.register(workspace=ws, model_path="./models/test1.pkl", model_name="test_model_1")