import streamlit as st
import os
from agents.copywriter import copywriter
from crewai import Crew, Process

# Configuração do modelo OpenAI
os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini-2024-07-18"

st.title("Interface do Copywriter")

# Criação de campos de input para o usuário
nome_loja = st.text_input("Nome da Loja", value="Vorr")
segmento = st.text_input("Segmento", value="moda feminina")
publico_alvo = st.text_input("Público-Alvo", value="jovens adultas")
tom_de_voz = st.text_input("Tom de Voz", value="descontraído e amigável")
objetivo_campanha = st.text_input("Objetivo da Campanha", value="liquidação de verão")



# Botão para processar os dados
if st.button("Gerar Copy"):
    # Inputs do usuário ou de algum fluxo de dados
    dados_cliente = {
        "nome_loja": nome_loja,
        "segmento": segmento,
        "publico_alvo": publico_alvo,
        "tom_de_voz": tom_de_voz,
        "objetivo_campanha": objetivo_campanha
    }

    copywriter_agent, copywriter_task = copywriter()

    crew = Crew(
        agents=[copywriter_agent],
        tasks=[copywriter_task],
        process=Process.sequential
    )

    resultado_final = crew.kickoff(inputs=dados_cliente)

    st.write("**Resultado Final:**")
    st.write(resultado_final)

