import os
from agents.copywriter import copywriter
#from utils.helper_functions import process_and_format_result

from crewai import Crew, Process


os.environ["OPENAI_MODEL_NAME"]="gpt-4o-mini-2024-07-18"

# Inputs do usuário ou de algum fluxo de dados
dados_cliente = {
    "nome_loja": "Vorr",
    "segmento": "moda feminina",
    "publico_alvo": "jovens adultas",
    "tom_de_voz": "descontraído e amigável",
    "objetivo_campanha": "liquidação de verão"
}

copywriter_agent, copywriter_task = copywriter()

crew = Crew(
    agents=[copywriter_agent],
    tasks=[copywriter_task],
    process=Process.sequential
)

resultado_final = crew.kickoff(inputs=dados_cliente)

print(resultado_final)

'''
formatted_result = process_and_format_result(resultado_final, dados_cliente)
print(formatted_result)
'''