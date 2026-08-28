from bot.Telegram_bot import main
from database.modelos import inicializar
import threading
import requests
import time
from flask import Flask

app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "Bot activo"

def correr_flask():
    app_flask.run(host='0.0.0.0', port=8080)

def mantener_activo():
    time.sleep(30)
    while True:
        try:
            requests.get("https://agente-traslados.onrender.com")
        except:
            pass
        time.sleep(600)

if __name__ == "__main__":
    inicializar()
    threading.Thread(target=correr_flask, daemon=True).start()
    threading.Thread(target=mantener_activo, daemon=True).start()
    main()