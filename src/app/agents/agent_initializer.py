az ad sp create-for-rbac --name "TechWorkshopL300AzureAI" --json-auth --role contributor --scopes /subscriptions/69f14792-2272-4f1d-96ff-44da16ea5f8a/resourceGroups/rg-techworkshop300from typing import List, Any
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition
from dotenv import load_dotenv

load_dotenv()

def initialize_agent(project_client : AIProjectClient, model : str, name : str, description : str, instructions : str, tools : List[Any]):
    with project_client:
        agent = project_client.agents.create_version(
            agent_name=name,
            description=description,
            definition=PromptAgentDefinition(
                model=model,
                instructions=instructions,
                tools=tools
            )
        )
        print(f"Created {name} agent, ID: {agent.id}")
