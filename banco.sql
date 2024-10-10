CREATE DATABASE onEntreeDB;

USE onEntreeDB;

CREATE TABLE locais (
    id_local INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    apelido VARCHAR(255),
    tipo VARCHAR(255) NOT NULL,
    cnpj VARCHAR(18) NOT NULL UNIQUE
);

CREATE TABLE localizacao (
    id_localizacao INT AUTO_INCREMENT PRIMARY KEY,
    cidade VARCHAR(100) NOT NULL,
    estado VARCHAR(100) NOT NULL,
    cep VARCHAR(10) NOT NULL,
    complemento VARCHAR(255),
    endereco VARCHAR(255) NOT NULL,
    id_local INT,
    FOREIGN KEY (id_local) REFERENCES locais(id_local)
);

CREATE TABLE contato (
    id_contato INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255),
    telefone VARCHAR(20),
    id_local INT,
    FOREIGN KEY (id_local) REFERENCES locais(id_local)
);

CREATE TABLE entradas (
    id_entrada INT AUTO_INCREMENT PRIMARY KEY,
    nome_entrada VARCHAR(255) NOT NULL,
    id_local INT,
    FOREIGN KEY (id_local) REFERENCES locais(id_local)
);

CREATE TABLE catracas (
    id_catraca INT AUTO_INCREMENT PRIMARY KEY,
    nome_catraca VARCHAR(255) NOT NULL,
    id_local INT,
    FOREIGN KEY (id_local) REFERENCES locais(id_local)
);

CREATE TABLE eventos (
    id_evento INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    data_evento DATE NOT NULL,
    horario_evento TIME NOT NULL,
    tipo VARCHAR(255) NOT NULL,
    id_local INT,
    FOREIGN KEY (id_local) REFERENCES locais(id_local)
);


SELECT * FROM locais;
SELECT * FROM localizacao;
SELECT * FROM contato;
SELECT * FROM entradas;
SELECT * FROM catracas;
SELECT * FROM eventos;

