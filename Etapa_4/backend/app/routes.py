from flask import Blueprint, request, jsonify
from utils import search_in_dataframe, load_operadoras_data
from flask_cors import cross_origin
import os

routes = Blueprint('routes', __name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

print(f"\n=== VERIFICAÇÃO DE CAMINHOS ===")
print(f"Diretório do script: {BASE_DIR}")
print(f"Caminho dos dados: {DATA_DIR}")
print(f"Conteúdo do diretório: {os.listdir(BASE_DIR)}")
print("==============================\n")

if not os.path.exists(DATA_DIR):
    raise Exception(f"""
    Diretório 'data' não encontrado!
    Caminho esperado: {DATA_DIR}
    Certifique-se que a pasta existe e contém:
    - Relatorio_cadop.csv
    Diretório atual: {os.getcwd()}
    """)

relatorio_cadop_path = os.path.join(DATA_DIR, "Relatorio_cadop.csv")

try:
    if not os.path.exists(relatorio_cadop_path):
        raise FileNotFoundError(f"Arquivo de operadoras não encontrado: {relatorio_cadop_path}")

    relatorio_cadop = load_operadoras_data(relatorio_cadop_path)
    print(f"✅ Operadoras carregadas - {len(relatorio_cadop)} registros")

except Exception as e:
    print(f"❌ Erro crítico ao carregar dados: {str(e)}")
    raise

@routes.route("/api/operadoras", methods=["GET"])
@cross_origin()
def search_operadoras():

    query = request.args.get("q", "").strip().lower()
    cidade = request.args.get("cidade", "").strip().lower()
    uf = request.args.get("uf", "").strip().upper()
    modalidade = request.args.get("modalidade", "").strip()

    if not any([query, cidade, uf, modalidade]):
        return jsonify({
            "success": False,
            "error": "Informe ao menos um critério de busca (nome, cidade, UF ou modalidade)",
            "results": [],
            "count": 0
        }), 400

    try:
        resultados = search_in_dataframe(
            relatorio_cadop,
            query=query,
            cidade=cidade,
            uf=uf,
            modalidade=modalidade,
            search_columns=["Razao_Social", "Nome_Fantasia", "Registro_ANS"]
        )

        return jsonify({
            "success": True,
            "count": len(resultados),
            "results": resultados
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e),
            "results": [],
            "count": 0
        }), 500