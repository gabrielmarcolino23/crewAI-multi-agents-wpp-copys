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

pdf_tool = PDFSearchTool(pdf='./docs/variaveis.pdf')

def copywriter_giftback():

        # Criar agentes e tarefas a partir da configuração YAML
    copywriter_giftback_agent = Agent(
        role=agents_config["copywriter_giftback"]["role"],
        goal=agents_config["copywriter_giftback"]["goal"],
        backstory=agents_config["copywriter_giftback"]["backstory"],
        memory=agents_config["copywriter_giftback"]["memory"],
        verbose=agents_config["copywriter_giftback"]["verbose"],
        stream=agents_config["copywriter_giftback"]["stream"],
        tools=[pdf_tool],
    )

    copywriter_giftback_task = Task(
        description=tasks_config['copywriter_giftback_task']['description'],
        expected_output=tasks_config['copywriter_giftback_task']['expected_output'],
        agent= copywriter_giftback_agent
    )

    return copywriter_giftback_agent, copywriter_giftback_task


