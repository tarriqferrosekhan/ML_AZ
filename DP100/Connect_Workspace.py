
from dotenv import load_dotenv
import os
from azure.ai.ml import MLClient
from azure.ai.ml.entities import Workspace
from azure.identity import DefaultAzureCredential , InteractiveBrowserCredential,ClientSecretCredential
from azure.ai.ml import command

os.system('cls')

load_dotenv()
subscription_id=os.getenv("subscription_id")
tenant_id=os.getenv("tenant_id")
client_id=os.getenv("client_id")
secret_id=os.getenv("secret_id")

resource_group="DP100"
workspace_name="mlw_test"


_ClientSecretCredential = ClientSecretCredential(
    tenant_id=tenant_id,
    client_id=client_id,
    client_secret=secret_id
)

ml_client = MLClient(
    credential=_ClientSecretCredential, 
    subscription_id=subscription_id, 
    resource_group_name=resource_group
)


# # configure job
# job = command(
#     code="./src",
#     command="python train.py",
#     environment="AzureML-sklearn-0.24-ubuntu18.04-py37-cpu@latest",
#     compute="aml-cluster",
#     experiment_name="train-model"
# )

# connect to workspace and submit job
_workSpace = ml_client.workspaces.get(workspace_name)
print("="*100)
print(_workSpace.display_name)
print(_workSpace.location)
print(_workSpace.storage_account)
print(_workSpace.application_insights)
print(_workSpace.key_vault)
print(_workSpace.container_registry)



print("="*100)

