CREATE TABLE resultados_4T2024 (
                                   razao_social VARCHAR(255),
                                   registro_ans VARCHAR(20),
                                   descricao VARCHAR(500),
                                   total_despesas DECIMAL(15, 2)
);

CREATE TABLE resultados_2024 (
                                 razao_social VARCHAR(255),
                                 registro_ans VARCHAR(20),
                                 descricao VARCHAR(500),
                                 total_despesas DECIMAL(15, 2)
);


INSERT INTO resultados_4T2024 (razao_social, registro_ans, descricao, total_despesas)
SELECT
    o.razao_social,
    d.registro_ans,
    d.descricao,
    SUM(d.vl_saldo_final - d.vl_saldo_inicial) AS total_despesas
FROM
    demonstracoes_contabeis d
        JOIN
    operadoras o ON d.registro_ans = o.registro_ans
WHERE
    d.descricao LIKE '%EVENTOS/SINISTROS CONHECIDOS%'
  AND d.data BETWEEN '2024-10-01' AND '2024-12-31' -- Dados do 4º trimestre de 2024
GROUP BY
    d.registro_ans, o.razao_social, d.descricao
ORDER BY
    total_despesas DESC
LIMIT 10;

INSERT INTO resultados_2024 (razao_social, registro_ans, descricao, total_despesas)
SELECT
    o.razao_social,
    d.registro_ans,
    d.descricao,
    SUM(d.vl_saldo_final - d.vl_saldo_inicial) AS total_despesas
FROM
    demonstracoes_contabeis d
        JOIN
    operadoras o ON d.registro_ans = o.registro_ans
WHERE
    d.descricao LIKE '%EVENTOS/SINISTROS CONHECIDOS%'
  AND YEAR(d.data) = 2024
GROUP BY
    d.registro_ans, o.razao_social, d.descricao
ORDER BY
    total_despesas DESC
LIMIT 10;
