from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
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
import jwt
import os

app = FastAPI()

load_dotenv()

# Configuração JWT
SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("JWT_SECRET_KEY_ALGORITHM")


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Extrair role e email do payload
        role = payload.get("role")
        email = payload.get("email")

        if role is None or email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Role ou email não encontrados no token",
            )
        # Retornar um dicionário com as informações extraídas
        return {"role": role, "email": email}
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expirado",
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
        )


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
async def generate_copy(req: Inputs, current_user: dict = Depends(get_current_user)):
    print(f"Usuário autenticado: {current_user.get('email')}")
    print(f"Usuário autenticado: {current_user.get('role')}")
    start_time = time.time()

    run_id = uuid4()
    print(f"Run ID: {run_id}")

    match req.tipo_copy:
        case "giftback":
            copywriter_agent, copywriter_task = copywriter_giftback()
        case "data_comemorativa":
            copywriter_agent, copywriter_task = copywriter_data_comemorativa()
        case "aniversario_cliente":
            copywriter_agent, copywriter_task = copywriter_aniversario_cliente()
        case "lancamento_colecao":
            copywriter_agent, copywriter_task = copywriter_lancamento_colecao()
        case "lancamento_produto":
            copywriter_agent, copywriter_task = copywriter_lancamento_produto()

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
