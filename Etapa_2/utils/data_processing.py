import pandas as pd
import unicodedata

def normalizar_texto(texto):
    if pd.isna(texto) or texto is None:
        return None
    texto = str(texto)
    texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')
    return ' '.join(texto.split()).strip()

def processar_dados(tabela, manter_abreviacoes=False):
    print("Processando dados...")

    df = pd.DataFrame(tabela[1:], columns=tabela[0])
    df = df.dropna(how='all').dropna(axis=1, how='all')

    for col in df.columns:
        df[col] = df[col].apply(normalizar_texto)

    if not manter_abreviacoes:
        abreviacoes = {
            "OD": "Seg. Odontológica",
            "AMB": "Seg. Ambulatorial",
        }
        for col in df.columns:
            df[col] = df[col].apply(lambda x: abreviacoes.get(str(x).strip(), x))

    return df.fillna('None')