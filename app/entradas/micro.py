import asyncio
import sounddevice as sd


async def escuchar_microfono():
    try:
        fs = 44100
        duration = 5
        print(sd.query_devices())
        # Cambiar este índice según la salida de sd.query_devices()
        mic_index = 2   # índice del micrófono Bluetooth
        print("Grabando desde el micrófono Bluetooth...")
        audio = sd.rec(int(duration * fs),
                    samplerate=fs,
                    channels=1,
                    device=mic_index)
        await asyncio.sleep(duration)
        return audio
    except Exception as e:
        print('Sistema detenido: ', e)
