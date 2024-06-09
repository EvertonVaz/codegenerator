# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    app.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: etovaz <etovaz@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/29 17:34:03 by codespace         #+#    #+#              #
#    Updated: 2024/06/09 16:19:08 by etovaz           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import streamlit as st
from crewai import Crew, Process
from agents import CodeGenerator
from tasks import TaskGenerator
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(api_key=os.getenv("API_KEY"), model="llama3-8b-8192")

# Inicializa os agentes
agents = CodeGenerator(model)
code_writer = agents.code_writer()
norme_checker = agents.norme_checker()
code_reviewer = agents.code_reviewer()
tailormade = agents.tailormade()
doc_emmet = agents.doc_emmet()

# Cria a interface do Streamlit
st.title("Gerador de Funções C")

# Campo de entrada para o nome da função
function_name = st.text_input("Nome da função:", "ft_split")

# Botão para iniciar o processo
if st.button("Gerar"):
    # Cria as tarefas
    tasks = TaskGenerator(model, function_name)
    code_task = tasks.code_task()
    norme_task = tasks.norme_task()
    review_task = tasks.review_task()
    tailormade_task = tasks.tailormade_task()
    doc_task = tasks.doc_task()

    # Cria a Crew
    crew = Crew(
        agents=[
            code_writer,
            code_reviewer,
            norme_checker,
            tailormade,
            doc_emmet
        ],
        tasks=[
            code_task,
            review_task,
            norme_task,
            tailormade_task,
            doc_task
        ],
        process=Process.sequential,
        language="pt-br",
        memory=True,
        cache=True,
        verbose=True,
        max_rpm=100,
        manager_llm=model
    )

    # Executa as tarefas
    result = crew.kickoff()

    # Imprime o resultado
    st.write(f"### Resultado: {result}")

    def get_output(name):
        with open(f"./src/io/{name}", "r") as f:
            return f.read()

    code = get_output("code")
    norm = get_output("norm")
    review = get_output("review")
    tailormade = get_output("tailormade")
    doc = get_output("doc")

    # Criação das abas
    tabs = st.tabs(["Code Writer", "Norme Checker", "Code Reviewer", "Tailormade", "Doc Emmet"])

    # Seleção e exibição do conteúdo das abas
    with tabs[0]:
        st.write(f"**Code Writer:**\n{code}")
    with tabs[1]:
        st.write(f"**Norme Checker:**\n{norm}")
    with tabs[2]:
        st.write(f"**Code Reviewer:**\n{review}")
    with tabs[3]:
        st.write(f"**Tailormade:**\n{tailormade}")
    with tabs[4]:
        st.write(f"**Doc Emmet:**\n{doc}")

