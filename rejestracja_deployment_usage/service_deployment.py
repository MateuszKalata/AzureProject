from azureml.core.webservice import AciWebservice, Webservice
from inference_config import ws, m_inference_config
from azureml.core.model import Model

deployment_config = AciWebservice.deploy_configuration()

model = Model(ws, id="test_model_1:1")

service = Model.deploy(ws, "mytestservice", [model], m_inference_config, deployment_config)
service.wait_for_deployment(show_output = True)
print(service.state)