import asyncio
import sounddevice as sd


async def contestar_auriculares(audio):
    try:
        fs = 44100
        duration = 5
        print(sd.query_devices())
        # Cambiar este índice según la salida de sd.query_devices()
        spk_index = 2   # índice de las bocinas Bluetooth
        print("Reproduciendo en las bocinas Bluetooth...")
        sd.play(audio, fs, device=spk_index)
        await asyncio.sleep(duration)
    except Exception as e:
        print('Sistema detenido: ', e)
