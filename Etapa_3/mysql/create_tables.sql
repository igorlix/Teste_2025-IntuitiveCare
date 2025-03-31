USE ans;

SET GLOBAL local_infile = 1;

DROP TABLE IF EXISTS demonstracoes_contabeis;
DROP TABLE IF EXISTS operadoras;

CREATE TABLE operadoras (
                            registro_ans VARCHAR(20) PRIMARY KEY,
                            cnpj VARCHAR(20),
                            razao_social VARCHAR(255),
                            nome_fantasia VARCHAR(255),
                            modalidade VARCHAR(100),
                            logradouro VARCHAR(255),
                            numero VARCHAR(20),
                            complemento VARCHAR(100),
                            bairro VARCHAR(100),
                            cidade VARCHAR(100),
                            uf VARCHAR(2),
                            cep VARCHAR(10),
                            ddd VARCHAR(5),
                            telefone VARCHAR(20),
                            fax VARCHAR(20),
                            endereco_eletronico VARCHAR(100),
                            representante VARCHAR(100),
                            cargo_representante VARCHAR(100),
                            regiao_comercializacao VARCHAR(100),
                            data_registro_ans DATE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE demonstracoes_contabeis (
                                         id INT AUTO_INCREMENT PRIMARY KEY,
                                         data DATE,
                                         registro_ans VARCHAR(20),
                                         cd_conta_contabil VARCHAR(20),
                                         descricao VARCHAR(500),
                                         vl_saldo_inicial DECIMAL(15,2),
                                         vl_saldo_final DECIMAL(15,2),
                                         FOREIGN KEY (registro_ans) REFERENCES operadoras(registro_ans)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



-- Índices para melhorar desempenho
CREATE INDEX idx_dem_contabeis_registro ON demonstracoes_contabeis(registro_ans);
CREATE INDEX idx_dem_contabeis_data_desc ON demonstracoes_contabeis(data, descricao(100));