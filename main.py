from bot.Telegram_bot import main
from database.modelos import inicializar
import threading
from flask import Flask

app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "Bot activo"

if __name__ == "__main__":
    inicializar()
    threading.Thread(target=main, daemon=True).start()
    app_flask.run(host='0.0.0.0', port=8080)