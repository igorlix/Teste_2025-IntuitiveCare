# Teste de Nivelamento - IntuitiveCare
Este projeto tem como objetivo atender as etapas do teste de nivelamento para a vaga de estagiário na IntuitiveCare.
## 🛠️ Tecnologias Utilizadas
![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Vue.js](https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D)
![IntelliJ IDEA](https://img.shields.io/badge/IntelliJ_IDEA-000000.svg?style=for-the-badge&logo=intellij-idea&logoColor=white)
## 📌 Etapas Realizadas:
### [1. TESTE DE WEB SCRAPING](Etapa_1/SCRAPING.md)

### [2. TESTE DE TRANSFORMAÇÃO DE DADOS](Etapa_2/TRANSFORMACAO.md)

### [3. TESTE DE BANCO DE DADOS](DADOS.md)

### [4. TESTE DE API e Web Interface](Etapa_4/API.md)

## 📂 Estrutura Geral do Repositório
``` 
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
├── Etapa_2               # Etapa não especificada
│
├── Etapa_3               # Banco de dados 
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
├── Etapa_4               # API e Frontend (Interface)
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
