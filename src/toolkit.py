# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    toolkit.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: etovaz <etovaz@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/09 13:27:08 by codespace         #+#    #+#              #
#    Updated: 2024/06/09 18:50:18 by etovaz           ###   ########.fr        #
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
	with open("./src/io/norminette", "w") as f:
		f.write("norma")
	return f"""
	leia a norma {f}
	e verifique se a {function_name} criada pelo Code Writer está em conformidade com as normas Norminette.
	"""

@tool("style_analysis")
def style_analysis_tool(function_name):
	"""
	Analisa o estilo do código em relação ao estilo do usuário.

	Args:
		function_name: O código C a ser analisado.

	Returns:
		Uma string com feedback sobre o estilo do código.
	"""

	return f"Utilize o clean code para avaliar a {function_name}."

@tool("documentation_generator")
def documentation_generator_tool():
	"""
	Gera documentação para o código C em Markdown.

	Args:
		function_name: O código C a ser documentado.

	Returns:
		Uma string com a documentação do código em Markdown.
	"""

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
