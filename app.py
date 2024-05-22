from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Hello Zucc"

@app.route('/bug')
def bad():
    try:
        raise TypeError()
    except TypeError as e:
        print(e)
    except TypeError as e:
        print("Duplicado, ou seja, nunca vai entrar aqui.")