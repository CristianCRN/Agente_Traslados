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
    # Corre Flask en un hilo separado
    threading.Thread(target=lambda: app_flask.run(host='0.0.0.0', port=8080)).start()
    # Corre el bot
    main()