from crewai_tools import PDFSearchTool

class ZoppyVariablesSearchTool(PDFSearchTool):
    name: str = "variaveis_tool"
    description: str = (
        "Use esta ferramenta para buscar informações sobre as variáveis da Zoppy disponíveis, "
        "suas descrições e orientações sobre quando utilizá-las."
    )

    def __init__(self, pdf):
        super().__init__(pdf=pdf)

    def run(self, input):
        # Converter a entrada de string para dicionário de forma segura
        try:
            query_dict = eval(input)
        except Exception as e:
            return f"Erro ao processar a entrada: {e}"
        query = query_dict.get('query', '')

        if not query:
            return "Por favor, forneça uma consulta válida para buscar nas variáveis da Zoppy."

        # Chamar o método original com a entrada modificada
        return super().run(str({'query': query}))
