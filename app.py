import streamlit as st
import google.generativeai as genai

# Estética Villa Vigilans
st.set_page_config(page_title="SCURRA PROTOCOL", page_icon="🎭")
st.markdown("<style>.stApp { background-color: #050505; } h1 { color: #CCFF00 !important; font-family: 'Courier New', monospace; }</style>", unsafe_allow_html=True)

st.title("🎭 SCURRA PROTOCOL")

# --- GESTÃO DA CHAVE ---
if "GEMINI_API_KEY" in st.secrets:
    API_KEY = st.secrets["GEMINI_API_KEY"]
else:
    API_KEY = "AIzaSyBbYIbe0B9uZT2jk3WJZVSv5z2dOIWWz-g"

try:
    genai.configure(api_key=API_KEY)
    # Mudança crucial: usando o sufixo 'latest' para evitar o erro 404
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
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
        # Injeção de personalidade robusta
        contexto = "És o Scurra, o bobo cínico da Villa Vigilans. Responde com sarcasmo pesado e negritos. O utilizador diz: "
        
        # Chamada direta e simples
        response = model.generate_content(contexto + prompt)
        
        if response.text:
            with st.chat_message("assistant"):
                st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Erro na Matriz (404/Refined): {e}")
        st.info("Dominus, se este erro persistir, o Google está a exigir o uso do modelo 'gemini-pro'. Deseja que eu tente a troca?")
