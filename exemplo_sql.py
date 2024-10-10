from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
import config

engine = create_engine(config.conn_str)

# Funções para Locais (já existentes)
def listarLocais():
    with Session(engine) as sessao:
        locais = sessao.execute(text("SELECT id_local, nome, tipo, cnpj FROM locais ORDER BY nome")).fetchall()
        lista_locais = [{'id_local': local.id_local, 'nome': local.nome, 'tipo': local.tipo, 'cnpj': local.cnpj} for local in locais]
        return lista_locais

def obterLocal(id_local):
    with Session(engine) as sessao:
        parametros = {'id_local': id_local}
        local = sessao.execute(
            text("SELECT id_local, nome, apelido, tipo, cnpj FROM locais WHERE id_local = :id_local"),
            parametros
        ).first()
        if local:
            return {
                'id_local': local.id_local,
                'nome': local.nome,
                'apelido': local.apelido,
                'tipo': local.tipo,
                'cnpj': local.cnpj
            }
        return None

def criarLocal(nome, apelido, tipo, cnpj):
    with Session(engine) as sessao, sessao.begin():
        local = {
            'nome': nome,
            'apelido': apelido,
            'tipo': tipo,
            'cnpj': cnpj
        }
        sessao.execute(
            text("INSERT INTO locais (nome, apelido, tipo, cnpj) VALUES (:nome, :apelido, :tipo, :cnpj)"),
            local
        )

def atualizarLocal(id_local, nome, apelido, tipo, cnpj):
    with Session(engine) as sessao, sessao.begin():
        parametros = {
            'id_local': id_local,
            'nome': nome,
            'apelido': apelido,
            'tipo': tipo,
            'cnpj': cnpj
        }
        resultado = sessao.execute(
            text("UPDATE locais SET nome = :nome, apelido = :apelido, tipo = :tipo, cnpj = :cnpj WHERE id_local = :id_local"),
            parametros
        )
        return resultado.rowcount > 0

def deletarLocal(id_local):
    with Session(engine) as sessao, sessao.begin():
        parametros = {'id_local': id_local}
        resultado = sessao.execute(
            text("DELETE FROM locais WHERE id_local = :id_local"),
            parametros
        )
        return resultado.rowcount > 0




# Funções para Localização
def listarLocalizacoes():
    with Session(engine) as sessao:
        localizacoes = sessao.execute(text("SELECT id_localizacao, cidade, estado, cep, complemento, endereco, id_local FROM localizacao ORDER BY cidade")).fetchall()
        lista_localizacoes = [{'id_localizacao': loc.id_localizacao, 'cidade': loc.cidade, 'estado': loc.estado, 'cep': loc.cep, 'complemento': loc.complemento, 'endereco': loc.endereco, 'id_local': loc.id_local} for loc in localizacoes]
        return lista_localizacoes

def obterLocalizacao(id_localizacao):
    with Session(engine) as sessao:
        parametros = {'id_localizacao': id_localizacao}
        localizacao = sessao.execute(
            text("SELECT id_localizacao, cidade, estado, cep, complemento, endereco, id_local FROM localizacao WHERE id_localizacao = :id_localizacao"),
            parametros
        ).first()
        if localizacao:
            return {
                'id_localizacao': localizacao.id_localizacao,
                'cidade': localizacao.cidade,
                'estado': localizacao.estado,
                'cep': localizacao.cep,
                'complemento': localizacao.complemento,
                'endereco': localizacao.endereco,
                'id_local': localizacao.id_local
            }
        return None

def criarLocalizacao(cidade, estado, cep, complemento, endereco, id_local):
    with Session(engine) as sessao, sessao.begin():
        localizacao = {
            'cidade': cidade,
            'estado': estado,
            'cep': cep,
            'complemento': complemento,
            'endereco': endereco,
            'id_local': id_local
        }
        sessao.execute(
            text("INSERT INTO localizacao (cidade, estado, cep, complemento, endereco, id_local) VALUES (:cidade, :estado, :cep, :complemento, :endereco, :id_local)"),
            localizacao
        )

def atualizarLocalizacao(id_localizacao, cidade, estado, cep, complemento, endereco, id_local):
    with Session(engine) as sessao, sessao.begin():
        parametros = {
            'id_localizacao': id_localizacao,
            'cidade': cidade,
            'estado': estado,
            'cep': cep,
            'complemento': complemento,
            'endereco': endereco,
            'id_local': id_local
        }
        resultado = sessao.execute(
            text("UPDATE localizacao SET cidade = :cidade, estado = :estado, cep = :cep, complemento = :complemento, endereco = :endereco, id_local = :id_local WHERE id_localizacao = :id_localizacao"),
            parametros
        )
        return resultado.rowcount > 0

def deletarLocalizacao(id_localizacao):
    with Session(engine) as sessao, sessao.begin():
        parametros = {'id_localizacao': id_localizacao}
        resultado = sessao.execute(
            text("DELETE FROM localizacao WHERE id_localizacao = :id_localizacao"),
            parametros
        )
        return resultado.rowcount > 0





# Funções para Contatos
def listarContatos():
    with Session(engine) as sessao:
        contatos = sessao.execute(text("SELECT id_contato, email, telefone, id_local FROM contato ORDER BY email")).fetchall()
        lista_contatos = [{'id_contato': contato.id_contato, 'email': contato.email, 'telefone': contato.telefone, 'id_local': contato.id_local} for contato in contatos]
        return lista_contatos

def obterContato(id_contato):
    with Session(engine) as sessao:
        parametros = {'id_contato': id_contato}
        contato = sessao.execute(
            text("SELECT id_contato, email, telefone, id_local FROM contato WHERE id_contato = :id_contato"),
            parametros
        ).first()
        if contato:
            return {
                'id_contato': contato.id_contato,
                'email': contato.email,
                'telefone': contato.telefone,
                'id_local': contato.id_local
            }
        return None

def criarContato(email, telefone, id_local):
    with Session(engine) as sessao, sessao.begin():
        contato = {
            'email': email,
            'telefone': telefone,
            'id_local': id_local
        }
        sessao.execute(
            text("INSERT INTO contato (email, telefone, id_local) VALUES (:email, :telefone, :id_local)"),
            contato
        )

def atualizarContato(id_contato, email, telefone, id_local):
    with Session(engine) as sessao, sessao.begin():
        parametros = {
            'id_contato': id_contato,
            'email': email,
            'telefone': telefone,
            'id_local': id_local
        }
        resultado = sessao.execute(
            text("UPDATE contato SET email = :email, telefone = :telefone, id_local = :id_local WHERE id_contato = :id_contato"),
            parametros
        )
        return resultado.rowcount > 0

def deletarContato(id_contato):
    with Session(engine) as sessao, sessao.begin():
        parametros = {'id_contato': id_contato}
        resultado = sessao.execute(
            text("DELETE FROM contato WHERE id_contato = :id_contato"),
            parametros
        )
        return resultado.rowcount > 0








# Funções para Entradas
def listarEntradas():
    with Session(engine) as sessao:
        entradas = sessao.execute(text("SELECT id_entrada, nome_entrada, id_local FROM entradas ORDER BY nome_entrada")).fetchall()
        lista_entradas = [{'id_entrada': entrada.id_entrada, 'nome_entrada': entrada.nome_entrada, 'id_local': entrada.id_local} for entrada in entradas]
        return lista_entradas

def obterEntrada(id_entrada):
    with Session(engine) as sessao:
        parametros = {'id_entrada': id_entrada}
        entrada = sessao.execute(
            text("SELECT id_entrada, nome_entrada, id_local FROM entradas WHERE id_entrada = :id_entrada"),
            parametros
        ).first()
        if entrada:
            return {
                'id_entrada': entrada.id_entrada,
                'nome_entrada': entrada.nome_entrada,
                'id_local': entrada.id_local
            }
        return None

def criarEntrada(nome_entrada, id_local):
    with Session(engine) as sessao, sessao.begin():
        entrada = {
            'nome_entrada': nome_entrada,
            'id_local': id_local
        }
        sessao.execute(
            text("INSERT INTO entradas (nome_entrada, id_local) VALUES (:nome_entrada, :id_local)"),
            entrada
        )

def atualizarEntrada(id_entrada, nome_entrada, id_local):
    with Session(engine) as sessao, sessao.begin():
        parametros = {
            'id_entrada': id_entrada,
            'nome_entrada': nome_entrada,
            'id_local': id_local
        }
        resultado = sessao.execute(
            text("UPDATE entradas SET nome_entrada = :nome_entrada, id_local = :id_local WHERE id_entrada = :id_entrada"),
            parametros
        )
        return resultado.rowcount > 0

def deletarEntrada(id_entrada):
    with Session(engine) as sessao, sessao.begin():
        parametros = {'id_entrada': id_entrada}
        resultado = sessao.execute(
            text("DELETE FROM entradas WHERE id_entrada = :id_entrada"),
            parametros
        )
        return resultado.rowcount > 0
    
    
    
    
    
    
    
    # Funções para Catracas
def listarCatracas():
    with Session(engine) as sessao:
        catracas = sessao.execute(text("SELECT id_catraca, nome_catraca, id_local FROM catracas ORDER BY nome_catraca")).fetchall()
        lista_catracas = [{'id_catraca': catraca.id_catraca, 'nome_catraca': catraca.nome_catraca, 'id_local': catraca.id_local} for catraca in catracas]
        return lista_catracas

def obterCatraca(id_catraca):
    with Session(engine) as sessao:
        parametros = {'id_catraca': id_catraca}
        catraca = sessao.execute(
            text("SELECT id_catraca, nome_catraca, id_local FROM catracas WHERE id_catraca = :id_catraca"),
            parametros
        ).first()
        if catraca:
            return {
                'id_catraca': catraca.id_catraca,
                'nome_catraca': catraca.nome_catraca,
                'id_local': catraca.id_local
            }
        return None

def criarCatraca(nome_catraca, id_local):
    with Session(engine) as sessao, sessao.begin():
        catraca = {
            'nome_catraca': nome_catraca,
            'id_local': id_local
        }
        sessao.execute(
            text("INSERT INTO catracas (nome_catraca, id_local) VALUES (:nome_catraca, :id_local)"),
            catraca
        )

def atualizarCatraca(id_catraca, nome_catraca, id_local):
    with Session(engine) as sessao, sessao.begin():
        parametros = {
            'id_catraca': id_catraca,
            'nome_catraca': nome_catraca,
            'id_local': id_local
        }
        resultado = sessao.execute(
            text("UPDATE catracas SET nome_catraca = :nome_catraca, id_local = :id_local WHERE id_catraca = :id_catraca"),
            parametros
        )
        return resultado.rowcount > 0

def deletarCatraca(id_catraca):
    with Session(engine) as sessao, sessao.begin():
        parametros = {'id_catraca': id_catraca}
        resultado = sessao.execute(
            text("DELETE FROM catracas WHERE id_catraca = :id_catraca"),
            parametros
        )
        return resultado.rowcount > 0
    




# Funções para Eventos
def listarEventos():
    with Session(engine) as sessao:
        eventos = sessao.execute(text("SELECT id_evento, nome, data_evento, horario_evento, tipo, id_local FROM eventos ORDER BY data_evento")).fetchall()
        lista_eventos = [{'id_evento': evento.id_evento, 'nome': evento.nome, 'data_evento': evento.data_evento, 'horario_evento': evento.horario_evento, 'tipo': evento.tipo, 'id_local': evento.id_local} for evento in eventos]
        return lista_eventos

def obterEvento(id_evento):
    with Session(engine) as sessao:
        parametros = {'id_evento': id_evento}
        evento = sessao.execute(
            text("SELECT id_evento, nome, data_evento, horario_evento, tipo, id_local FROM eventos WHERE id_evento = :id_evento"),
            parametros
        ).first()
        if evento:
            return {
                'id_evento': evento.id_evento,
                'nome': evento.nome,
                'data_evento': evento.data_evento,
                'horario_evento': evento.horario_evento,
                'tipo': evento.tipo,
                'id_local': evento.id_local
            }
        return None

def criarEvento(nome, data_evento, horario_evento, tipo, id_local):
    with Session(engine) as sessao, sessao.begin():
        evento = {
            'nome': nome,
            'data_evento': data_evento,
            'horario_evento': horario_evento,
            'tipo': tipo,
            'id_local': id_local
        }
        sessao.execute(
            text("INSERT INTO eventos (nome, data_evento, horario_evento, tipo, id_local) VALUES (:nome, :data_evento, :horario_evento, :tipo, :id_local)"),
            evento
        )

def atualizarEvento(id_evento, nome, data_evento, horario_evento, tipo, id_local):
    with Session(engine) as sessao, sessao.begin():
        parametros = {
            'id_evento': id_evento,
            'nome': nome,
            'data_evento': data_evento,
            'horario_evento': horario_evento,
            'tipo': tipo,
            'id_local': id_local
        }
        resultado = sessao.execute(
            text("UPDATE eventos SET nome = :nome, data_evento = :data_evento, horario_evento = :horario_evento, tipo = :tipo, id_local = :id_local WHERE id_evento = :id_evento"),
            parametros
        )
        return resultado.rowcount > 0

def deletarEvento(id_evento):
    with Session(engine) as sessao, sessao.begin():
        parametros = {'id_evento': id_evento}
        resultado = sessao.execute(
            text("DELETE FROM eventos WHERE id_evento = :id_evento"),
            parametros
        )
        return resultado.rowcount > 0