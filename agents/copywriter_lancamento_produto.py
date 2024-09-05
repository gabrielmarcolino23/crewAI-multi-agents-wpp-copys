import yaml
from crewai import Agent, Task
from crewai_tools import PDFSearchTool

from dotenv import load_dotenv

load_dotenv()

# Carregar arquivo YAML
with open("config/agents.yaml", "r", encoding="utf-8") as file:
    agents_config = yaml.safe_load(file)

with open("config/tasks.yaml", "r", encoding="utf-8") as file:
    tasks_config = yaml.safe_load(file)

variaveis_tool = PDFSearchTool(pdf="./docs/variaveis.pdf")
exemplos_tool = PDFSearchTool(pdf="./docs/exemplos.pdf")


def copywriter_lancamento_produto():

    # Criar agentes e tarefas a partir da configuração YAML
    copywriter_lancamento_produto_agent = Agent(
        role=agents_config["copywriter_lancamento_produto"]["role"],
        goal=agents_config["copywriter_lancamento_produto"]["goal"],
        backstory=agents_config["copywriter_lancamento_produto"]["backstory"],
        memory=agents_config["copywriter_lancamento_produto"]["memory"],
        verbose=agents_config["copywriter_lancamento_produto"]["verbose"],
        stream=agents_config["copywriter_lancamento_produto"]["stream"],
        tools=[variaveis_tool, exemplos_tool],
    )

    copywriter_lancamento_produto_task = Task(
        description=tasks_config["copywriter_lancamento_produto_task"]["description"],
        expected_output=tasks_config["copywriter_lancamento_produto_task"][
            "expected_output"
        ],
        agent=copywriter_lancamento_produto_agent,
    )

    return copywriter_lancamento_produto_agent, copywriter_lancamento_produto_task
