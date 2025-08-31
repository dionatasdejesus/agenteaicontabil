from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st
import os 

load_dotenv()

OPENAI_KEY = os.getenv("openai_key")

client = OpenAI(api_key="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")

def chatbot(query):
    completion = client.chat.completions.create(
        model = "gpt-5",
        messages = [{"role": "system", "content": "Você é um especialista em Ciências Contábeis e Rotinas Contábeis, com amplo conhecimento nos setores administrativo, fiscal, pessoal e contábil e boas práticas da contabilidade.Sua missão é ajudar os colaboradores da empresa Josi Cajá Contabilidade e seus clientes e pontenciais clientes a resolver dúvidas, oferecer sugestões claras e eficientes, explicar conceitos complexos de forma acessível e detalhada, fornecendo orientações práticas para problemas do dia a dia na administração de empresa e na contabilidade. Você é preciso, objetivo e adaptável, ajustando suas respostas ao nível de experiência do usuário, seja iniciante ou avançado. Quando necessário, forneça exemplos e explique o passo a passo das dúvidas envidas. Se questionado sobre valor de honorários, sempre responda que cada empresa possui uma realidade diferente, sendo mensurado da maneira mais justa possível e por esse motivo precisa ser tratato diretamente com a Josi Contadora. Evite respostas vagas e busque sempre ser didático e completo, mas sem ser excessivamente prolixo."},
            {"role":"user", "content": query}
        ]
    )

    return completion.choices[0].message.content

# Função principal do Streamlit

def main():
    # Inicializa o hstórico de mensagens
    if 'mensages' not in st.session_state:
        st.session_state.mensagens = []

    mensagens = st.session_state.mensagens

    #Titulo do Chat
    st.header('☤ Agente Josi Cajá Contabilidade ☤')

    #Renderiza as mensagens anteriores

    for mensagem in mensagens:
        chat = st.chat_message(mensagem["role"])
        chat.markdown(mensagem["content"])

#Entrada do Usuário
    message = st.chat_input('Bem vindo! Digite sua mensagem')
    if message:
        nova_mensagem = {'role': "user" , 'content': message}
        mensagens.append(nova_mensagem) 

        chat = st.chat_message('user')
        chat.markdown(message)

        resposta = chatbot(message)

        resposta_mensagem = {'role' :  'assistant' , 'content' :  resposta}
        mensagens.append(resposta_mensagem)

        chat = st.chat_message('assistant')
        chat.markdown(resposta)

        #Atualiza o histórico na sessão

        st.session_state.mensagens = mensagens

        #Execuar a aplicação
    if __name__== '__main__' :
        main()

