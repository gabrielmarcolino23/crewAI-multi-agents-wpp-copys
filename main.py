from fastapi import FastAPI
from pydantic import BaseModel
from crewai import Crew, Process
from agents.copywriter_aniversario_cliente import copywriter_aniversario_cliente
from agents.copywriter_data_comemorativa import copywriter_data_comemorativa
from agents.copywriter_giftback import copywriter_giftback
from agents.copywriter_lancamento_colecao import copywriter_lancamento_colecao
from agents.copywriter_lancamento_produto import copywriter_lancamento_produto
from uuid import uuid4
from dotenv import load_dotenv
from enum import Enum
import time

app = FastAPI()

load_dotenv()


class TipoCopy(str, Enum):
    giftback = "giftback"
    data_comemorativa = "data_comemorativa"
    lancamento_produto = "lancamento_produto"
    lancamento_colecao = "lancamento_colecao"
    aniversario_cliente = "aniversario_cliente"


class Inputs(BaseModel):
    nome_loja: str
    segmento: str
    publico_alvo: str
    tom_de_voz: str
    objetivo_copy: str
    tipo_copy: TipoCopy
    data_comemorativa: str | None = None
    descricao_colecao: str | None = None
    descricao_produto: str | None = None
    nome_colecao: str | None = None
    nome_produto: str | None = None


@app.post("/generate/copy")
async def research_candidates(req: Inputs):
    start_time = time.time()

    run_id = uuid4()
    print(f"Run ID: {run_id}")

    match req.tipo_copy:
        case "giftback":
            copywriter_agent, copywriter_task = copywriter_giftback()
        case "data_comemorativa":
            copywriter_agent, copywriter_task = copywriter_data_comemorativa()
        case "lancamento_produto":
            copywriter_agent, copywriter_task = copywriter_lancamento_produto()
        case "lancamento_colecao":
            copywriter_agent, copywriter_task = copywriter_lancamento_colecao()
        case "aniversario_cliente":
            copywriter_agent, copywriter_task = copywriter_aniversario_cliente()

    crew = Crew(
        agents=[copywriter_agent],
        tasks=[copywriter_task],
        process=Process.sequential,
        verbose=False,
    )

    resultado_final = await crew.kickoff_async(
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

    end_time = time.time()
    execution_time = end_time - start_time

    return {
        "run_id": str(run_id),
        "copy": resultado_final.raw,
        "tempo_execucao": f"{execution_time}s",
    }


if __name__ == "__main__":
    import uvicorn

    print(">>>>>>>>>>>> version V0.0.1")
    uvicorn.run(app, host="0.0.0.0", port=8000)
