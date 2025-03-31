# 📚 Etapa 2 - Teste de Nivelamento (Transformação de Dados)
## 📌 Descrição do Problema
Este projeto é a segunda etapa de um teste técnico de estágio e tem por objetivo extrair dados do arquivo PDF "Rol de Procedimentos e Eventos em Saúde", disponibilizado na etapa anterior. Os objetivos desta etapa são:
- **Extrair e estruturar** os dados a partir do PDF.
- **Substituir abreviações** das colunas "OD" (Seg. Odontológica) e "AMB" (Seg. Ambulatorial).
- Salvar os dados em formato estruturado (**CSV**).
- Compactar o resultado em arquivo **ZIP** denominado `Igor_Lixandrao_Santos.zip`.

Foi realizado também um passo adicional e não exigido originalmente:
- Validação detalhada através da comparação dos dados extraídos (CSV) com uma tabela XLSX oficial disponível no mesmo site do PDF para assegurar a precisão da transformação.

## 📌 Como foi resolvido (Entradas e Saídas)
### ✅ Extração dos dados em PDF
- **Entrada**: Documento PDF oficial.
- **Saída**: Lista estruturada contendo as tabelas extraídas (via `pdfplumber`).

### ✅ Processamento e transformação dos dados
- **Entrada**: Dados brutos extraídos do PDF.
- **Ações Realizadas**:
    - Conversão dos dados em formato tabular (`pandas DataFrame`).
    - Normalização textual (acentuações, espaços extras e valores inválidos).
    - Substituição das abreviações "OD" e "AMB".

- **Saída**: CSV estruturado com dados tratados.

### ✅ Exportação e Compactação dos Resultados
- **Entrada**: Dados estruturados em formato CSV.
- **Ação**: Criação de arquivo ZIP.
- **Saída**: Arquivo compactado denominado `Igor_Lixandrao_Santos.zip`.

### ✅ Validação adicional e comparação com XLSX Oficial
- **Entrada**: CSV gerado e arquivo XLSX original do site.
- **Ações Realizadas**:
    - Leitura e tratamento dos dados na tabela XLSX oficial.
    - Comparação criteriosa (valores faltantes, extras ou incorretos).

- **Resultado**: Garantia adicional de conformidade dos dados extraídos e transformados.

## 📌 Resultados Obtidos Resumidos
🔹 Arquivo **CSV** tratado e estruturado corretamente.
🔹 Compactação bem-sucedida gerando arquivo **ZIP** para entrega.
🔹 A validação extra forneceu maior segurança e qualidade, demonstrando melhor a precisão.
