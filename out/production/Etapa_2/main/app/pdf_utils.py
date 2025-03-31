import pdfplumber


def extrair_tabelas_pdf(pdf_path):
    todas_tabelas = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tabela = page.extract_table()
            if tabela:
                todas_tabelas.extend(tabela)
    if not todas_tabelas:
        raise ValueError("Nenhuma tabela encontrada no PDF")
    return todas_tabelas
