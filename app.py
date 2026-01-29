import streamlit as st
import google.generativeai as genai

# Estética Villa Vigilans
st.set_page_config(page_title="SCURRA PROTOCOL", page_icon="🎭")
st.markdown("<style>.stApp { background-color: #050505; } h1 { color: #CCFF00 !important; }</style>", unsafe_allow_html=True)

st.title("🎭 SCURRA PROTOCOL")

# --- GESTÃO DA CHAVE ---
if "GEMINI_API_KEY" in st.secrets:
    API_KEY = st.secrets["GEMINI_API_KEY"]
else:
    API_KEY = "AIzaSyBbYIbe0B9uZT2jk3WJZVSv5z2dOIWWz-g"

try:
    genai.configure(api_key=API_KEY)
    # Mudança para o modelo PRO - A versão mais estável da API v1beta
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    st.error(f"Erro de Configuração: {e}")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Relata a tua desgraça..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    try:
        # Prompt de sistema embutido na conversa
        contexto = "Age como o Scurra, o bobo cínico da Villa Vigilans. Responde com sarcasmo e negritos. Utilizador: "
        
        response = model.generate_content(contexto + prompt)
        
        if response:
            with st.chat_message("assistant"):
                st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"A Matriz recusa o modelo Pro: {e}")
        st.info("Dominus, se este falhar, o problema reside na ativação da API no Google AI Studio.")
