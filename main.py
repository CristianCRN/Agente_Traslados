from bot.Telegram_bot import main
from database.modelos import inicializar
import asyncio
import threading
from flask import Flask

app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "Bot activo"

def correr_flask():
    app_flask.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
    inicializar()
    # Flask corre en hilo separado
    threading.Thread(target=correr_flask, daemon=True).start()
    # Bot corre en el hilo principal
    main()