import streamlit as st
import google.generativeai as genai

# Configuração da Villa - Estética Néon
st.set_page_config(page_title="SCURRA PROTOCOL", page_icon="🎭")
st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    h1 { color: #CCFF00 !important; font-family: 'Courier New', monospace; text-shadow: 2px 2px #0055FF; }
    p, span, div { color: #00FFFF !important; font-family: 'Courier New', monospace; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎭 SCURRA PROTOCOL")

# --- GESTÃO DA CHAVE (COFRE) ---
# Tenta ler do Streamlit Secrets primeiro. Se não existir, usa a nova chave direta.
if "GEMINI_API_KEY" in st.secrets:
    API_KEY = st.secrets["GEMINI_API_KEY"]
else:
    API_KEY = "AIzaSyBbYIbe0B9uZT2jk3WJZVSv5z2dOIWWz-g"

genai.configure(api_key=API_KEY)

# Inicialização simplificada para evitar o erro InvalidArgument
model = genai.GenerativeModel('gemini-1.5-flash')

if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibição do histórico
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input do Dominus
if prompt := st.chat_input("Relata a tua desgraça..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    try:
        # Fundimos a personalidade diretamente no prompt para garantir compatibilidade
        scurra_context = (
            "És o Scurra, o bobo cínico da Villa Vigilans. Responde com ironia ácida, "
            "humor negro e usa negritos nas partes mais sarcásticas. "
            f"O utilizador diz: {prompt}"
        )
        
        response = model.generate_content(scurra_context)
        
        if response.text:
            with st.chat_message("assistant"):
                st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            
    except Exception as e:
        st.error(f"Erro na Matriz: {str(e)}")
        st.info("Nota: Se o erro persistir, verifique se a chave no 'Cofre' do Streamlit está correta.")
