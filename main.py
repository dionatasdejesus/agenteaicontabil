import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Agente Josi Cajá", page_icon="☤", layout="centered")

OPENAI_KEY = st.secrets["openai_key"]
client = OpenAI(api_key=OPENAI_KEY)

def chatbot(query):
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é um especialista em Ciências Contábeis..."},
            {"role": "user", "content": query}
        ]
    )
    return completion.choices[0].message.content

def main():
    st.title("☤ Agente Josi Cajá Contabilidade ☤")
    st.markdown("Bem-vindo! Digite sua dúvida contábil abaixo 👇")

    if "mensagens" not in st.session_state:
        st.session_state.mensagens = []

    for msg in st.session_state.mensagens:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Digite sua mensagem")
    if user_input:
        st.session_state.mensagens.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        resposta = chatbot(user_input)
        st.session_state.mensagens.append({"role": "assistant", "content": resposta})
        with st.chat_message("assistant"):
            st.markdown(resposta)

if __name__ == "__main__":
    main()

 

