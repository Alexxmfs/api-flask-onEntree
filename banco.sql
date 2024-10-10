CREATE DATABASE onEntreeDB;
USE onEntreeDB;

CREATE TABLE locais (
    id_local INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    apelido VARCHAR(255),
    tipo VARCHAR(255) NOT NULL,
    cnpj VARCHAR(18) NOT NULL UNIQUE,
    
    cidade VARCHAR(100) NOT NULL,
    estado VARCHAR(100) NOT NULL,
    cep VARCHAR(10) NOT NULL,
    complemento VARCHAR(255),
    endereco VARCHAR(255) NOT NULL,
    
    email VARCHAR(255),
    telefone VARCHAR(20),

    nome_entrada VARCHAR(255) NOT NULL,
    nome_catraca VARCHAR(255) NOT NULL
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
SELECT * FROM eventos;