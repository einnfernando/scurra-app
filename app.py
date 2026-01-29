import streamlit as st
import google.generativeai as genai

# Estética Villa Vigilans
st.set_page_config(page_title="SCURRA PROTOCOL", page_icon="🎭")
st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    h1, h2, h3 { color: #CCFF00 !important; font-family: 'Courier New', monospace; text-shadow: 2px 2px #0055FF; }
    p { color: #00FFFF !important; font-family: 'Courier New', monospace; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎭 SCURRA PROTOCOL")

# Configuração da API
API_KEY = "gen-lang-client-0277274736" 
genai.configure(api_key=API_KEY)
instruction = "És o Scurra, o bobo cínico da Villa Vigilans. Responde com ironia, humor ácido e negritos."
model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=instruction)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Relata a tua desgraça..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        response = model.generate_content(prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
