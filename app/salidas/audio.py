import asyncio
import sounddevice as sd


async def contestar_auriculares(audio):
    try:
        fs = 44100
        duration = 5
        # print(sd.query_devices())  # Debug Only
        # Cambiar este índice según la salida de sd.query_devices()
        spk_index = 12   # índice de las bocinas Bluetooth
        print("Reproduciendo en las bocinas Bluetooth...")
        sd.play(audio, fs, device=spk_index)
        await asyncio.sleep(duration)
    except Exception as e:
        print('Error de comunicación con auriculares: ', e)
