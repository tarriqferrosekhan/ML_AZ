
from dotenv import load_dotenv
import os
from azure.ai.ml import MLClient
from azure.ai.ml.entities import Workspace
from azure.identity import DefaultAzureCredential , InteractiveBrowserCredential,ClientSecretCredential

os.system('cls')

load_dotenv()
subscription_id=os.getenv("subscription_id")
tenant_id=os.getenv("tenant_id")
client_id=os.getenv("client_id")
secret_id=os.getenv("secret_id")

resource_group="DP100"
workspace_name="mlw_test"


_interactive_credential = InteractiveBrowserCredential()
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

workspace = Workspace(
    name=workspace_name,
    location="centralindia",  # Or your desired Azure region
    description="My new Azure ML workspace",
    tags={"project": "my_ml_project"},
    display_name="My ML Workspace",
    hbi_workspace=False, # Set to True for High Business Impact data
)

# Create the workspace
ws_result = ml_client.workspaces.begin_create(workspace).result()
print(f"Workspace created: {ws_result.name}")