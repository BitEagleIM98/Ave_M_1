import vosk
import json
import os
import numpy as np
from scipy.signal import resample
from app.procesamiento.filtro_voz import bandpass_filter
from dotenv import load_dotenv
load_dotenv()
# TODO: Implementar una forma de instalar vosk ya sea crear todo el venv completo o una fomra con sudo apt
fs = 44100
VOSK_MODEL = os.getenv("VOSK_MODEL")
print(VOSK_MODEL)



async def reconocimiento_audio(audio):
    audio_filtrado = bandpass_filter(audio, fs)
    # Normalizar
    audio = audio / np.max(np.abs(audio))
    # Resamplear a 16 kHz
    fs_target = 16000
    num_samples = int(len(audio) * fs_target / fs)
    audio_resampled = resample(audio, num_samples)
    # Convertir a bytes
    audio_bytes = audio_resampled.astype(np.int16).tobytes()
    model = vosk.Model(VOSK_MODEL)
    rec = vosk.KaldiRecognizer(model, fs_target)
    # Pasar audio en chunks
    step = 4000
    for i in range(0, len(audio_bytes), step):
        rec.AcceptWaveform(audio_bytes[i:i+step])
    
    result = rec.FinalResult()

    # Mostrar texto reconocido
    print("Reconocido:", json.loads(result)["text"])
    return json.loads(result)["text"], audio
