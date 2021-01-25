from azureml.core.webservice import AciWebservice, Webservice
from inference_config import ws, m_inference_config
from azureml.core.model import Model

#deployment_config = AciWebservice.deploy_configuration(memory_gb=4)

#model = Model(ws, id="test_model_1:1")

service = Webservice(ws, "mytestservice2")
service.update(inference_config=m_inference_config)
service.wait_for_deployment(show_output = True)
print(service.state)