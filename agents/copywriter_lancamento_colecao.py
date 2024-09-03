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

pdf_tool = PDFSearchTool(pdf='./docs/copy_tecnicas.pdf')

def copywriter_lacamento_colecao():

        # Criar agentes e tarefas a partir da configuração YAML
    copywriter_lancamento_colecao_agent = Agent(
        role=agents_config["copywriter_lancamento_colecao_agent"]["role"],
        goal=agents_config["copywriter_lancamento_colecao_agent"]["goal"],
        backstory=agents_config["copywriter_lancamento_colecao_agent"]["backstory"],
        memory=agents_config["copywriter_lancamento_colecao_agent"]["memory"],
        verbose=agents_config["copywriter_lancamento_colecao_agent"]["verbose"],
        stream=agents_config["copywriter_lancamento_colecao_agent"]["stream"],
        tools=[pdf_tool],
    )

    copywriter_lancamento_colecao_task = Task(
        description=tasks_config['copywriter_lancamento_colecao_task']['description'],
        expected_output=tasks_config['copywriter_lancamento_colecao_task']['expected_output'],
        agent= copywriter_lancamento_colecao_agent
    )

    return copywriter_lancamento_colecao_agent, copywriter_lancamento_colecao_task
