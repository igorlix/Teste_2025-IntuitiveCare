from flask import Flask
from flask_cors import CORS
from routes import routes


app = Flask(__name__)
CORS(app)

app.register_blueprint(routes)


@app.route("/")  # Rota para o home
def home():
    return "<h1>Bem-vindo ao servidor Flask!</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)



