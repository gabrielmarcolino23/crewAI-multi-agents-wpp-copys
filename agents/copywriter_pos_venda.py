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

def copywriter_pos_venda():
    # Criar o agente com as ferramentas
    copywriter_pos_venda_agent = Agent(
        role=agents_config["copywriter_pos_venda"]["role"],
        goal=agents_config["copywriter_pos_venda"]["goal"],
        backstory=agents_config["copywriter_pos_venda"]["backstory"],
        memory=agents_config["copywriter_pos_venda"]["memory"],
        verbose=agents_config["copywriter_pos_venda"]["verbose"],
        stream=agents_config["copywriter_pos_venda"]["stream"],
        tools=[variaveis_tool, exemplos_tool],
    )

    copywriter_pos_venda_task = Task(
        description=tasks_config["copywriter_pos_venda_task"]["description"],
        expected_output=tasks_config["copywriter_pos_venda_task"]["expected_output"],
        agent=copywriter_pos_venda_agent,
        
    )

    return copywriter_pos_venda_agent, copywriter_pos_venda_task
