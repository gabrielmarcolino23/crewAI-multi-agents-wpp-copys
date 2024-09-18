import yaml
from crewai import Agent, Task
from utils.ragExamplesWpp import RagExamplesWpp
from utils.zoppyVariables_tool import ZoppyVariablesSearchTool
from dotenv import load_dotenv
load_dotenv()

# Carregar arquivo YAML
with open('config/agents.yaml', 'r', encoding='utf-8') as file:
    agents_config = yaml.safe_load(file)

with open('config/tasks.yaml', 'r', encoding='utf-8') as file:
    tasks_config = yaml.safe_load(file)

variaveis_tool = ZoppyVariablesSearchTool(pdf="./docs/variaveis.pdf")
exemplos_tool = RagExamplesWpp(pdf="./docs/exemplos.pdf")  

def copywriter_aniversario_cliente():

    # Criar agentes e tarefas a partir da configuração YAML
    copywriter_aniversario_cliente_agent = Agent(
        role=agents_config["copywriter_aniversario_cliente"]["role"],
        goal=agents_config["copywriter_aniversario_cliente"]["goal"],
        backstory=agents_config["copywriter_aniversario_cliente"]["backstory"],
        memory=agents_config["copywriter_aniversario_cliente"]["memory"],
        verbose=agents_config["copywriter_aniversario_cliente"]["verbose"],
        stream=agents_config["copywriter_aniversario_cliente"]["stream"],
        tools=[variaveis_tool, exemplos_tool],
    )

    copywriter_aniversario_cliente_task = Task(
        description=tasks_config['copywriter_aniversario_cliente_task']['description'],
        expected_output=tasks_config['copywriter_aniversario_cliente_task']['expected_output'],
        agent= copywriter_aniversario_cliente_agent
    )

    return copywriter_aniversario_cliente_agent, copywriter_aniversario_cliente_task
