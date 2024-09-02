from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
load_dotenv()
import yaml
import os

@CrewBase
class CopyWriterCrew():
	"""CopyWriter crew"""

	def __init__(self):
		with open('config/agents.yaml', 'r', encoding='utf-8') as file:
			self.agents_config = yaml.safe_load(file)

		with open('config/tasks.yaml', 'r', encoding='utf-8') as file:
			self.tasks_config = yaml.safe_load(file)

		self.openai_llm = ChatOpenAI(model="gpt-4o-mini")

	@agent
	def copywriter(self) -> Agent:
		return Agent(
			config=self.agents_config['copywriter'],
			llm = self.openai_llm,
		)

	@task
	def copywriter_task(self) -> Task:
		return Task(
			config=self.tasks_config['copywriter_task'],
			agent=self.copywriter(),
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the CopyWriter crew"""
		return Crew(
			agents=self.agents, 
			tasks=self.tasks, 
			process=Process.sequential,
			verbose=False,
		)