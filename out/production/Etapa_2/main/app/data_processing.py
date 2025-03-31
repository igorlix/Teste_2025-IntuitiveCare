import pandas as pd
import unicodedata


def normalizar_texto(texto):
    if pd.isna(texto) or texto is None:
        return None
    texto = str(texto)
    texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')
    texto = ' '.join(texto.split()).strip()
    return texto


def processar_dados(tabela, manter_abreviacoes=False):
    df = pd.DataFrame(tabela[1:], columns=tabela[0])
    df = df.dropna(how='all').dropna(axis=1, how='all')

    for col in df.columns:
        df[col] = df[col].apply(normalizar_texto)

    abreviacoes = {
        "OD": "Seg. Odontológica",
        "AMB": "Seg. Ambulatorial",
        "HCO": "Hospitalar Com Obstetrícia",
        "HSO": "Hospitalar Sem Obstetrícia",
        "REF": "Plano Referência",
        "PAC": "Procedimento de Alta Complexidade",
        "DUT": "Diretriz de Utilização"
    }

    if not manter_abreviacoes:
        for col in df.columns:
            df[col] = df[col].apply(lambda x: abreviacoes.get(str(x).strip(), x) if pd.notna(x) else x)

    df = df.fillna('None')

    return df
