import streamlit as st
import google.generativeai as genai
import pypdf

# Configurando a Cara do site
st.set_page_config(page_title="Aziz Concept - Atendimento", page_icon="✨")
st.title("🤖 Assistente Virtual - Aziz Concept")
st.write("Bem-vinda! Como posso te ajudar com suas peças hoje?")

# A chave do motor (Já preenchida para você!)
genai.configure(api_key="COLOQUE_SUA_CHAVE_AQUI")

# Lendo o PDF da Loja
@st.cache_data
def extrair_texto_pdf(caminho):
    texto = ""
    try:
        leitor = pypdf.PdfReader(caminho)
        for pagina in leitor.pages:
            texto += pagina.extract_text()
    except Exception as e:
        texto = "Erro ao carregar políticas da loja."
    return texto

# Lendo exatamente o arquivo que você subiu
documento_loja = extrair_texto_pdf("regras_loja.pdf")

# As regras absolutas
instrucoes = f"""
Você é a assistente virtual de atendimento da loja online de roupas femininas Aziz Concept.
Responda às dúvidas das clientes de forma educada e simpática, baseando-se ESTRITAMENTE nestas políticas da loja:

{documento_loja}

Se a pergunta for sobre um assunto que não consta nas regras acima, peça desculpas e oriente a cliente a entrar em contato com o suporte humano no WhatsApp.
"""

# O modelo de IA
modelo = genai.GenerativeModel(
    model_name="gemini-3.7-flash",
    system_instruction=instrucoes
)

# Memória do chat e Exibição
if "chat" not in st.session_state:
    st.session_state.chat = modelo.start_chat()

for mensagem in st.session_state.chat.history:
    if mensagem.role == "user":
        with st.chat_message("user"):
            st.markdown(mensagem.parts[0].text)
    else:
        with st.chat_message("assistant"):
            st.markdown(mensagem.parts[0].text)

# Caixa de pergunta
pergunta = st.chat_input("Digite sua dúvida aqui...")

if pergunta:
    with st.chat_message("user"):
        st.markdown(pergunta)
    with st.chat_message("assistant"):
        resposta = st.session_state.chat.send_message(pergunta)
        st.markdown(resposta.text)
