from app.IO_config import Camara

camara = Camara()


async def recibir_cuadro():
    camara.ver_camara()
    cuadro = camara.frame
    status = camara.ret
    return status, cuadro
