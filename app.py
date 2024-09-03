import streamlit as st
import os
from agents.copywriter import copywriter
from crewai import Crew, Process

from dotenv import load_dotenv
load_dotenv()

# Configuração do modelo OpenAI
os.environ["OPENAI_MODEL_NAME"] = "gpt-4o"

# Configuração da página e título
st.set_page_config(page_title="Zoppy CopyAI", page_icon="🔵", layout="wide")

#Titulo pagina
st.title("Zoppy - Copywriter")

# Organização da interface em duas colunas principais
col1, col2 = st.columns([3, 2], gap="large")

with col1:
    st.subheader("Preencha os detalhes para gerar a copy")
    
    # Inputs do Usuário
    tipo_campanha = st.selectbox(
        "Tipo de Campanha de WhatsApp",
        options=["Data Comemorativa", "Lançamento de produto", "Lançamento de coleção", 
                 "Aniversário Cliente","Giftback"]
    )

    nome_loja = st.text_input("Nome da Loja", placeholder="Digite o nome da loja")
    segmento = st.text_input("Segmento", placeholder="Digite o segmento de mercado (ex: Moda, Tecnologia)")
    publico_alvo = st.text_input("Público-Alvo", placeholder="Descreva o público-alvo (ex: Jovens adultos, Profissionais)")
    tom_de_voz = st.selectbox("Tom de Voz", options=["Formal", "Informal","Divertido","Amigável"], index=0)
    objetivo_campanha = st.text_input("Objetivo da Copy", placeholder="Qual o seu objetivo final ao enviar esta mensagem?")

with col2:
    st.subheader("Copy Gerada")

    # Inputs adicionais para a descrição do modelo de copy
    nome_modelo = st.text_input("Nome do Modelo", placeholder="Dê um nome para o modelo")
    descricao_modelo = st.text_area("Descrição", placeholder="Dê uma descrição para o modelo", height=100)

    # Botão para Processar os Dados e Adicionar o Modelo
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
            process=Process.sequential,
            verbose=False
        )

        # Gerar a copy com base nos inputs fornecidos
        resultado_final = crew.kickoff(inputs=dados_cliente)

        # Exibir o resultado na interface
        st.text_area("Resultado Final", resultado_final, height=300)

        # Simulação de adição do modelo (ajuste conforme necessário)
        st.success(f"Modelo '{nome_modelo}' adicionado com sucesso!")
    else:
        st.info("Preencha os dados acima e clique em 'Gerar Copy' para criar sua campanha e adicionar o modelo.")

# Rodapé com informações adicionais
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<footer style='text-align: center; color: #4a148c;'>"
    "© 2024 TonyWriter. Todos os direitos reservados."
    "</footer>",
    unsafe_allow_html=True
)
