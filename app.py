import os
import pypdf
import streamlit as st
import google.generativeai as genai

# Obtém a chave de Secrets (Streamlit Cloud) ou variável de ambiente/fallback local
API_KEY = st.secrets.get("GOOGLE_API_KEY", os.getenv("GOOGLE_API_KEY", "AQ.Ab8RN6ITF3o5FNyHcSsw3J0655Gr6kXyCLfGEcdqZ1m2Rv9oYg"))
genai.configure(api_key=API_KEY)

st.set_page_config(page_title="BimBam Buy - Assistente IA", page_icon="🛍️", layout="centered")

st.title("🛍️ BimBam Buy — Assistente de Suporte")
st.caption("Agente Inteligente baseado nas políticas oficiais da loja virtual BimBam Buy.")

PDF_PATH = "data/BimBam_Buy_Documentacao_Completa.pdf"

@st.cache_resource(show_spinner="Carregando base de conhecimento da BimBam Buy...")
def extract_pdf_text(pdf_path: str):
    if not os.path.exists(pdf_path):
        return None
    reader = pypdf.PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"
    return full_text

context_text = extract_pdf_text(PDF_PATH)

if context_text is None:
    st.error(f"Arquivo não encontrado em: {PDF_PATH}. Certifique-se de que o PDF está dentro da pasta 'data/'.")
else:
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Olá! Sou o assistente virtual da BimBam Buy. Como posso ajudar você com dúvidas sobre reembolsos, prazos de entrega, métodos de pagamento ou garantias?"}
        ]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if user_input := st.chat_input("Digite sua dúvida aqui..."):
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Consultando documentação oficial..."):
                try:
                    model = genai.GenerativeModel("models/gemini-3.6-flash")
                    prompt = f"""Você é o assistente virtual oficial de suporte ao cliente da BimBam Buy.
Responda às dúvidas dos clientes exclusivamente com base na documentação oficial fornecida abaixo.
Se a informação não constar no texto, responda de forma cordial e direta que a loja não possui essa informação cadastrada.

--- DOCUMENTAÇÃO OFICIAL DA BIMBAM BUY ---
{context_text}
------------------------------------------

Pergunta do cliente: {user_input}
Resposta clara e objetiva:"""

                    response = model.generate_content(prompt)
                    answer = response.text
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                except Exception as err:
                    st.error(f"Erro ao gerar resposta: {err}")