import yaml
from crewai import Agent, Task
from crewai_tools import PDFSearchTool

from dotenv import load_dotenv
load_dotenv()


pdf_tool = PDFSearchTool(pdf='./docs/variaveis.pdf')


# Carregar arquivo YAML
with open('config/agents.yaml', 'r', encoding='utf-8') as file:
    agents_config = yaml.safe_load(file)

with open('config/tasks.yaml', 'r', encoding='utf-8') as file:
    tasks_config = yaml.safe_load(file)

def copywriter():
    # Criar agentes e tarefas a partir da configuração YAML
    copywriter_agent = Agent(
        role=agents_config['copywriter']['role'],
        goal=agents_config['copywriter']['goal'],
        backstory=agents_config['copywriter']['backstory'],
        memory=agents_config['copywriter']['memory'],
        verbose=agents_config['copywriter']['verbose'],
        stream=True,
        tools=[pdf_tool]
    )

    copywriter_task = Task(
        description=tasks_config['copywriter_task']['description'],
        expected_output=tasks_config['copywriter_task']['expected_output'],
        agent=copywriter_agent
    )

    return copywriter_agent, copywriter_task
