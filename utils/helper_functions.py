# utils/formatting.py

def format_output(output_text, client_first_name):
    # Converter para string, caso não seja já uma string
    formatted_output = str(output_text)

    # Substituir placeholders por valores reais
    formatted_output = formatted_output.replace("{client_first_name}", client_first_name)

    # Aplicar formatação adicional (quebras de linha, espaçamento)
    formatted_output = formatted_output.strip()  # Remover espaços desnecessários no início/fim
    formatted_output = "\n\n".join(formatted_output.split("\n"))  # Adicionar espaçamento entre linhas

    return formatted_output

def process_result(resultado_final, dados_cliente):
    # Acessar o primeiro resultado da tarefa e pegar o atributo 'raw', que contém o texto gerado
    output_text = resultado_final.tasks_output[0].raw

    # Converter o conteúdo de 'raw' para string e aplicar formatação
    formatted_result = format_output(output_text, dados_cliente["client_first_name"])

    return formatted_result

# utils/formatting.py

def process_and_format_result(resultado_final, dados_cliente):
    # Acessar o primeiro resultado da tarefa e pegar o atributo 'raw', que contém o texto gerado
    output_text = str(resultado_final.tasks_output[0].raw)  # Converter para string, caso não seja uma string

    # Substituir placeholders por valores reais
    formatted_output = output_text.replace("{client_first_name}", dados_cliente["client_first_name"])

    # Aplicar formatação adicional (quebras de linha, espaçamento)
    formatted_output = formatted_output.strip()  # Remover espaços desnecessários no início/fim
    formatted_output = "\n\n".join(formatted_output.split("\n"))  # Adicionar espaçamento entre linhas

    return formatted_output

