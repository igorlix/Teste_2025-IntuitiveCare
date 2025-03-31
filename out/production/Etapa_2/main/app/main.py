import os
import zipfile
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent.parent))  # Ajuste conforme necessário


from pdf_utils import extrair_tabelas_pdf
from data_processing import processar_dados
from comparison import verificar_resultados


def main():
    arquivo_pdf = 'Etapa_2/src/main/input/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'
    caminho_csv = 'Etapa_2/src/main/input/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.csv'
    nome_zip = "Teste_Igor_Lixandrao_Santos.zip"

    dados_extraidos = extrair_tabelas_pdf(arquivo_pdf)
    df = processar_dados(dados_extraidos, manter_abreviacoes=True)

    df.to_csv(caminho_csv, index=False, sep=';', encoding='utf-8-sig')

    with zipfile.ZipFile(nome_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(caminho_csv)

    verificar_resultados(arquivo_pdf)

    if os.path.exists(caminho_csv):
        os.remove(caminho_csv)


if __name__ == "__main__":
    main()
