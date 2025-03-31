# 📚 Documentação do Processo de Scraping
Este documento descreve detalhadamente o sistema implementado para automatizar a captura e processamento dos arquivos PDF relacionados aos Anexos I e II de uma página web específica do Governo Brasileiro (ANS). O sistema realiza o scraping, identifica links relevantes, faz download dos arquivos PDF e os agrupa num arquivo ZIP único.
## 🔄 Fluxo de Execução
O processo compreende as seguintes etapas sequenciais:
1. **Busca de Anexos**
    - Acessa o conteúdo HTML usando Jsoup.
    - Extrai apenas links que contêm claramente "Anexo I" ou "Anexo II".

2. **Download dos PDFs**
    - Faz o download automatizado dos arquivos PDF identificados.
    - Salva os arquivos baixados no diretório configurado internamente.

3. **Compactação dos Arquivos**
    - Agrupa todos os PDFs baixados em um único arquivo ZIP.
    - Facilita distribuição e armazenamento unificado.

4. **Log de Execução**
    - Registra status no console em tempo real.
    - Detalha erros e progresso geral do sistema.
## 🚀 Configuração do Ambiente de Desenvolvimento
Para garantir o sucesso do sistema, siga rigorosamente as etapas listadas abaixo:
### Pré-Requisitos:
#### 1. 🔧 **Instalação do Java Development Kit (JDK)**
- Verifique se a versão instalada é **21 ou superior**.
- Comando no terminal para verificar versão:
``` shell
java -version
```

#### 2. 📦 **Instalação e Configuração do Maven**
- Garanta as seguintes configurações no arquivo POM.xml:
``` xml
<dependencies>
    <dependency>
        <groupId>org.jsoup</groupId>
        <artifactId>jsoup</artifactId>
        <version>1.16.1</version>
    </dependency>
</dependencies>
```
## 🧩 Componentes Detalhados do Sistema
### 1. `MainScraping` — Controlador Principal
Responsabilidades:
- Orquestrar todo o fluxo do sistema.
- Controlar interação entre os componentes de scraping, download e compactação.

Detalhe adicional relevante:
- Gestão clara de tratamentos de erro.
- Mensagens de feedback precisas no console.

### 2. `PDFBaixar` — Gerenciador de Downloads e Scraping
Responsabilidades:
- Usa Jsoup para conectar-se e analisar a página HTML especificada.
- Filtra links terminados em `.pdf` contendo "Anexo I" ou "Anexo II".
- Realiza downloads com HTTP padrão, tratando respostas e status adequadamente.

Destaques importantes:
- Utiliza `HttpURLConnection` com tratamento explícito do status HTTP.
- Exibe progresso detalhado do download (`%`) no console.

### 3. `PDFCompactar` — Compactador de Arquivos
Responsabilidades:
- Cria automaticamente diretórios necessários caso não existam.
- Adiciona arquivos existentes ao ZIP final.
- Exibe claramente alertas no caso de arquivos faltantes.

### 4. `Anexo` — Modelo de Dados
Propriedades básicas representando os PDFs encontrados:
- `String nome`: Nome do arquivo PDF.
- `String url`: URL diretamente apontando ao arquivo PDF.

## 📂 Estrutura Completa de Diretórios
A estrutura gerada pelo sistema fica da seguinte forma:
``` plaintext
src/main/
├── java/br/com/intuitivecare/scraping/
│   ├── MainScraping.java
│   ├── PDFBaixar.java
│   ├── PDFCompactar.java
│   └── modelo/
│       └── Anexo.java
└── output/
    ├── anexos/                   # PDFs baixados são armazenados aqui
    └── Anexos.zip                # Resultado final compactado (ZIP)
```
## 🖥️ Exemplo Completo de Saída de Execução
A execução gera logs claros e detalhados no console conforme abaixo:
``` plaintext
[STATUS] Iniciando processo de scraping...
[INFO] Total de PDFs encontrados na página: 5
Download de Anexo_I.pdf: 100%
Arquivo baixado com sucesso: Anexo_I.pdf
Download de Anexo_II.pdf: 100%
Arquivo baixado com sucesso: Anexo_II.pdf
Processo concluído! Arquivo compactado criado em: output/Anexos.zip
```
**Observação:** Em caso de erros serão exibidos alertas detalhados no próprio console informando claramente o problema.
