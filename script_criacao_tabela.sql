USE DB_IMAGEM

CREATE TABLE TB_CADASTRO_IMAGEM(
ID_IMAGEM INT PRIMARY KEY IDENTITY (100,1), -- Auto Increment, come�a a partir do 100, sempre de 1 em 1 digito.
NOME_ARQUIVO VARCHAR(100) NOT NULL,
CLASSIF_IMAGEM VARCHAR(100) NOT NULL,
IMAGEM_BASE64 VARCHAR(MAX) NOT NULL,
DATA_CADASTRO DATETIME, -- GETDATE
DESCR_IMAGEM VARCHAR(500),

)

INSERT INTO TB_CADASTRO_IMAGEM (ID_IMAGEM, NOME_ARQUIVO, CLASSIF_IMAGEM, IMAGEM_BASE64, DATA_CADASTRO, DESCR_IMAGEM)
VALUES
('imagem_1.png', 'Classifica��o tipo 4', 'codigobase64...', GETDATE(), 'Imagem apresenta uma flor de colora��o rosa...')
('imagem_2.jpeg', 'Classifica��o tipo 7', 'codigobase64...', GETDATE(), 'Imagem apresenta uma bola de futebol...')

-- Nos campos de IMAGEM_BASE64 sera inserido os encodes das imagens que podem ser adquiridos em sites como https://base64.guru/converter/encode/image
-- N�o colequei o encode para encurtar o c�digo



