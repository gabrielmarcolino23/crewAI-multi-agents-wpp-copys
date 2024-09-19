import yaml
from crewai import Agent, Task
from utils.ragExamplesWpp import RagExamplesWpp
from utils.zoppyVariables_tool import ZoppyVariablesSearchTool
from dotenv import load_dotenv

load_dotenv()

# Carregar arquivo YAML
with open("config/agents.yaml", "r", encoding="utf-8") as file:
    agents_config = yaml.safe_load(file)

with open("config/tasks.yaml", "r", encoding="utf-8") as file:
    tasks_config = yaml.safe_load(file)

variaveis_tool = ZoppyVariablesSearchTool(pdf="./docs/variaveis.pdf")
exemplos_tool = RagExamplesWpp(pdf="./docs/exemplos.pdf")


def copywriter_giftback():
    # Criar o agente com as ferramentas
    copywriter_giftback_agent = Agent(
        role=agents_config["copywriter_giftback"]["role"],
        goal=agents_config["copywriter_giftback"]["goal"],
        backstory=agents_config["copywriter_giftback"]["backstory"],
        memory=agents_config["copywriter_giftback"]["memory"],
        verbose=agents_config["copywriter_giftback"]["verbose"],
        stream=agents_config["copywriter_giftback"]["stream"],
        tools=[variaveis_tool, exemplos_tool],
    )

    copywriter_giftback_task = Task(
        description=tasks_config["copywriter_giftback_task"]["description"],
        expected_output=tasks_config["copywriter_giftback_task"]["expected_output"],
        agent=copywriter_giftback_agent,
    )

    return copywriter_giftback_agent, copywriter_giftback_task
