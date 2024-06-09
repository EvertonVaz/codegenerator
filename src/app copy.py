# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    app.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: codespace <codespace@student.42.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/29 17:34:03 by codespace         #+#    #+#              #
#    Updated: 2024/06/09 17:28:49 by codespace        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
from crewai import Crew, Process
from agents import CodeGenerator
from tasks import TaskGenerator
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()


model = ChatGroq(api_key=os.getenv("API_KEY"), model="llama3-8b-8192")
function_name = "ft_split"

agents = CodeGenerator(model)
print(agents)
code_writer = agents.code_writer()
norme_checker = agents.norme_checker()
code_reviewer = agents.code_reviewer()
tailormade = agents.tailormade()
doc_emmet = agents.doc_emmet()

tasks = TaskGenerator(model, function_name)

code_task = tasks.code_task()
norme_task = tasks.norme_task()
review_task = tasks.review_task()
tailormade_task = tasks.tailormade_task()
doc_task = tasks.doc_task()

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
print(result)