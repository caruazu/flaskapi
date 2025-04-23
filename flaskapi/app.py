# my_flask_api/app.py
from flask import Flask

# Cria uma instância da aplicação Flask
app = Flask(__name__)

# Define uma rota para a URL raiz ('/')
@app.route('/')
def hello_world():
    """Retorna uma saudação simples."""
    return 'Hello, World!'

# Bloco para rodar o servidor de desenvolvimento diretamente
# (Não recomendado para produção)
if __name__ == '__main__':
    # Roda o app no host local (127.0.0.1) na porta 5000
    # debug=True ativa o modo de depuração (recarrega em alterações, mostra erros detalhados)
    app.run(debug=True, host='0.0.0.0')