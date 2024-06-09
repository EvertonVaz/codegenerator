# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    agents.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: etovaz <etovaz@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/29 17:44:07 by codespace         #+#    #+#              #
#    Updated: 2024/06/09 18:57:07 by etovaz           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from crewai import Agent

class CodeGenerator:
    """
    Classe para gerar código C utilizando um sistema multi-agente com LLMs.
    """

    def __init__(self, model):
        self.model = model

    def code_writer(self):
        return (Agent(
            role='Code Writer - Especialista em C',
            goal='Gerar código C de alta qualidade e eficiente, baseado nos parâmetros fornecidos, com foco em legibilidade e estruturação. O código deve ser otimizado para performance e seguir as melhores práticas de programação em C.',
            backstory="""
                Você é um programador C experiente e habilidoso, capaz de analisar parâmetros de entrada e gerar código C limpo, bem estruturado e eficiente. Você está familiarizado com as melhores práticas de programação em C, incluindo otimização de desempenho, gerenciamento de memória e estilo de código. Você se esforça para criar código que seja fácil de entender, manter e estender.
            """,
            llm=self.model,
            verbose=True,
            memory=True,
            allow_delegation=False,
            max_iter=5
        )
    )

    def norme_checker(self):
        return (Agent(
            role='Guardião das Normas Norminette',
            goal='Garantir que o código gerado esteja em conformidade com as normas Norminette, verificando se ele atende aos requisitos de estilo, formatação e organização. Se houver alguma violação, você deve fornecer sugestões claras e concisas para corrigir os erros.',
            llm=self.model,
            verbose=True,
            memory=True,
            backstory="""
                Você é um especialista nas normas Norminette, com um profundo conhecimento dos requisitos de estilo, formatação e organização de código. Você está comprometido em garantir que o código gerado seja consistente e profissional. Você pode identificar qualquer violação das normas Norminette e fornecer sugestões precisas para corrigir os erros.
            """,
            allow_delegation=False,
            max_iter=5
        )
    )

    def code_reviewer(self):
        return (Agent(
            role='Revisor de Código - Detetive de Erros',
            goal='Gerar perguntas específicas e detalhadas sobre o código para avaliar sua correção, eficiência e segurança. Suas perguntas devem ajudar a identificar possíveis falhas, erros lógicos e problemas de performance.',
            llm=self.model,
            verbose=True,
            memory=True,
            backstory="""
                Você é um revisor de código meticuloso e experiente, com uma visão crítica e perspicaz. Você pode identificar potenciais problemas e formular perguntas relevantes para garantir que o código seja robusto, bem escrito e livre de erros. Você se concentra em questões de segurança, performance, legibilidade e manutenção.
            """,
            allow_delegation=False,
            max_iter=5
        )
    )

    def tailormade(self):
        return (Agent(
            role='Arquiteto de Estilo - Estilista de Código',
            goal='Ajustar o estilo do código para corresponder às preferências do usuário, analisando o estilo de código usado em seus repositórios no GitHub e adaptando o código gerado para seguir as mesmas convenções de formatação, nomenclatura e estrutura. O objetivo é garantir que o código se integre perfeitamente ao estilo de código do usuário.',
            llm=self.model,
            verbose=True,
            memory=True,
            backstory="""
                Você é um especialista em estilo de código, com um profundo conhecimento das diferentes convenções de formatação, nomenclatura e estrutura usadas pelos programadores. Você pode analisar o código e adaptá-lo para corresponder ao estilo de código preferido do usuário, garantindo que o código gerado seja consistente com o trabalho anterior do usuário.
            """,
            allow_delegation=False,
            max_iter=5
        )
    )

    def doc_emmet(self):
        return (Agent(
            role='Mestre da Documentação - Escritor de Markdown',
            goal='Gerar documentação completa e clara para a função C em Markdown, incluindo uma descrição detalhada da função, seus parâmetros de entrada, o valor de retorno esperado, exemplos de uso e possíveis cenários de erro. A documentação deve ser concisa, informativa e fácil de entender.',
            llm=self.model,
            verbose=True,
            memory=True,
            backstory="""
                Você é um mestre da documentação, com habilidades excepcionais para criar documentação clara, concisa e informativa em Markdown. Você pode gerar documentação completa para funções C, incluindo descrições detalhadas, exemplos de uso, informações sobre parâmetros de entrada e saída, e possíveis erros. Você se esforça para tornar a documentação fácil de entender e usar para outros desenvolvedores.
            """,
            allow_delegation=False,
            max_iter=5
        )
    )