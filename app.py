from flask import Flask, jsonify, request, Response
from flask_cors import CORS
import config
from exemplo_sql import (
    listarLocais, criarLocal, obterLocal, atualizarLocal, deletarLocal,
    listarLocalizacoes, criarLocalizacao, obterLocalizacao, atualizarLocalizacao, deletarLocalizacao, listarContatos, criarContato, obterContato, atualizarContato, deletarContato, listarEntradas, obterEntrada, criarEntrada, atualizarEntrada, deletarEntrada, listarCatracas, obterCatraca, criarCatraca, atualizarCatraca, deletarCatraca, listarEventos, obterEvento, criarEvento, atualizarEvento, deletarEvento
)

app = Flask(__name__)
CORS(app)

# Rotas para Locais
@app.get('/locais')
def listar_locais():
    locais = listarLocais()
    lista = [{'id_local': local['id_local'], 'nome': local['nome'], 'tipo': local['tipo'], 'cnpj': local['cnpj']} for local in locais]
    return jsonify(lista)

@app.get('/locais/<int:id_local>')
def obter_local(id_local):
    local = obterLocal(id_local)
    if local:
        return jsonify({
            'id_local': local['id_local'],
            'nome': local['nome'],
            'apelido': local['apelido'],
            'tipo': local['tipo'],
            'cnpj': local['cnpj']
        })
    else:
        return Response(status=404)

@app.post('/criar-locais')
def criar_local():
    dados = request.json
    nome = dados.get('nome')
    apelido = dados.get('apelido')
    tipo = dados.get('tipo')
    cnpj = dados.get('cnpj')
    
    criarLocal(nome, apelido, tipo, cnpj)
    return Response(status=201)

@app.put('/atualizar-locais/<int:id_local>')
def atualizar_local(id_local):
    dados = request.json
    nome = dados.get('nome')
    apelido = dados.get('apelido')
    tipo = dados.get('tipo')
    cnpj = dados.get('cnpj')
    
    atualizado = atualizarLocal(id_local, nome, apelido, tipo, cnpj)
    return Response(status=200 if atualizado else 404)

@app.delete('/deletar-locais/<int:id_local>')
def deletar_local(id_local):
    deletado = deletarLocal(id_local)
    return Response(status=200 if deletado else 404)

# Rotas para Localização
@app.get('/localizacoes')
def listar_localizacoes():
    localizacoes = listarLocalizacoes()
    lista = [{'id_localizacao': loc['id_localizacao'], 'cidade': loc['cidade'], 'estado': loc['estado'], 'cep': loc['cep'], 'endereco': loc['endereco'], 'id_local': loc['id_local']} for loc in localizacoes]
    return jsonify(lista)

@app.get('/localizacoes/<int:id_localizacao>')
def obter_localizacao(id_localizacao):
    localizacao = obterLocalizacao(id_localizacao)
    if localizacao:
        return jsonify({
            'id_localizacao': localizacao['id_localizacao'],
            'cidade': localizacao['cidade'],
            'estado': localizacao['estado'],
            'cep': localizacao['cep'],
            'complemento': localizacao['complemento'],
            'endereco': localizacao['endereco'],
            'id_local': localizacao['id_local']
        })
    else:
        return Response(status=404)

@app.post('/criar-localizacoes')
def criar_localizacao():
    dados = request.json
    cidade = dados.get('cidade')
    estado = dados.get('estado')
    cep = dados.get('cep')
    complemento = dados.get('complemento')
    endereco = dados.get('endereco')
    id_local = dados.get('id_local')

    criarLocalizacao(cidade, estado, cep, complemento, endereco, id_local)
    return Response(status=201)

@app.put('/atualizar-localizacoes/<int:id_localizacao>')
def atualizar_localizacao(id_localizacao):
    dados = request.json
    cidade = dados.get('cidade')
    estado = dados.get('estado')
    cep = dados.get('cep')
    complemento = dados.get('complemento')
    endereco = dados.get('endereco')
    id_local = dados.get('id_local')

    atualizado = atualizarLocalizacao(id_localizacao, cidade, estado, cep, complemento, endereco, id_local)
    return Response(status=200 if atualizado else 404)

@app.delete('/deletar-localizacoes/<int:id_localizacao>')
def deletar_localizacao(id_localizacao):
    deletado = deletarLocalizacao(id_localizacao)
    return Response(status=200 if deletado else 404)




# Rotas para Contatos
@app.get('/contatos')
def listar_contatos():
    contatos = listarContatos()
    lista = [{'id_contato': contato['id_contato'], 'email': contato['email'], 'telefone': contato['telefone'], 'id_local': contato['id_local']} for contato in contatos]
    return jsonify(lista)

@app.get('/contatos/<int:id_contato>')
def obter_contato(id_contato):
    contato = obterContato(id_contato)
    if contato:
        return jsonify({
            'id_contato': contato['id_contato'],
            'email': contato['email'],
            'telefone': contato['telefone'],
            'id_local': contato['id_local']
        })
    else:
        return Response(status=404)

@app.post('/criar-contatos')
def criar_contato():
    dados = request.json
    email = dados.get('email')
    telefone = dados.get('telefone')
    id_local = dados.get('id_local')
    
    criarContato(email, telefone, id_local)
    return Response(status=201)

@app.put('/atualizar-contatos/<int:id_contato>')
def atualizar_contato(id_contato):
    dados = request.json
    email = dados.get('email')
    telefone = dados.get('telefone')
    id_local = dados.get('id_local')
    
    atualizado = atualizarContato(id_contato, email, telefone, id_local)
    return Response(status=200 if atualizado else 404)

@app.delete('/deletar-contatos/<int:id_contato>')
def deletar_contato(id_contato):
    deletado = deletarContato(id_contato)
    return Response(status=200 if deletado else 404)





# Rotas para Entradas
@app.get('/entradas')
def listar_entradas():
    entradas = listarEntradas()
    lista = [{'id_entrada': entrada['id_entrada'], 'nome_entrada': entrada['nome_entrada'], 'id_local': entrada['id_local']} for entrada in entradas]
    return jsonify(lista)

@app.get('/entradas/<int:id_entrada>')
def obter_entrada(id_entrada):
    entrada = obterEntrada(id_entrada)
    if entrada:
        return jsonify({
            'id_entrada': entrada['id_entrada'],
            'nome_entrada': entrada['nome_entrada'],
            'id_local': entrada['id_local']
        })
    else:
        return Response(status=404)

@app.post('/criar-entradas')
def criar_entrada():
    dados = request.json
    nome_entrada = dados.get('nome_entrada')
    id_local = dados.get('id_local')
    
    criarEntrada(nome_entrada, id_local)
    return Response(status=201)

@app.put('/atualizar-entradas/<int:id_entrada>')
def atualizar_entrada(id_entrada):
    dados = request.json
    nome_entrada = dados.get('nome_entrada')
    id_local = dados.get('id_local')
    
    atualizado = atualizarEntrada(id_entrada, nome_entrada, id_local)
    return Response(status=200 if atualizado else 404)

@app.delete('/deletar-entradas/<int:id_entrada>')
def deletar_entrada(id_entrada):
    deletado = deletarEntrada(id_entrada)
    return Response(status=200 if deletado else 404)








# Rotas para Catracas
@app.get('/catracas')
def listar_catracas():
    catracas = listarCatracas()
    lista = [{'id_catraca': catraca['id_catraca'], 'nome_catraca': catraca['nome_catraca'], 'id_local': catraca['id_local']} for catraca in catracas]
    return jsonify(lista)

@app.get('/catracas/<int:id_catraca>')
def obter_catraca(id_catraca):
    catraca = obterCatraca(id_catraca)
    if catraca:
        return jsonify({
            'id_catraca': catraca['id_catraca'],
            'nome_catraca': catraca['nome_catraca'],
            'id_local': catraca['id_local']
        })
    else:
        return Response(status=404)

@app.post('/criar-catracas')
def criar_catraca():
    dados = request.json
    nome_catraca = dados.get('nome_catraca')
    id_local = dados.get('id_local')
    
    criarCatraca(nome_catraca, id_local)
    return Response(status=201)

@app.put('/atualizar-catracas/<int:id_catraca>')
def atualizar_catraca(id_catraca):
    dados = request.json
    nome_catraca = dados.get('nome_catraca')
    id_local = dados.get('id_local')
    
    atualizado = atualizarCatraca(id_catraca, nome_catraca, id_local)
    return Response(status=200 if atualizado else 404)

@app.delete('/deletar-catracas/<int:id_catraca>')
def deletar_catraca(id_catraca):
    deletado = deletarCatraca(id_catraca)
    return Response(status=200 if deletado else 404)






# Rotas para Eventos
@app.get('/eventos')
def listar_eventos():
    eventos = listarEventos()
    lista = [{
        'id_evento': evento['id_evento'],
        'nome': evento['nome'],
        'data_evento': evento['data_evento'],
        'horario_evento': str(evento['horario_evento']),  # Converte para string
        'tipo': evento['tipo'],
        'id_local': evento['id_local']
    } for evento in eventos]
    return jsonify(lista)

@app.get('/eventos/<int:id_evento>')
def obter_evento(id_evento):
    evento = obterEvento(id_evento)
    if evento:
        return jsonify({
            'id_evento': evento['id_evento'],
            'nome': evento['nome'],
            'data_evento': evento['data_evento'],
            'horario_evento': str(evento['horario_evento']),  
            'tipo': evento['tipo'],
            'id_local': evento['id_local']
        })
    else:
        return Response(status=404)

@app.post('/criar-eventos')
def criar_evento():
    dados = request.json
    nome = dados.get('nome')
    data_evento = dados.get('data_evento')
    horario_evento = dados.get('horario_evento')
    tipo = dados.get('tipo')
    id_local = dados.get('id_local')
    
    criarEvento(nome, data_evento, horario_evento, tipo, id_local)
    return Response(status=201)

@app.put('/atualizar-eventos/<int:id_evento>')
def atualizar_evento(id_evento):
    dados = request.json
    nome = dados.get('nome')
    data_evento = dados.get('data_evento')
    horario_evento = dados.get('horario_evento')
    tipo = dados.get('tipo')
    id_local = dados.get('id_local')
    
    atualizado = atualizarEvento(id_evento, nome, data_evento, horario_evento, tipo, id_local)
    return Response(status=200 if atualizado else 404)

@app.delete('/deletar-eventos/<int:id_evento>')
def deletar_evento(id_evento):
    deletado = deletarEvento(id_evento)
    return Response(status=200 if deletado else 404)

if __name__ == '__main__':
    app.run(host=config.host, port=config.port, debug=True)
