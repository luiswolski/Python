CREATE SCHEMA `clientes` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;
USE clientes;
CREATE TABLE `clientes`.`clientes` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `nome` VARCHAR(255) NULL,
    `sobrenome` VARCHAR(255) NULL,
    `idade` INT(11) NULL,
    `peso` FLOAT NULL,
    PRIMARY KEY (`id`)
)  ENGINE=INNODB DEFAULT CHARACTER SET=UTF8MB4 COLLATE = UTF8MB4_BIN;
INSERT INTO clientes.clientes (nome, sobrenome, idade, peso) VALUES 
('Luiz', 'Otávio', 20, 100), ('Maria', 'Inês', 50, 57), ('Joana', 'Silva', 32, 78), ('Roberto', 'Oliveira', 27, 87), 
('Fabrício', 'Felix', 35, 99);