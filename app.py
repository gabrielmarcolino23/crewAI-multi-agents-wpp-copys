import streamlit as st
import os
from agents.copywriter_data_comemorativa import copywriter_data_comemorativa
from crewai import Crew, Process
from dotenv import load_dotenv
# from langsmith import Client

load_dotenv()

# Configuração do modelo OpenAI
os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini-2024-07-18   "

# Inicialização do cliente LangSmith para feedback
# client = Client(os.getenv("LANGSMITH_API_KEY"))

# Configuração da página e título
st.set_page_config(page_title="Zoppy CopyAI", page_icon="🔵", layout="wide")

# Título da página
st.title("Zoppy - Copywriter")

# Organização da interface em duas colunas principais
col1, col2 = st.columns([3, 2], gap="large")

with col1:
    st.subheader("Preencha os detalhes para gerar a copy")
    
    # Input principal: Tipo de campanha
    tipo_campanha = st.selectbox(
        "Tipo de Campanha de WhatsApp",
        options=["Data Comemorativa", "Lançamento de produto", "Lançamento de coleção", 
                 "Aniversário Cliente", "Giftback"]
    )

    # Inputs dinâmicos que aparecem logo após a seleção do tipo de campanha
    if tipo_campanha == "Data Comemorativa":
        data_comemorativa = st.text_input("Data Comemorativa", placeholder="Ex: Dia das Mães, Natal")
    
    elif tipo_campanha == "Lançamento de produto":
        nome_produto = st.text_input("Nome do Produto", placeholder="Digite o nome do produto")
        descricao_produto = st.text_area("Descrição do Produto", placeholder="Descreva o produto", height=100)
    
    elif tipo_campanha == "Lançamento de coleção":
        nome_colecao = st.text_input("Nome da Coleção", placeholder="Digite o nome da coleção")
        descricao_colecao = st.text_area("Descrição da Coleção", placeholder="Descreva a coleção", height=100)

    # Inputs comuns a todas as campanhas
    nome_loja = st.text_input("Nome da Loja", placeholder="Digite o nome da loja")
    segmento = st.text_input("Segmento", placeholder="Digite o segmento de mercado (ex: Moda, Tecnologia)")
    publico_alvo = st.text_input("Público-Alvo", placeholder="Descreva o público-alvo (ex: Jovens adultos, Profissionais)")
    tom_de_voz = st.selectbox("Tom de Voz", options=["Formal", "Informal", "Divertido", "Amigável"], index=0)
    objetivo_campanha = st.text_input("Objetivo da Copy", placeholder="Qual o seu objetivo final ao enviar esta mensagem?")

with col2:
    st.subheader("Copy Gerada")

    # Inputs adicionais para a descrição do modelo de copy
    nome_modelo = st.text_input("Nome do Modelo", placeholder="Dê um nome para o modelo")
    descricao_modelo = st.text_area("Descrição", placeholder="Dê uma descrição para o modelo", height=100)

    # Botão para Processar os Dados e Adicionar o Modelo
    if st.button("Gerar Copy"):
        # Coleta dos dados comuns para enviar ao agente
        dados_cliente = {
            "nome_loja": nome_loja,
            "segmento": segmento,
            "publico_alvo": publico_alvo,
            "tom_voz": tom_de_voz,
            "objetivo_campanha": objetivo_campanha,
            "tipo_campanha": tipo_campanha
        }

        # Adiciona campos específicos dependendo do tipo de campanha
        if tipo_campanha == "Data Comemorativa":
            dados_cliente["data_comemorativa"] = data_comemorativa
        elif tipo_campanha == "Lançamento de produto":
            dados_cliente["nome_produto"] = nome_produto
            dados_cliente["descricao_produto"] = descricao_produto
        elif tipo_campanha == "Lançamento de coleção":
            dados_cliente["nome_colecao"] = nome_colecao
            dados_cliente["descricao_colecao"] = descricao_colecao

        # Criação do agente e task de copywriting com base nos inputs
        copywriter_agent, copywriter_task = copywriter_data_comemorativa()

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

        # # Solicitação de feedback após exibir o resultado
        # st.subheader("Avalie a Copy")
        # nota = st.slider("Qual nota você dá para esta copy?", 0, 10, step=1)

        # if st.button("Enviar Feedback"):
        #     # Enviar o feedback para o LangSmith
        #     client.create_feedback(
        #     run_id,
        #     key="feedback-key",
        #     score=1.0,
        #     comment="comment",
        # )

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
