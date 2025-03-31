import pdfplumber

def extrair_tabelas_pdf(pdf_path):
    print("Extraindo tabelas do PDF...")
    todas_tabelas = []

    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            tabela = page.extract_table()
            if tabela:
                print(f"Tabela encontrada na página {i+1} com {len(tabela)} linhas")
                todas_tabelas.extend(tabela)

    if not todas_tabelas:
        raise ValueError("Nenhuma tabela encontrada no PDF")

    return todas_tabelas