# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tasks.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: etovaz <etovaz@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/09 13:22:40 by codespace         #+#    #+#              #
#    Updated: 2024/06/09 19:04:56 by etovaz           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from crewai import Task
from src.agents import CodeGenerator
from src.toolkit import function_info_tool, norminette_check_tool, code_quality_tool, style_analysis_tool, documentation_generator_tool

class TaskGenerator(CodeGenerator):
	def __init__(self, model, function_name):
		self.function_name = function_name
		super().__init__(model)

	def code_task(self):
		return (
			Task(
				description=f"""Responda em portugues brasileiro
				Gerar a função C {self.function_name}. A função deve ser escrita de forma clara, eficiente e organizada. Certifique-se de seguir as melhores práticas de programação em C, incluindo a otimização de desempenho e a gestão de memória. O código deve ser fácil de entender, manter e estender.
       			""",

				expected_output='Código C para a função, otimizado para performance e legibilidade. O código deve seguir as melhores práticas de programação em C, incluindo a otimização de desempenho e a gestão de memória. O código deve ser fácil de entender, manter e estender.',
				agent=self.code_writer(),
				allow_delegation=True,
				output_file='src/io/code',
			)
		)

	def norme_task(self):
		return (
			Task(
				description=f"""Responda em portugues brasileiro
				Verificar se a função {self.function_name} está em conformidade com as normas Norminette. As normas Norminette definem padrões para estilo de código, formatação e organização. Certifique-se de que o código atenda a todos os requisitos das normas Norminette para garantir que ele seja consistente e profissional.""",

				expected_output='Código C que atenda às normas Norminette. Se houver alguma violação das normas Norminette, forneça sugestões claras e concisas para corrigir os erros.',
				agent=self.norme_checker(),
				context=[self.code_task()],
				output_file='src/io/norm'
			)
		)

	def review_task(self):
		return (
			Task(
				description=f"""Responda em portugues brasileiro
				Gerar perguntas específicas e detalhadas sobre a função {self.function_name} para avaliar sua correção, eficiência e segurança. As perguntas devem ajudar a identificar possíveis falhas, erros lógicos e problemas de performance. Você deve se concentrar em questões de segurança, performance, legibilidade e manutenção.""",

				expected_output='Perguntas para revisão do código. As perguntas devem ser relevantes, claras e concisas. Elas devem ajudar a identificar possíveis falhas, erros lógicos e problemas de performance.',
				agent=self.code_reviewer(),
				context=[self.code_task(), self.norme_task()],
				output_file='src/io/review'
			)
		)

	def tailormade_task(self):
		return (
			Task(
				description=f"""Responda em portugues brasileiro
				Ajustar o estilo da função {self.function_name} para corresponder às preferências do usuário, analisando o estilo de código usado em seus repositórios no GitHub. O objetivo é garantir que o código se integre perfeitamente ao estilo de código do usuário, seguindo as mesmas convenções de formatação, nomenclatura e estrutura.""",

				expected_output='Código C com o estilo ajustado para corresponder às preferências do usuário. O código deve seguir as mesmas convenções de formatação, nomenclatura e estrutura do código do usuário.',
				agent=self.tailormade(),
				context=[self.code_task(), self.norme_task(), self.review_task()],
				output_file='src/io/tailormade',
			)
		)

	def doc_task(self):
		return (
			Task(
				description=f"""Responda em portugues brasileiro
				Gerar documentação completa e clara para a função {self.function_name} que o Code Writer escreveu, em Markdown, incluindo uma descrição detalhada da função, seus parâmetros de entrada, o valor de retorno esperado, exemplos de uso e possíveis cenários de erro. A documentação deve ser concisa, informativa e fácil de entender.""",

				expected_output='Documentação em Markdown para a função C, incluindo uma descrição detalhada da função, seus parâmetros de entrada, o valor de retorno esperado, exemplos de uso e possíveis cenários de erro. A documentação deve ser concisa, informativa e fácil de entender.',
				agent=self.doc_emmet(),
				context=[self.code_task(), self.review_task(), self.tailormade_task()],
				output_file='src/io/doc',
			)
		)