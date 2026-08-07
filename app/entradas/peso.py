from app.IO_config import Bascula

bascula = Bascula()


async def recibir_peso():
    bascula.leer_bascula()
    return bascula.dato_bascula
