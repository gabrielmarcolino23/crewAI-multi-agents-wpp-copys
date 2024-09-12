from fastapi import FastAPI
from pydantic import BaseModel
from crewai import Crew, Process
from agents.copywriter_whatsApp import copywriter_whatsApp_agent()
from uuid import uuid4  
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()

# Definir o modelo de entrada
class Inputs(BaseModel):
    nome_loja: str
    segmento: str
    publico_alvo: str
    tom_de_voz: str
    objetivo_copy: str
    tipo_copy: str
    data_comemorativa: str | None
    descricao_colecao: str | None
    descricao_produto: str | None
    nome_colecao: str | None
    nome_produto: str | None

# Definir a rota para executar a tarefa
@app.post("/generate/copy")
async def generate_copy(req: Inputs):

    run_id = uuid4()
    print(f"Run ID: {run_id}")

    copywriter_agent, copywriter_task = copywriter_whatsApp_agent()

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
            "tom_voz": req.tom_de_voz,
            "objetivo_campanha": req.objetivo_copy,
            "tipo_campanha": req.tipo_copy,
            "data_comemorativa": req.data_comemorativa,
            "descricao_colecao": req.descricao_colecao,
            "descricao_produto": req.descricao_produto,
            "nome_colecao": req.nome_colecao,
            "nome_produto": req.nome_produto,
        }
    )

    return {
        "run_id": str(run_id),  
        "copy": resultado_final.raw
    }

# Rodar o servidor usando Uvicorn
if __name__ == "__main__":
    import uvicorn

    print(">>>>>>>>>>>> version V0.0.1")
    uvicorn.run(app, host="0.0.0.0", port=8000)
