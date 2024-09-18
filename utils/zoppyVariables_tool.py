from crewai_tools import PDFSearchTool

class ZoppyVariablesSearchTool(PDFSearchTool):
    name: str = "variaveis_tool"
    description: str = (
    "Use esta ferramenta para buscar informações detalhadas sobre as variáveis disponíveis na Zoppy, "
    "incluindo suas descrições e orientações sobre quando utilizá-las. "
    "Quando precisar de informações sobre uma variável específica, forneça o nome exato da variável na consulta. "
    "Evite consultas genéricas como 'placeholders' e seja o mais específico possível."
)
    def __init__(self, pdf):
        super().__init__(pdf=pdf)

    def run(self, input):
        try:
            query_dict = eval(input)
        except Exception as e:
            return f"Erro ao processar a entrada: {e}"
        query = query_dict.get('query', '')

        if not query:
            return "Por favor, forneça uma consulta válida para buscar nas variáveis da Zoppy."

        return super().run(str({'query': query}))
