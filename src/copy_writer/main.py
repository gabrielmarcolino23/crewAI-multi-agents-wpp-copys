from copy_writer.crew import CopyWriterCrew

def run():
    inputs = {
    "nome_loja": "Vorr",
    "segmento": "moda feminina",
    "publico_alvo": "jovens adultas",
    "tom_de_voz": "descontraído e amigável",
    "objetivo_campanha": "liquidação de verão",
    "tipo_campanha": "Liquidação",
    }
    CopyWriterCrew().crew().kickoff(inputs=inputs)

if __name__ == '__main__':
    run()