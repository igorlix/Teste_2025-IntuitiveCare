import pandas as pd
import os
import zipfile
from .xlsx_utils import ler_xlsx_corretamente
from .data_processing import normalizar_texto


def comparar_dataframes(df_csv, df_xlsx):
    df_csv['chave'] = df_csv.apply(lambda row: '|'.join(row.values.astype(str)), axis=1)
    df_xlsx['chave'] = df_xlsx.apply(lambda row: '|'.join(row.values.astype(str)), axis=1)

    missing_in_csv = df_xlsx[~df_xlsx['chave'].isin(df_csv['chave'])]
    extra_in_csv = df_csv[~df_csv['chave'].isin(df_xlsx['chave'])]

    return missing_in_csv, extra_in_csv


def verificar_resultados(pdf_path):
    base_name = os.path.splitext(pdf_path)[0]
    csv_path = 'procedimentos_saude.csv'
    xlsx_path = f'{base_name}.xlsx'
    zip_path = "Teste_Igor_Lixandrao_Santos.zip"

    if not os.path.exists(xlsx_path):
        raise FileNotFoundError(f"Arquivo XLSX {xlsx_path} não encontrado.")

    if os.path.exists(zip_path):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall()

    df_csv = pd.read_csv(csv_path, sep=';', encoding='utf-8-sig')
    df_xlsx = ler_xlsx_corretamente(xlsx_path)

    df_csv.columns = [normalizar_texto(col) for col in df_csv.columns]
    df_xlsx.columns = [normalizar_texto(col) for col in df_xlsx.columns]

    if set(df_csv.columns) != set(df_xlsx.columns):
        raise ValueError("As colunas não são compatíveis para comparação.")

    df_xlsx = df_xlsx[df_csv.columns]

    missing_in_csv, extra_in_csv = comparar_dataframes(df_csv, df_xlsx)

    with open('relatorio_comparacao.txt', 'w', encoding='utf-8') as f:
        f.write(f"Linhas faltando no CSV: {len(missing_in_csv)}\n")
        f.write(missing_in_csv.head(5).drop(columns=['chave']).to_string() + "\n\n")
        f.write(f"Linhas extras no CSV: {len(extra_in_csv)}\n")
        f.write(extra_in_csv.head(5).drop(columns=['chave']).to_string() + "\n")

    if os.path.exists(csv_path):
        os.remove(csv_path)
