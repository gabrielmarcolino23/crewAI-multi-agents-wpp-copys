from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
from crewai_tools import PDFSearchTool
from langchain_openai import ChatOpenAI
load_dotenv()

@CrewBase
class CopyWriterCrew():
	"""CopyWriter crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	def __init__(self):
		self.openai_llm = ChatOpenAI(model="gpt-4o-mini")

	@agent
	def copywriter(self) -> Agent:
		return Agent(
			config=self.agents_config['copywriter'],
			llm = self.openai_llm,
			verbose=True
		)

	@task
	def copywriter_task(self) -> Task:
		return Task(
			config=self.tasks_config['copywriter_task'],
			tool=PDFSearchTool(),
			agent=self.copywriter(),
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the CopyWriter crew"""
		return Crew(
			agents=self.agents, 
			tasks=self.tasks, 
			process=Process.sequential,
			verbose=True,
		)