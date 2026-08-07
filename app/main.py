from app.procesamiento.orden import construir_orden


async def main():
    while True:
        construir_orden()