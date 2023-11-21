from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date

app = FastAPI()

class Aluno(BaseModel):
    nome: str
    data_nascimento: date
    endereco: str

class Disciplina(BaseModel):
    nome: str
    descricao: Optional[str]

class PedidoMaterial(BaseModel):
    descricao: str
    quantidade: int

alunos_db = []
disciplinas_db = [Disciplina(nome="Matemática"), Disciplina(nome="História")]
pedidos_db = []

@app.post("/cadastro_aluno", status_code=201)
async def cadastrar_aluno(aluno: Aluno):
    alunos_db.append(aluno)
    return {"mensagem": "Aluno cadastrado com sucesso"}

@app.get("/listar_disciplinas", response_model=List[Disciplina])
async def listar_disciplinas():
    return disciplinas_db

@app.post("/matricular_disciplina/{nome_disciplina}", status_code=200)
async def matricular_disciplina(nome_disciplina: str):
    if nome_disciplina not in disciplinas_db:
        raise HTTPException(status_code=404, detail="Disciplina não encontrada")
    return {"mensagem": f"Matriculado na disciplina {nome_disciplina}"}

@app.get("/listar_alunos", response_model=List[Aluno])
async def listar_alunos():
    return alunos_db

@app.post("/pedido_material", status_code=201)
async def pedido_material(pedido: PedidoMaterial):
    pedidos_db.append(pedido)
    return {"mensagem": "Pedido de material didático registrado"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
