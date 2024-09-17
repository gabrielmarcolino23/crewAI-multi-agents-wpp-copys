from crewai_tools import PDFSearchTool

class RagExamplesWpp(PDFSearchTool):
    def run(self, input):
        # Converter a entrada de string para dicionário
        query_dict = eval(input)
        original_query = query_dict.get('query', '')
        tom_voz = query_dict.get('tom_voz', '')
        if tom_voz:
            # Modificar a consulta para incluir o tom de voz
            modified_query = f"{original_query} tom {tom_voz}"
        else:
            modified_query = original_query
        # Atualizar a entrada
        modified_input = {'query': modified_query}
        # Chamar o método original com a entrada modificada
        return super().run(str(modified_input))
