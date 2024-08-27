import streamlit as st
import os
from agents.copywriter import copywriter
from crewai import Crew, Process

# Configuração do modelo OpenAI
os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini-2024-07-18"

st.title("Interface do Copywriter")

tipo_campanha = st.selectbox(
    "Tipo de Campanha de WhatsApp",
    options=["Data Comemorativa", "Lançamento de produto", "Lançamento de coleção",
              "Liquidação", "Carrinho Abandonado", "NPS", 
              "Aniversário Cliente","Pós-Venda", "Giftback"]
)

# Criação de campos de input para o usuário
nome_loja = st.text_input("Nome da Loja", value="")
segmento = st.text_input("Segmento", value="")
publico_alvo = st.text_input("Público-Alvo", value="")
tom_de_voz = st.text_input("Tom de Voz", value="")
objetivo_campanha = st.text_input("Objetivo da Campanha", value="")



# Botão para processar os dados
if st.button("Gerar Copy"):
    # Inputs do usuário ou de algum fluxo de dados
    dados_cliente = {
        "nome_loja": nome_loja,
        "segmento": segmento,
        "publico_alvo": publico_alvo,
        "tom_de_voz": tom_de_voz,
        "objetivo_campanha": objetivo_campanha,
        "tipo_campanha": tipo_campanha
    }

    copywriter_agent, copywriter_task = copywriter()

    crew = Crew(
        agents=[copywriter_agent],
        tasks=[copywriter_task],
        process=Process.sequential
    )

    # Interpolar apenas placeholders {exemplo}, não {{exemplo}}
    resultado_final = crew.kickoff(inputs=dados_cliente)

    st.write("**Resultado Final:**")
    st.write(resultado_final)
