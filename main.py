from instagrapi import Client
from flask import Flask
import os

app = Flask(__name__)

# Configurar cliente do Instagram
cl = Client()

# Carregar credenciais do ambiente
INSTA_USERNAME = os.environ.get("suporte.hypegram")
INSTA_PASSWORD = os.environ.get("53974123Vxpro@")
SESSIONID = os.environ.get("SESSIONID")  # Opcional (evita login direto)

@app.route('/')
def home():
    try:
        if SESSIONID:
            cl.load_settings("session.json")  # Carrega sessão se existir
            cl.login_by_sessionid(SESSIONID)
        else:
            cl.login(INSTA_USERNAME, INSTA_PASSWORD)
            cl.dump_settings("session.json")  # Salva sessão

        user_info = cl.user_info_by_username("instagram")
        return {"user": user_info.dict()}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)