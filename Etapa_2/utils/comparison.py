
import pandas as pd
from datetime import datetime
from .xlsx_utils import ler_xlsx_corretamente
from .data_processing import normalizar_texto

def normalizar_valores(valor):

    if pd.isna(valor) or valor in [None, 'None', 'NaN', 'nan', '']:
        return None

    # Normalização de datas
    if isinstance(valor, (datetime, pd.Timestamp)):
        return valor.strftime('%Y-%m-%d')
    try:

        dt = datetime.strptime(str(valor), '%d/%m/%Y')
        return dt.strftime('%Y-%m-%d')
    except (ValueError, TypeError):
        pass

    try:
        num = float(valor)
        if num.is_integer():
            return str(int(num))
        return str(num)
    except (ValueError, TypeError):
        pass

    return str(valor).strip().upper()

def normalizar_dataframe(df):
    return df.apply(lambda col: col.map(normalizar_valores))

def comparar_dataframes(df_csv, df_xlsx):

    df_csv_norm = normalizar_dataframe(df_csv)
    df_xlsx_norm = normalizar_dataframe(df_xlsx)

    df_csv_norm['chave'] = df_csv_norm.apply(
        lambda row: '|'.join(row.values.astype(str)), axis=1)
    df_xlsx_norm['chave'] = df_xlsx_norm.apply(
        lambda row: '|'.join(row.values.astype(str)), axis=1)

    missing_in_csv = df_xlsx[~df_xlsx_norm['chave'].isin(df_csv_norm['chave'])]
    extra_in_csv = df_csv[~df_csv_norm['chave'].isin(df_xlsx_norm['chave'])]

    return missing_in_csv, extra_in_csv

def analisar_diferencas(missing, extra):

    analise = {
        'total_missing': len(missing),
        'total_extra': len(extra),
        'problemas_identificados': [],
        'diferencas_por_coluna': {}
    }


    if len(missing) > 0:
        exemplo = missing.iloc[0]
        analise['exemplo_diferenca'] = exemplo.to_dict()

    return analise

def verificar_resultados(pdf_path, csv_path, zip_path, input_dir, output_dir, xlsx_path):

    df_csv = pd.read_csv(csv_path, sep=';', encoding='utf-8-sig')
    df_xlsx = ler_xlsx_corretamente(xlsx_path)

    df_csv.columns = [normalizar_texto(col) for col in df_csv.columns]
    df_xlsx.columns = [normalizar_texto(col) for col in df_xlsx.columns]

    df_xlsx = df_xlsx[df_csv.columns]

    missing, extra = comparar_dataframes(df_csv, df_xlsx)
    analise = analisar_diferencas(missing, extra)

    with open(output_dir / "relatorio_comparacao_final.txt", 'w', encoding='utf-8') as f:
        f.write("RELATÓRIO DE COMPARAÇÃO FINAL\n")
        f.write("="*50 + "\n\n")

        # Resumo
        f.write(f"Total de linhas no CSV: {len(df_csv)}\n")
        f.write(f"Total de linhas no XLSX: {len(df_xlsx)}\n")
        f.write(f"Diferenças reais encontradas: {len(missing)}\n\n")

        # Detalhes das correções aplicadas
        f.write("CORREÇÕES APLICADAS:\n")
        f.write("- Normalização de valores nulos (None/NaN/nan)\n")
        f.write("- Padronização de formatos de data\n")
        f.write("- Uniformização de números decimais (.0 removido para inteiros)\n")
        f.write("- Normalização de strings (trim e uppercase)\n\n")

        # Exemplos
        if len(missing) > 0:
            f.write("PRINCIPAIS DIFERENÇAS RESTANTES:\n")
            f.write(missing.head(5).to_string() + "\n\n")

        f.write("CONCLUSÃO:\n")
        if len(missing) == 0 and len(extra) == 0:
            f.write("✅ Os arquivos são idênticos após normalização\n")
        else:
            f.write(f"⚠️ Existem {len(missing)} diferenças reais após normalização\n")