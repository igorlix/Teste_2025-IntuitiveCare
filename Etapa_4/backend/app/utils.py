import pandas as pd
import os

def load_operadoras_data(file_path):
    print(f"\nCarregando operadoras de: {file_path}")

    try:
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

        df = pd.read_csv(
            file_path,
            sep=";",
            encoding='utf-8',
            dtype={
                'Registro_ANS': str,
                'DDD': str,
                'Telefone': str,
                'CEP': str,
                'CNPJ': str
            }
        )

        colunas_obrigatorias = [
            'Registro_ANS', 'Razao_Social', 'Nome_Fantasia',
            'Cidade', 'UF', 'Modalidade'
        ]
        for col in colunas_obrigatorias:
            if col not in df.columns:
                raise ValueError(f"Coluna obrigatória '{col}' não encontrada no arquivo")

        df = df.dropna(subset=['Razao_Social'])
        df['UF'] = df['UF'].str.upper().str.strip()
        df['Cidade'] = df['Cidade'].str.lower().str.strip()
        df['Modalidade'] = df['Modalidade'].str.strip()
        return df.fillna('')

    except Exception as e:
        raise Exception(f"Falha ao carregar {file_path}: {str(e)}")


def search_in_dataframe(df, query, cidade, uf, modalidade, search_columns):
    try:
        mask = pd.Series(True, index=df.index)
        if query:
            query = str(query).lower().strip()
            if len(query) >= 3:
                query_mask = pd.Series(False, index=df.index)
                for col in search_columns:
                    if col in df.columns:
                        query_mask |= df[col].astype(str).str.lower().str.contains(query, na=False)
                mask &= query_mask

        if cidade:
            cidade = str(cidade).lower().strip()
            mask &= df['Cidade'].astype(str).str.lower().str.contains(cidade, na=False)

        if uf:
            uf = str(uf).upper().strip()
            mask &= df['UF'].astype(str).str.upper() == uf

        if modalidade:
            modalidade = str(modalidade).strip()
            mask &= df['Modalidade'].astype(str).str.strip() == modalidade

        resultados = df[mask].copy()

        for col in ['CNPJ', 'Telefone', 'Fax', 'CEP']:
            if col in resultados.columns:
                resultados[col] = resultados[col].astype(str)

        return resultados.to_dict(orient='records')

    except Exception as e:
        print(f"Erro na busca: {str(e)}")
        return []