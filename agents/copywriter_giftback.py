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

def copywriter_giftback():

        # Criar agentes e tarefas a partir da configuração YAML
    copywriter_giftback_agent = Agent(
        role=agents_config["copywriter_giftback_agent"]["role"],
        goal=agents_config["copywriter_giftback_agent"]["goal"],
        backstory=agents_config["copywriter_giftback_agent"]["backstory"],
        memory=agents_config["copywriter_giftback_agent"]["memory"],
        verbose=agents_config["copywriter_giftback_agent"]["verbose"],
        stream=agents_config["copywriter_giftback_agent"]["stream"],
        tools=[pdf_tool],
    )

    copywriter_giftback_task = Task(
        description=tasks_config['copywriter_giftback_agent_task']['description'],
        expected_output=tasks_config['copywriter_giftback_agent_task']['expected_output'],
        agent= copywriter_giftback_agent
    )

    return copywriter_giftback_agent, copywriter_giftback_task


