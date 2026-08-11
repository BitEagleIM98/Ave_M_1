# TODO: hacer implementación de reconocimiento de imagen
import cv2
import numpy as np
import tflite_runtime.interpreter as tflite

interpreter = tflite.Interpreter(model_path="mobilenet_ssd.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


async def reconocer_objeto(frame):
    # Preprocesar imagen
    img = cv2.resize(frame, (300, 300))
    input_data = np.expand_dims(img, axis=0).astype(np.uint8)
    # Ejecutar inferencia
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    # Resultados
    boxes = interpreter.get_tensor(output_details[0]['index'])[0]
    classes = interpreter.get_tensor(output_details[1]['index'])[0]
    scores = interpreter.get_tensor(output_details[2]['index'])[0]
