import os
from agents.copywriter import copywriter
from utils.helper_functions import process_and_format_result

from crewai import Crew, Process

os.environ["OPENAI_MODEL_NAME"]="gpt-4o-mini-2024-07-18"

# Inputs do usuário ou de algum fluxo de dados
dados_cliente = {
    "client_first_name": "Ana",
    "nome_loja": "Voor",
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

formatted_result = process_and_format_result(resultado_final, dados_cliente)

print(formatted_result)


#print(resultado_final)

'''
def format_output(output_text, client_first_name):
    # Converter para string, caso não seja já uma string
    formatted_output = str(output_text)

    # Substituir placeholders por valores reais
    formatted_output = formatted_output.replace("{client_first_name}", client_first_name)

    # Aplicar formatação adicional (quebras de linha, espaçamento)
    formatted_output = formatted_output.strip()  # Remover espaços desnecessários no início/fim
    formatted_output = "\n\n".join(formatted_output.split("\n"))  # Adicionar espaçamento entre linhas

    return formatted_output

'''
#formatted_result = format_output(resultado_final, dados_cliente["client_first_name"])
#print(formatted_result)

#print(dir(resultado_final))

#print(resultado_final.tasks_output)  # Verificar o conteúdo de tasks_output

# Verificar o conteúdo de tasks_output

# Acessar o primeiro resultado da tarefa e pegar o atributo 'raw', que contém o texto gerado
#output_text = resultado_final.tasks_output[0].raw
#formatted_result = format_output(formatted_result, dados_cliente["client_first_name"])

#print(formatted_result)