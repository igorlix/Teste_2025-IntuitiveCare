# Teste de Nivelamento - IntuitiveCare
Este projeto tem como objetivo atender as etapas do teste de nivelamento para a vaga de estagiário na **IntuitiveCare**.
## 🛠️ Tecnologias Utilizadas

![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Vue.js](https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D)
![IntelliJ IDEA](https://img.shields.io/badge/IntelliJ_IDEA-000000.svg?style=for-the-badge&logo=intellij-idea&logoColor=white)

## 📌 Etapas Realizadas:
1. [**TESTE DE WEB SCRAPING**](Etapa_1/SCRAPING.md)
2. [**TESTE DE TRANSFORMAÇÃO DE DADOS**](Etapa_2/TRANSFORMARDADOS.md)
3. [**TESTE DE BANCO DE DADOS**](Etapa_3/DADOS.md)
4. [**TESTE DE API e Web Interface**](Etapa_4/API.md)

## 📂 Estrutura Geral do Repositório
``` plaintext
Teste-IntuitiveCare
├── Etapa_1               # Web Scraping
│   ├── src
│   │   ├── main
│   │   │   ├── java.br.com.intuitivecare.scraping
│   │   │   │   ├── modelo (Anexo)
│   │   │   │   ├── MainScraping
│   │   │   │   ├── PDFBaixar
│   │   │   │   └── PDFCompactar
│   │   │   └── output
│   │   │       ├── anexos/
│   │   │       └── Anexos.zip
│   │   └── test.java.br.com.intuitivecare
│   └── SCRAPING.md
│
├── Etapa_2               # Transformação de Dados
│   ├── input
│   │   ├── Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf
│   │   └── Anexo_I_Rol_2021RN_465.2021_RN627L.2024.xlsx
│   ├── output
│   │   ├── relatorio_comparacao_completo.txt
│   │   ├── relatorio_comparacao_final.txt
│   │   └── Teste_Igor_Lixandrao_Santos.zip
│   ├── utils
│   │   ├── comparison.py
│   │   ├── data_processing.py
│   │   ├── pdf_utils.py
│   │   ├── xlsx_utils.py
│   │   └── __init__.py
│   ├── main.py
│   ├── DADOS.md
│   └── TRANSFORMARDADOS.md
│
├── Etapa_3               # Banco de Dados 
│   ├── dados
│   │   ├── contabeis
│   │   └── operadoras
│   ├── imagens
│   ├── mysql
│   │   ├── create_tables.sql
│   │   ├── load_data.sql
│   │   └── queries_analiticas.sql
│   └── DADOS.md
│
├── Etapa_4               # API e Frontend (Interface Web)
│   ├── backend
│   │   ├── app
│   │   │   ├── data
│   │   │   ├── main.py
│   │   │   ├── routes.py
│   │   │   └── utils.py
│   │   ├── test
│   │   └── requirements.txt
│   ├── public
│   ├── src
│   │   ├── assets
│   │   ├── components
│   │   │   ├── ResultCard.vue
│   │   │   ├── SearchControls.vue
│   │   │   ├── SearchHeader.vue
│   │   │   └── SearchResults.vue
│   │   ├── App.vue
│   │   └── main.js
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js 
│   └── API.md
│
└── README.md          
```
## 📝 Detalhes das Etapas
### 🌐 Etapa 1 - Web Scraping:
- Utilizando Java para baixar e compactar arquivos PDF a partir de links específicos fornecidos, salvando no formato `.zip`.

### 🔄 Etapa 2 - Transformação de Dados:
- Utilização de Python para extrair, processar e comparar dados em PDF e planilhas XLSX, gerando um arquivo CSV consolidado, análises comparativas e relatórios detalhados em formato `.zip` e `.txt`.

### 📚 Etapa 3 - Banco de Dados:
- Uso do MySQL para armazenar e consultar dados estruturados, realizando análises detalhadas.

### ⚙️ Etapa 4 - API e Interface Web:
- Integração de API Flask com frontend desenvolvido em Vue.js para uma interface interativa.
