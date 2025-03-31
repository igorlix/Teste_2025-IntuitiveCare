# 📚 **TRANSFORMARDADOS.md Etapa 2 (Teste de Nivelamento)**

## 📌 **Descrição do Problema**
Esta documentação é referente à Etapa 2 do teste técnico para estágio, que consiste na extração dos dados de uma tabela rol em pdf e conversão em formato .csv

Este projeto consiste em um teste de transformação e validação de dados com o objetivo de extrair, tratar e armazenar as informações da tabela "**Rol de Procedimentos e Eventos em Saúde**" do arquivo PDF fornecido pelo Anexo I do teste anterior. Além disso, deveriam ser substituídas as abreviações nas colunas "**OD**" (Odontológica) e "**AMB**" (Ambulatorial) pelas respectivas descrições completas. Posteriormente, foi necessário salvar esses dados tratados em formato CSV, compactá-los num arquivo ZIP e validar a precisão da extração e transformação.
Embora não solicitado explicitamente no enunciado original, uma validação adicional foi realizada comparando o arquivo CSV gerado com uma versão XLSX oficial da tabela, obtida diretamente no mesmo site do PDF original, visando garantir a integridade e qualidade esperada dos dados extraídos.
## 📌 **Como foi Resolvido**
O problema foi abordado com os seguintes passos principais:
1. **Extração dos dados do PDF**:
    - Feita através da biblioteca **pdfplumber**, extraindo tabelas de todas as páginas do documento.

2. **Tratamento e estruturação dos dados**:
    - Criação de um DataFrame Python (`pandas`), realizando padronização textual (remoção de acentuação, espaços extras e valores inválidos ou nulos).
    - Substituição automática de abreviações ("OD" e "AMB") pelas descrições completas conforme a legenda apresentada no próprio documento oficial.

3. **Armazenamento dos resultados**:
    - Exportação da tabela processada e estruturada para formato **CSV**.
    - Compactação do CSV final em um arquivo ZIP nomeado `Igor_Lixandrao_Santos.zip`.

4. **Validação aprimorada (extra)**:
    - Embora esta etapa não estivesse descrita explicitamente no teste, foi realizada uma verificação adicional, com a comparação criteriosa do CSV gerado com uma tabela XLSX oficial obtida diretamente do mesmo site. Essa validação verificou discrepâncias de valores, linhas faltantes ou extras e testou consistências de colunas e formato, garantindo alto nível de confiança na extração executada.

## 📌 **Resultados obtidos**
- Arquivo CSV devidamente estruturado e tratado.
- Compactação bem-sucedida em um arquivo ZIP para entrega conforme solicitado.
- Ferramenta adicional criada para validar a conformidade do CSV gerado com a tabela XLSX oficial obtida no mesmo site, proporcionando uma camada extra de segurança e qualidade nos dados tratados.

