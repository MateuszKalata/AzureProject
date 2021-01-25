from azureml.core.environment import Environment
from azureml.core.model import InferenceConfig
from azureml.core import Workspace
from azureml.core.authentication import AzureCliAuthentication

interactive_auth = AzureCliAuthentication(cloud="AzureCloud")
ws = Workspace.get(name="Machine-Learning", subscription_id="ecadfaca-baf6-4554-b903-5d4de6dea911", resource_group="Projekt-Azure", auth=interactive_auth)

env = Environment.get(ws, "AzureML-Minimal").clone("test_env")

for pip_package in [ "sentence-transformers" ]:
    env.python.conda_dependencies.add_pip_package(pip_package)

m_inference_config = InferenceConfig(entry_script="./entry_script.py", environment=env)