import os
from agents.copywriter_giftback import copywriter_giftback
from agents.copywriter_data_comemorativa import copywriter_data_comemorativa
#from utils.helper_functions import process_and_format_result
from dotenv import load_dotenv
load_dotenv()

from crewai import Crew, Process


os.environ["OPENAI_MODEL_NAME"]="gpt-4o"

# Inputs do usuário ou de algum fluxo de dados
dados_cliente = {
    "nome_loja": "Vorr",
    "segmento": "moda feminina",
    "publico_alvo": "jovens adultas",
    "tom_voz": "amigável",
    "objetivo_campanha": "Promoção de 20% off em todos os produtos para o Dia das Mães",
    "tipo_campanha": "data_comemorativa",
    'data_comemorativa': "Dia das Mães"
}

copywriter_agent, copywriter_task = copywriter_data_comemorativa()
#   = copywriter_data_comemorativa()

crew = Crew(
    agents=[copywriter_agent],
    tasks=[copywriter_task],
    process=Process.sequential,
    verbose=True
)

resultado_final = crew.kickoff(inputs=dados_cliente)

print(resultado_final)

'''
formatted_result = process_and_format_result(resultado_final, dados_cliente)
print(formatted_result)
'''