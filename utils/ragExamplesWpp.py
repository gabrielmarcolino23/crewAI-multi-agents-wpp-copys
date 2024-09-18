from crewai_tools import PDFSearchTool

class RagExamplesWpp(PDFSearchTool):
    def run(self, input):
        query_dict = eval(input)
        original_query = query_dict.get('query', '')
        tom_voz = query_dict.get('tom_voz', '')
        if tom_voz:
            
            modified_query = f"{original_query} tom {tom_voz}"
        else:
            modified_query = original_query
       
        modified_input = {'query': modified_query}
      
        return super().run(str(modified_input))
