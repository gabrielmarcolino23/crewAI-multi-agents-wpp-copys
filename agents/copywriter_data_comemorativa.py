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

def copywriter_data_comemorativa():
    # Criar agentes e tarefas a partir da configuração YAML
    copywriter_data_comemorativa_agent = Agent(
        role=agents_config["copywriter_data_comemorativa"]["role"],
        goal=agents_config["copywriter_data_comemorativa"]["goal"],
        backstory=agents_config["copywriter_data_comemorativa"]["backstory"],
        memory=agents_config["copywriter_data_comemorativa"]["memory"],
        verbose=agents_config["copywriter_data_comemorativa"]["verbose"],
        stream=agents_config["copywriter_data_comemorativa"]["stream"],
        tools=[variaveis_tool, exemplos_tool],
    )

    copywright_data_comemorativa_task = Task(
        description=tasks_config['copywright_data_comemorativa_task']['description'],
        expected_output=tasks_config['copywright_data_comemorativa_task']['expected_output'],
        agent=copywriter_data_comemorativa_agent
    )

    return copywriter_data_comemorativa_agent, copywright_data_comemorativa_task
