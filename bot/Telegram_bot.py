import io
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from agente.extractor import traslados, validacion_respuesta
from database.operaciones import guardar_traslado
from reportes.generador_excel import generar_reporte
import datetime

def main():
    load_dotenv()
    TOKEN = os.getenv("TELEGRAM_TOKEN")

    async def start(update, context):
        await update.message.reply_text(
            "¡Hola! Soy Richard tu asistente de traslados personal. Cuéntame a donde te diriges."
        )

    async def recibir_texto(update, context):
        texto = update.message.text
        try: 
            if texto.lower().startswith("traslado"):
                datos = traslados(texto)
                datos = validacion_respuesta(datos)
                fecha=datetime.datetime.now()
                guardar_traslado(str(fecha.day).zfill(2), str(fecha.month).zfill(2), str(fecha.year).zfill(2), datos["descripcion"], datos["proyecto"])
                await update.message.reply_text("Traslado Registrado")
            else:
                await update.message.reply_text("Por Favor Repite el traslado e inicia con la palabra Traslado")
        except Exception as e:
            await update.message.reply_text(f"Error: {str(e)}")
                    
    async def reporte(update, context):
        try:
            if not context.args or len(context.args)< 2:
                await update.message.reply_text("Error. Usa el formato: /reporte MM AAAA")
                return  
            mes=context.args[0]
            ano=context.args[1]
            generar_reporte(mes,ano)
            await update.message.reply_document(document=open("Formato Planilla de Transporte.xlsx", "rb"))
        except Exception as e:
            await update.message.reply_text("No se pudo obtener de manera exitosa el reporte")

        
        
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, recibir_texto))
    app.add_handler(CommandHandler("reporte", reporte))
        
    print("Bot corriendo...")
    app.run_polling()
if __name__ == "__main__":
    main()
        