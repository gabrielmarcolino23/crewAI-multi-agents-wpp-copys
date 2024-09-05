from fastapi import FastAPI
from pydantic import BaseModel
from crewai import Crew, Process
from agents.copywriter_giftback import copywriter_giftback

app = FastAPI()

from dotenv import load_dotenv

load_dotenv()


# Definir o modelo de entrada
class Inputs(BaseModel):
    nome_loja: str
    segmento: str
    publico_alvo: str
    tom_voz: str
    objetivo_campanha: str
    tipo_campanha: str
    data_comemorativa: str


# Definir a rota para executar a tarefa
@app.post("/generate/copy")
async def research_candidates(req: Inputs):
    copywriter_agent, copywriter_task = copywriter_giftback()

    crew = Crew(
        agents=[copywriter_agent],
        tasks=[copywriter_task],
        process=Process.sequential,
        verbose=True,
    )

    resultado_final = crew.kickoff(
        inputs={
            "nome_loja": req.nome_loja,
            "segmento": req.segmento,
            "publico_alvo": req.publico_alvo,
            "tom_voz": req.tom_voz,
            "objetivo_campanha": req.objetivo_campanha,
            "tipo_campanha": req.tipo_campanha,
            "data_comemorativa": req.data_comemorativa,
        }
    )

    return {"result": resultado_final.raw}


# Rodar o servidor usando Uvicorn
if __name__ == "__main__":
    import uvicorn

    print(">>>>>>>>>>>> version V0.0.1")
    uvicorn.run(app, host="0.0.0.0", port=8000)