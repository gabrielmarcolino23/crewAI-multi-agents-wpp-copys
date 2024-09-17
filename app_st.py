import streamlit as st
from crewai import Crew, Process
from agents.copywriter_aniversario_cliente import copywriter_aniversario_cliente
from agents.copywriter_data_comemorativa import copywriter_data_comemorativa
from agents.copywriter_giftback import copywriter_giftback
from agents.copywriter_lancamento_colecao import copywriter_lancamento_colecao
from agents.copywriter_lancamento_produto import copywriter_lancamento_produto

# Configuração da página e título
st.set_page_config(page_title="Zoppy CopyAI", page_icon="🔵", layout="wide")

# Título da página
st.title("Zoppy - Copywriter")

# Organização da interface em duas colunas principais
col1, col2 = st.columns([3, 2], gap="large")

with col1:
    st.subheader("Preencha os detalhes para gerar a copy")
    
    # Input principal: Tipo de campanha
    tipo_copy = st.selectbox(
        "Tipo de Campanha de WhatsApp",
        options=["data_comemorativa", "lancamento_produto", "lancamento_colecao", 
                 "aniversario_cliente", "giftback"]
    )

    # Inputs dinâmicos que aparecem logo após a seleção do tipo de campanha
    data_comemorativa = None
    descricao_produto = None
    nome_produto = None
    nome_colecao = None
    descricao_colecao = None

    if tipo_copy == "data_comemorativa":
        data_comemorativa = st.text_input("Data Comemorativa", placeholder="Ex: Dia das Mães, Natal")
    
    elif tipo_copy == "lancamento_produto":
        nome_produto = st.text_input("Nome do Produto", placeholder="Digite o nome do produto")
        descricao_produto = st.text_area("Descrição do Produto", placeholder="Descreva o produto", height=100)
    
    elif tipo_copy == "lancamento_colecao":
        nome_colecao = st.text_input("Nome da Coleção", placeholder="Digite o nome da coleção")
        descricao_colecao = st.text_area("Descrição da Coleção", placeholder="Descreva a coleção", height=100)
    
    # Inputs comuns a todas as campanhas
    nome_loja = st.text_input("Nome da Loja", placeholder="Digite o nome da loja")
    segmento = st.text_input("Segmento", placeholder="Digite o segmento de mercado (ex: Moda, Tecnologia)")
    publico_alvo = st.text_input("Público-Alvo", placeholder="Descreva o público-alvo (ex: Jovens adultos, Profissionais)")
    tom_de_voz = st.selectbox("Tom de Voz", options=["Formal", "Informal", "Divertido", "Amigável"], index=0)
    objetivo_copy = st.text_input("Objetivo da Copy", placeholder="Qual o seu objetivo final ao enviar esta mensagem?")

with col2:
    st.subheader("Copy Gerada")

    # Inputs adicionais para a descrição do modelo de copy
    nome_modelo = st.text_input("Nome do Modelo", placeholder="Dê um nome para o modelo")
    descricao_modelo = st.text_area("Descrição", placeholder="Dê uma descrição para o modelo", height=100)

    # Botão para Processar os Dados e Gerar a Copy
    if st.button("Gerar Copy"):
        # Coleta dos dados comuns
        dados_cliente = {
            "nome_loja": nome_loja,
            "segmento": segmento,
            "publico_alvo": publico_alvo,
            "tom_voz": tom_de_voz,
            "objetivo_campanha": objetivo_copy,
            "tipo_campanha": tipo_copy
        }

        # Adiciona campos específicos dependendo do tipo de campanha
        if tipo_copy == "data_comemorativa":
            dados_cliente["data_comemorativa"] = data_comemorativa
            copywriter_agent, copywriter_task = copywriter_data_comemorativa()

        elif tipo_copy == "lancamento_produto":
            dados_cliente["nome_produto"] = nome_produto
            dados_cliente["descricao_produto"] = descricao_produto
            copywriter_agent, copywriter_task = copywriter_lancamento_produto()

        elif tipo_copy == "lancamento_colecao":
            dados_cliente["nome_colecao"] = nome_colecao
            dados_cliente["descricao_colecao"] = descricao_colecao
            copywriter_agent, copywriter_task = copywriter_lancamento_colecao()

        elif tipo_copy == "aniversario_cliente":
            copywriter_agent, copywriter_task = copywriter_aniversario_cliente()

        elif tipo_copy == "giftback":
            copywriter_agent, copywriter_task = copywriter_giftback()

        # Criação do agente e task de copywriting com base nos inputs
        crew = Crew(
            agents=[copywriter_agent],
            tasks=[copywriter_task],
            process=Process.sequential,
            verbose=False
        )

        # Gerar a copy com base nos inputs fornecidos
        resultado_final = crew.kickoff(inputs=dados_cliente)

        # Exibir o resultado na interface
        st.text_area("Resultado Final", resultado_final.raw, height=300)

# Rodapé com informações adicionais
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<footer style='text-align: center; color: #4a148c;'>"
    "© 2024 TonyWriter. Todos os direitos reservados."
    "</footer>",
    unsafe_allow_html=True
)
