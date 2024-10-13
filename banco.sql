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

	ALTER TABLE locais
	ADD COLUMN data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;

	ALTER TABLE eventos
	ADD COLUMN email VARCHAR(255);

	ALTER TABLE eventos
	ADD COLUMN telefone VARCHAR(20);

	INSERT INTO locais (id_local, nome, apelido, tipo, cnpj, cidade, estado, cep, complemento, endereco, email, telefone, nome_entrada, nome_catraca)
	VALUES 
	(1, 'Restaurante A', 'RestA', 'Restaurante', '12.345.678/0001-99', 'São Paulo', 'SP', '01000-000', 'Apto 101', 'Rua Exemplo, 123', 'contato@restaurantea.com', '(11) 1234-5678', 'Entrada Principal', 'Catraca 1'),
	(2, 'Bar B', 'BarB', 'Bar', '98.765.432/0001-88', 'Rio de Janeiro', 'RJ', '20000-000', 'Sala 202', 'Avenida Exemplo, 456', 'contato@barb.com', '(21) 9876-5432', 'Entrada Secundária', 'Catraca 2');


	INSERT INTO eventos (nome, data_evento, horario_evento, tipo, id_local)
	VALUES 
	('Show de Rock', '2024-11-15', '20:00:00', 'Música', 1),
	('Feira de Artesanato', '2024-12-01', '10:00:00', 'Feira', 1);


	SELECT * FROM locais;
	SELECT * FROM eventos;
