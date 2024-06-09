# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    toolkit.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: codespace <codespace@student.42.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/09 13:27:08 by codespace         #+#    #+#              #
#    Updated: 2024/06/09 15:49:21 by codespace        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os, subprocess
from crewai_tools import tool

@tool("function_info")
def function_info_tool():
    """
    Fornece informações sobre como escrever a função em C.

    Args:
        function_name: O nome da função.

    Returns:
        Uma string com informações sobre a função.
    """

    return f"""
		Para escrever a função em C, você deve:
		1. Definir o tipo de retorno da função.
		2. Definir os parâmetros de entrada da função.
		3. Implementar o corpo da função para realizar a tarefa desejada.
		4. Retornar o valor apropriado para o tipo de retorno definido.

		Exemplo:

		```c
		int function_name(int param1, int param2) {{
			// Implementação da função
			return resultado;
		}}
		```

		Lembre-se de seguir as normas Norminette para escrever o código.
    """


@tool("code_quality")
def code_quality_tool(function_name):
	"""
	Analisa a qualidade do código e fornece feedback.

	Args:
		function_name: O código C a ser analisado.

	Returns:
		Uma string com feedback sobre a qualidade do código.
	"""

	feedback = f"""
	O código parece bem escrito e fácil de entender.
	As variáveis têm nomes descritivos e o código é organizado.
	No entanto, é possível melhorar o código adicionando mais comentários para explicar o funcionamento das funções.
	"""

	return feedback

@tool("norminette_check")
def norminette_check_tool(function_name):
	"""
	Verifica se o código está em conformidade com as normas Norminette.

	Args:
		function_name: O código C a ser verificado.

	Returns:
		Uma string com feedback sobre a conformidade com as normas Norminette.
	"""

	# Cria um arquivo temporário com o código
	with open("temp.c", "w") as f:
		f.write(function_name)

	# Executa a norminette no arquivo temporário
	try:
		result = subprocess.run(["norminette", "temp.c"], capture_output=True, text=True)
		output = result.stdout.strip()
		if output:
			return f"O código não está em conformidade com as normas Norminette: {output}"
		else:
			return "O código está em conformidade com as normas Norminette."
	except FileNotFoundError:
		return "O comando 'norminette' não foi encontrado. Certifique-se de que a biblioteca Norminette está instalada."
	finally:
		# Exclui o arquivo temporário
		os.remove("temp.c")

@tool("style_analysis")
def style_analysis_tool(function_name, github_url):
	"""
	Analisa o estilo do código em relação ao estilo do usuário.

	Args:
		function_name: O código C a ser analisado.
		github_url: URL do perfil do GitHub do usuário.

	Returns:
		Uma string com feedback sobre o estilo do código.
	"""

	# Simula a análise do estilo do código em relação ao estilo do usuário.
	# Aqui você pode implementar a lógica para analisar o estilo do código.
	# Por exemplo, você pode usar uma biblioteca de análise de código ou um rastreador de código.

	# Substitua esta lógica com a sua própria implementação.
	if github_url:
		return "O código está de acordo com o estilo de código do seu perfil no GitHub. "
	else:
		return "O código está escrito com um estilo de código padrão."

@tool("documentation_generator")
def documentation_generator_tool():
	"""
	Gera documentação para o código C em Markdown.

	Args:
		function_name: O código C a ser documentado.

	Returns:
		Uma string com a documentação do código em Markdown.
	"""

	# Substitua esta lógica com a sua própria implementação.
	documentation = f"""
	## Função function_name

	Esta função function_name realiza uma tarefa específica.

	**Parâmetros:**

	* **Nenhum parâmetro**

	**Retorno:**

	* Nenhum retorno

	**Exemplos:**
	function_name
	"""
	with open("documentation.md", "w") as f:
		f.write(documentation)
	return documentation
