from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
import config

engine = create_engine(config.conn_str)

def listarLocaisPorNome(nome):
    with Session(engine) as sessao:
        parametros = {'nome': f'%{nome}%'}  # Usar '%' para pesquisa parcial
        locais = sessao.execute(
            text("SELECT * FROM locais WHERE nome LIKE :nome ORDER BY nome"),
            parametros
        ).fetchall()
        lista_locais = [
            {
                'id_local': local.id_local,
                'nome': local.nome,
                'apelido': local.apelido,
                'tipo': local.tipo,
                'cnpj': local.cnpj,
                'cidade': local.cidade,
                'estado': local.estado,
                'cep': local.cep,
                'complemento': local.complemento,
                'endereco': local.endereco,
                'email': local.email,
                'telefone': local.telefone,
                'nome_entrada': local.nome_entrada,
                'nome_catraca': local.nome_catraca,
                'data_atualizacao': str(local.data_atualizacao)
            } for local in locais
        ]
        return lista_locais


def listarLocais():
    with Session(engine) as sessao:
        locais = sessao.execute(
            text("SELECT * FROM locais ORDER BY nome")
        ).fetchall()
        lista_locais = [
            {
                'id_local': local.id_local,
                'nome': local.nome,
                'apelido': local.apelido,
                'tipo': local.tipo,
                'cnpj': local.cnpj,
                'cidade': local.cidade,
                'estado': local.estado,
                'cep': local.cep,
                'complemento': local.complemento,
                'endereco': local.endereco,
                'email': local.email,
                'telefone': local.telefone,
                'nome_entrada': local.nome_entrada,
                'nome_catraca': local.nome_catraca,
                'data_atualizacao': str(local.data_atualizacao)
            } for local in locais
        ]
        return lista_locais

def obterLocal(id_local):
    with Session(engine) as sessao:
        parametros = {'id_local': id_local}
        local = sessao.execute(
            text("SELECT * FROM locais WHERE id_local = :id_local"),
            parametros
        ).first()
        if local:
            return {
                'id_local': local.id_local,
                'nome': local.nome,
                'apelido': local.apelido,
                'tipo': local.tipo,
                'cnpj': local.cnpj,
                'cidade': local.cidade,
                'estado': local.estado,
                'cep': local.cep,
                'complemento': local.complemento,
                'endereco': local.endereco,
                'email': local.email,
                'telefone': local.telefone,
                'nome_entrada': local.nome_entrada,
                'nome_catraca': local.nome_catraca,
                'data_atualizacao': local.data_atualizacao
            }
        return None

def criarLocal(nome, apelido, tipo, cnpj, cidade, estado, cep, complemento, endereco, email, telefone, nome_entrada, nome_catraca):
    with Session(engine) as sessao, sessao.begin():
        local = {
            'nome': nome,
            'apelido': apelido,
            'tipo': tipo,
            'cnpj': cnpj,
            'cidade': cidade,
            'estado': estado,
            'cep': cep,
            'complemento': complemento,
            'endereco': endereco,
            'email': email,
            'telefone': telefone,
            'nome_entrada': nome_entrada,
            'nome_catraca': nome_catraca
        }
        sessao.execute(
            text(
                "INSERT INTO locais (nome, apelido, tipo, cnpj, cidade, estado, cep, complemento, endereco, email, telefone, nome_entrada, nome_catraca) "
                "VALUES (:nome, :apelido, :tipo, :cnpj, :cidade, :estado, :cep, :complemento, :endereco, :email, :telefone, :nome_entrada, :nome_catraca)"
            ),
            local
        )

def atualizarLocal(id_local, nome, apelido, tipo, cnpj, cidade, estado, cep, complemento, endereco, email, telefone, nome_entrada, nome_catraca):
    with Session(engine) as sessao, sessao.begin():
        parametros = {
            'id_local': id_local,
            'nome': nome,
            'apelido': apelido,
            'tipo': tipo,
            'cnpj': cnpj,
            'cidade': cidade,
            'estado': estado,
            'cep': cep,
            'complemento': complemento,
            'endereco': endereco,
            'email': email,
            'telefone': telefone,
            'nome_entrada': nome_entrada,
            'nome_catraca': nome_catraca
        }
        resultado = sessao.execute(
            text(
                "UPDATE locais SET nome = :nome, apelido = :apelido, tipo = :tipo, cnpj = :cnpj, "
                "cidade = :cidade, estado = :estado, cep = :cep, complemento = :complemento, endereco = :endereco, "
                "email = :email, telefone = :telefone, nome_entrada = :nome_entrada, nome_catraca = :nome_catraca "
                "WHERE id_local = :id_local"
            ),
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


def listarEventos():
    with Session(engine) as sessao:
        eventos = sessao.execute(
            text("SELECT * FROM eventos ORDER BY data_evento, horario_evento")
        ).fetchall()
        lista_eventos = [
            {
                'id_evento': evento.id_evento,
                'nome': evento.nome,
                'data_evento': evento.data_evento,
                'horario_evento': evento.horario_evento,
                'tipo': evento.tipo,
                'email': evento.email,
                'telefone': evento.telefone,
                'id_local': evento.id_local
            } for evento in eventos
        ]
        return lista_eventos

def obterEvento(id_evento):
    with Session(engine) as sessao:
        parametros = {'id_evento': id_evento}
        evento = sessao.execute(
            text("SELECT * FROM eventos WHERE id_evento = :id_evento"),
            parametros
        ).first()
        
        if evento:
            return {
                'id_evento': evento.id_evento,
                'nome': evento.nome,
                'data_evento': evento.data_evento,
                'horario_evento': str(evento.horario_evento),  
                'tipo': evento.tipo,
                'email': evento.email,
                'telefone': evento.telefone,
                'id_local': evento.id_local
            }
        return None

def criarEvento(nome, data_evento, horario_evento, tipo, email, telefone, id_local):
    with Session(engine) as sessao, sessao.begin():
        evento = {
            'nome': nome,
            'data_evento': data_evento,
            'horario_evento': horario_evento,
            'tipo': tipo,
            'email': email,
            'telefone': telefone,
            'id_local': id_local
        }
        sessao.execute(
            text(
                "INSERT INTO eventos (nome, data_evento, horario_evento, tipo, email, telefone, id_local) "
                "VALUES (:nome, :data_evento, :horario_evento, :tipo, :email, :telefone, :id_local)"
            ),
            evento
        )

def atualizarEvento(id_evento, nome, data_evento, horario_evento, tipo, email, telefone, id_local):
    with Session(engine) as sessao, sessao.begin():
        parametros = {
            'id_evento': id_evento,
            'nome': nome,
            'data_evento': data_evento,
            'horario_evento': horario_evento,
            'tipo': tipo,
            'email': email,
            'telefone': telefone,
            'id_local': id_local
        }
        resultado = sessao.execute(
            text(
                "UPDATE eventos SET nome = :nome, data_evento = :data_evento, "
                "horario_evento = :horario_evento, tipo = :tipo, email = :email, telefone = :telefone, id_local = :id_local "
                "WHERE id_evento = :id_evento"
            ),
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


def obterEventoComLocal(id_evento):
    with Session(engine) as sessao:
        parametros = {'id_evento': id_evento}
        evento_com_local = sessao.execute(
            text("""
                SELECT 
                    e.id_evento,
                    e.nome AS evento_nome,
                    e.data_evento,
                    e.horario_evento,
                    e.tipo AS evento_tipo,
                    e.email,
                    e.telefone,
                    e.id_local,
                    l.nome AS local_nome,
                    l.endereco AS local_endereco,
                    l.nome_entrada AS local_portões
                FROM 
                    eventos e
                INNER JOIN 
                    locais l ON e.id_local = l.id_local
                WHERE 
                    e.id_evento = :id_evento
            """),
            parametros
        ).first()

        if evento_com_local:
            return {
                'id_evento': evento_com_local.id_evento,
                'nome': evento_com_local.evento_nome,
                'data_evento': evento_com_local.data_evento,
                'horario_evento': str(evento_com_local.horario_evento), 
                'tipo': evento_com_local.evento_tipo,
                'email': evento_com_local.email,
                'telefone': evento_com_local.telefone,
                'id_local': evento_com_local.id_local,
                'local': {
                    'nome': evento_com_local.local_nome,
                    'endereco': evento_com_local.local_endereco,
                    'portões': evento_com_local.local_portões
                }
            }
        return None

def listarEventosComLocal():
    with Session(engine) as sessao:
        eventos = sessao.execute(
            text("""
                SELECT 
                    e.id_evento,
                    e.nome AS evento_nome,
                    e.data_evento,
                    e.horario_evento,
                    e.tipo AS evento_tipo,
                    e.email,
                    e.telefone,
                    e.id_local,
                    l.nome AS local_nome,
                    l.endereco AS local_endereco,
                    l.nome_entrada AS local_portões
                FROM 
                    eventos e
                INNER JOIN 
                    locais l ON e.id_local = l.id_local
                ORDER BY e.data_evento, e.horario_evento
            """)
        ).fetchall()
        lista_eventos = [
            {
                'id_evento': evento.id_evento,
                'nome': evento.evento_nome,
                'data_evento': evento.data_evento,
                'horario_evento': str(evento.horario_evento), 
                'tipo': evento.evento_tipo,
                'email': evento.email,
                'telefone': evento.telefone,
                'id_local': evento.id_local,
                'local': {
                    'nome': evento.local_nome,
                    'endereco': evento.local_endereco,
                    'portões': evento.local_portões
                }
            } for evento in eventos
        ]
        return lista_eventos

def listarEventosPorNome(nome):
    with Session(engine) as sessao:
        parametros = {'nome': f'%{nome}%'}
        eventos = sessao.execute(
            text("""
                SELECT 
                    e.id_evento,
                    e.nome AS evento_nome,
                    e.data_evento,
                    e.horario_evento,
                    e.tipo AS evento_tipo,
                    e.email,
                    e.telefone,
                    e.id_local,
                    l.nome AS local_nome,
                    l.endereco AS local_endereco,
                    l.nome_entrada AS local_portões
                FROM 
                    eventos e
                INNER JOIN 
                    locais l ON e.id_local = l.id_local
                WHERE 
                    e.nome LIKE :nome
                ORDER BY e.data_evento, e.horario_evento
            """),
            parametros
        ).fetchall()
        lista_eventos = [
            {
                'id_evento': evento.id_evento,
                'nome': evento.evento_nome,
                'data_evento': evento.data_evento,
                'horario_evento': str(evento.horario_evento), 
                'tipo': evento.evento_tipo,
                'email': evento.email,
                'telefone': evento.telefone,
                'id_local': evento.id_local,
                'local': {
                    'nome': evento.local_nome,
                    'endereco': evento.local_endereco,
                    'portões': evento.local_portões
                }
            } for evento in eventos
        ]
        return lista_eventos