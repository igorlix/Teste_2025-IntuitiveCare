
LOAD DATA LOCAL INFILE 'Etapa_3/dados/operadoras/Relatorio_cadop.csv'
    INTO TABLE operadoras
    FIELDS TERMINATED BY ';'
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS
    (registro_ans, cnpj, razao_social, nome_fantasia, modalidade,
     logradouro, numero, complemento, bairro, cidade, uf, cep,
     ddd, telefone, fax, endereco_eletronico, representante,
     cargo_representante, regiao_comercializacao, @data_registro_ans)
    SET data_registro_ans = STR_TO_DATE(@data_registro_ans, '%Y-%m-%d');


LOAD DATA LOCAL INFILE 'Etapa_3/dados/contabeis/2023/1T2023.csv'
    INTO TABLE demonstracoes_contabeis
    FIELDS TERMINATED BY ';'
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS
    (@data, registro_ans, cd_conta_contabil, descricao, @vl_saldo_inicial, @vl_saldo_final)
    SET
        data = STR_TO_DATE(@data, '%Y-%m-%d'),
        vl_saldo_inicial = REPLACE(REPLACE(@vl_saldo_inicial, '.', ''), ',', '.'),
        vl_saldo_final = REPLACE(REPLACE(@vl_saldo_final, '.', ''), ',', '.');

LOAD DATA LOCAL INFILE 'Etapa_3/dados/contabeis/2023/2t2023.csv'
    INTO TABLE demonstracoes_contabeis
    FIELDS TERMINATED BY ';'
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS
    (@data, registro_ans, cd_conta_contabil, descricao, @vl_saldo_inicial, @vl_saldo_final)
    SET
        data = STR_TO_DATE(@data, '%Y-%m-%d'),
        vl_saldo_inicial = REPLACE(REPLACE(@vl_saldo_inicial, '.', ''), ',', '.'),
        vl_saldo_final = REPLACE(REPLACE(@vl_saldo_final, '.', ''), ',', '.');

LOAD DATA LOCAL INFILE 'Etapa_3/dados/contabeis/2023/3T2023.csv'
    INTO TABLE demonstracoes_contabeis
    FIELDS TERMINATED BY ';'
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS
    (@data, registro_ans, cd_conta_contabil, descricao, @vl_saldo_inicial, @vl_saldo_final)
    SET
        data = STR_TO_DATE(@data, '%Y-%m-%d'),
        vl_saldo_inicial = REPLACE(REPLACE(@vl_saldo_inicial, '.', ''), ',', '.'),
        vl_saldo_final = REPLACE(REPLACE(@vl_saldo_final, '.', ''), ',', '.');

LOAD DATA LOCAL INFILE 'Etapa_3/dados/contabeis/2023/4T2023.csv'
    INTO TABLE demonstracoes_contabeis
    FIELDS TERMINATED BY ';'
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS
    (@data, registro_ans, cd_conta_contabil, descricao, @vl_saldo_inicial, @vl_saldo_final)
    SET
        data = STR_TO_DATE(@data, '%Y-%m-%d'),
        vl_saldo_inicial = REPLACE(REPLACE(@vl_saldo_inicial, '.', ''), ',', '.'),
        vl_saldo_final = REPLACE(REPLACE(@vl_saldo_final, '.', ''), ',', '.');

LOAD DATA LOCAL INFILE 'Etapa_3/dados/contabeis/2024/1T2024.csv'
    INTO TABLE demonstracoes_contabeis
    FIELDS TERMINATED BY ';'
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS
    (@data, registro_ans, cd_conta_contabil, descricao, @vl_saldo_inicial, @vl_saldo_final)
    SET
        data = STR_TO_DATE(@data, '%Y-%m-%d'),
        vl_saldo_inicial = REPLACE(REPLACE(@vl_saldo_inicial, '.', ''), ',', '.'),
        vl_saldo_final = REPLACE(REPLACE(@vl_saldo_final, '.', ''), ',', '.');

LOAD DATA LOCAL INFILE 'Etapa_3/dados/contabeis/2024/2T2024.csv'
    INTO TABLE demonstracoes_contabeis
    FIELDS TERMINATED BY ';'
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS
    (@data, registro_ans, cd_conta_contabil, descricao, @vl_saldo_inicial, @vl_saldo_final)
    SET
        data = STR_TO_DATE(@data, '%Y-%m-%d'),
        vl_saldo_inicial = REPLACE(REPLACE(@vl_saldo_inicial, '.', ''), ',', '.'),
        vl_saldo_final = REPLACE(REPLACE(@vl_saldo_final, '.', ''), ',', '.');

LOAD DATA LOCAL INFILE 'Etapa_3/dados/contabeis/2024/3T2024.csv'
    INTO TABLE demonstracoes_contabeis
    FIELDS TERMINATED BY ';'
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS
    (@data, registro_ans, cd_conta_contabil, descricao, @vl_saldo_inicial, @vl_saldo_final)
    SET
        data = STR_TO_DATE(@data, '%Y-%m-%d'),
        vl_saldo_inicial = REPLACE(REPLACE(@vl_saldo_inicial, '.', ''), ',', '.'),
        vl_saldo_final = REPLACE(REPLACE(@vl_saldo_final, '.', ''), ',', '.');

LOAD DATA LOCAL INFILE 'Etapa_3/dados/contabeis/2024/4T2024.csv'
    INTO TABLE demonstracoes_contabeis
    FIELDS TERMINATED BY ';'
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS
    (@data, registro_ans, cd_conta_contabil, descricao, @vl_saldo_inicial, @vl_saldo_final)
    SET
        data = STR_TO_DATE(@data, '%Y-%m-%d'),
        vl_saldo_inicial = REPLACE(REPLACE(@vl_saldo_inicial, '.', ''), ',', '.'),
        vl_saldo_final = REPLACE(REPLACE(@vl_saldo_final, '.', ''), ',', '.');

SELECT DISTINCT registro_ans
FROM demonstracoes_contabeis
WHERE registro_ans NOT IN (SELECT registro_ans FROM operadoras);

INSERT INTO operadoras (registro_ans, razao_social)
SELECT DISTINCT d.registro_ans, 'Operadora Desconhecida'
FROM demonstracoes_contabeis d
WHERE d.registro_ans NOT IN (SELECT registro_ans FROM operadoras);

SELECT COUNT(*) AS total FROM demonstracoes_contabeis;
SELECT COUNT(*) AS total FROM operadoras;

SELECT *
FROM demonstracoes_contabeis
LIMIT 10;

SELECT DISTINCT descricao
FROM demonstracoes_contabeis
WHERE descricao LIKE '%EVENTOS%';

CREATE INDEX idx_descricoes ON demonstracoes_contabeis(descricao(100));
CREATE INDEX idx_datas ON demonstracoes_contabeis(data);
CREATE INDEX idx_registro_demonstracoes ON demonstracoes_contabeis(registro_ans);

ALTER TABLE demonstracoes_contabeis
    ADD COLUMN total_despesas DECIMAL(15, 2) GENERATED ALWAYS AS (vl_saldo_final - vl_saldo_inicial) STORED;

