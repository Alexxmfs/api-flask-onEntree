from flask import Flask, jsonify, request, Response
from flask_cors import CORS
import config
from exemplo_sql import (
    listarLocais, criarLocal, obterLocal, atualizarLocal, deletarLocal, listarEventos, obterEvento, criarEvento, atualizarEvento, deletarEvento
)

app = Flask(__name__)
CORS(app)

# Rotas para Locais
@app.get('/locais')
def listar_locais():
    locais = listarLocais()
    lista = [
        {
            'id_local': local['id_local'],
            'nome': local['nome'],
            'apelido': local['apelido'],
            'tipo': local['tipo'],
            'cnpj': local['cnpj'],
            'cidade': local['cidade'],
            'estado': local['estado'],
            'cep': local['cep'],
            'complemento': local['complemento'],
            'endereco': local['endereco'],
            'email': local['email'],
            'telefone': local['telefone'],
            'nome_entrada': local['nome_entrada'],
            'nome_catraca': local['nome_catraca']
        } for local in locais
    ]
    return jsonify(lista)

@app.get('/locais/<int:id_local>')
def obter_local(id_local):
    local = obterLocal(id_local)
    if local:
        return jsonify(local)
    else:
        return Response(status=404)

@app.post('/criar-locais')
def criar_local():
    dados = request.json
    criarLocal(**dados)
    return Response(status=201)

@app.put('/atualizar-locais/<int:id_local>')
def atualizar_local(id_local):
    dados = request.json
    atualizado = atualizarLocal(id_local, **dados)
    return Response(status=200 if atualizado else 404)

@app.delete('/deletar-locais/<int:id_local>')
def deletar_local(id_local):
    deletado = deletarLocal(id_local)
    return Response(status=200 if deletado else 404)


# Rotas para Eventos
@app.get('/eventos')
def listar_eventos():
    eventos = listarEventos()
    lista = [
        {
            'id_evento': evento['id_evento'],
            'nome': evento['nome'],
            'data_evento': evento['data_evento'],
            'horario_evento': str(evento['horario_evento']),  # Converte timedelta para string
            'tipo': evento['tipo'],
            'email': evento['email'],
            'telefone': evento['telefone'],
            'id_local': evento['id_local']
        } for evento in eventos
    ]
    return jsonify(lista)

@app.get('/eventos/<int:id_evento>')
def obter_evento(id_evento):
    evento = obterEvento(id_evento)
    if evento:
        return jsonify(evento), 200  # Retorna o evento com status 200 (OK)
    else:
        return Response(status=404)  # Retorna status 404 se não encontrar o evento

@app.post('/criar-eventos')
def criar_evento():
    dados = request.json
    criarEvento(**dados)
    return Response(status=201)

@app.put('/atualizar-eventos/<int:id_evento>')
def atualizar_evento(id_evento):
    dados = request.json
    atualizado = atualizarEvento(id_evento, **dados)
    return Response(status=200 if atualizado else 404)

@app.delete('/deletar-eventos/<int:id_evento>')
def deletar_evento(id_evento):
    deletado = deletarEvento(id_evento)
    return Response(status=200 if deletado else 404)

if __name__ == '__main__':
    app.run(host=config.host, port=config.port, debug=True)