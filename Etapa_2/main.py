import os
import zipfile
from pathlib import Path

def main():
    from utils.pdf_utils import extrair_tabelas_pdf
    from utils.data_processing import processar_dados
    from utils.comparison import verificar_resultados

    BASE_DIR = Path(__file__).parent
    input_dir = BASE_DIR / "input"
    output_dir = BASE_DIR / "output"


    arquivo_pdf = input_dir / "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
    caminho_csv = output_dir / "procedimentos_saude.csv"
    nome_zip = output_dir / "Teste_Igor_Lixandrao_Santos.zip"
    arquivo_xlsx = input_dir / "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.xlsx"

    os.makedirs(output_dir, exist_ok=True)

    dados_extraidos = extrair_tabelas_pdf(arquivo_pdf)
    df = processar_dados(dados_extraidos, manter_abreviacoes=True)
    df.to_csv(caminho_csv, index=False, sep=';', encoding='utf-8-sig')

    with zipfile.ZipFile(nome_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(caminho_csv, arcname=caminho_csv.name)

    verificar_resultados(
        pdf_path=arquivo_pdf,
        csv_path=caminho_csv,
        zip_path=nome_zip,
        input_dir=input_dir,
        output_dir=output_dir,
        xlsx_path=arquivo_xlsx
    )

    # Limpeza
    if caminho_csv.exists():
        caminho_csv.unlink()

if __name__ == "__main__":
    main()