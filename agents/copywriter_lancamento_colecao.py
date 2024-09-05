import yaml
from crewai import Agent, Task
from crewai_tools import PDFSearchTool

from dotenv import load_dotenv
load_dotenv()

# Carregar arquivo YAML
with open('config/agents.yaml', 'r', encoding='utf-8') as file:
    agents_config = yaml.safe_load(file)

with open('config/tasks.yaml', 'r', encoding='utf-8') as file:
    tasks_config = yaml.safe_load(file)

variaveis_tool = PDFSearchTool(pdf="./docs/variaveis.pdf")
exemplos_tool = PDFSearchTool(pdf="./docs/exemplos.pdf")

def copywriter_lacamento_colecao():

        # Criar agentes e tarefas a partir da configuração YAML
    copywriter_lancamento_colecao_agent = Agent(
        role=agents_config["copywriter_lancamento_colecao"]["role"],
        goal=agents_config["copywriter_lancamento_colecao"]["goal"],
        backstory=agents_config["copywriter_lancamento_colecao"]["backstory"],
        memory=agents_config["copywriter_lancamento_colecao"]["memory"],
        verbose=agents_config["copywriter_lancamento_colecao"]["verbose"],
        stream=agents_config["copywriter_lancamento_colecao"]["stream"],
        tools=[variaveis_tool, exemplos_tool],
    )

    copywriter_lancamento_colecao_task = Task(
        description=tasks_config['copywriter_lancamento_colecao_task']['description'],
        expected_output=tasks_config['copywriter_lancamento_colecao_task']['expected_output'],
        agent= copywriter_lancamento_colecao_agent
    )

    return copywriter_lancamento_colecao_agent, copywriter_lancamento_colecao_task
