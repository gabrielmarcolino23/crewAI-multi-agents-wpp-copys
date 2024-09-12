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

def copywriter_whatsApp():

        # Criar agentes e tarefas a partir da configuração YAML
    copywriter_whatsApp_agent = Agent(
        role=agents_config["copywriter_whatsApp"]["role"],
        goal=agents_config["copywriter_whatsApp"]["goal"],
        backstory=agents_config["copywriter_whatsApp"]["backstory"],
        memory=agents_config["copywriter_whatsApp"]["memory"],
        verbose=agents_config["copywriter_whatsApp"]["verbose"],
        stream=agents_config["copywriter_whatsApp"]["stream"],
        tools=[variaveis_tool, exemplos_tool],
    )

    copywriter_whatsApp_task = Task(
        description=tasks_config['copywriter_whatsApp_task']['description'],
        expected_output=tasks_config['copywriter_whatsApp_task']['expected_output'],
        agent= copywriter_whatsApp_agent
    )

    return copywriter_whatsApp_agent, copywriter_whatsApp_task
