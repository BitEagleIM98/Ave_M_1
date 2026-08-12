from app.entradas.peso import recibir_peso
from app.entradas.cam import recibir_cuadro
import sys
from time import sleep
# TODO: definir base de datos y si se usará ORM (SQLite3 o SQLAlchemy) 



async def construir_orden():
    etiqueta = ''
    articulo = ''
    cont_err_cam = 0
    cont_err_pes = 0
    try:
        etiqueta = input('Selecciones tipo de carrito (entrada/salida/merma): ').lower()  # TODO: cambiar por reconocimiento de voz

        while True:
            if etiqueta == "entrada":
                break
            elif etiqueta == "salida":
                break
            elif etiqueta == "merma":
                break
            else:
                etiqueta = input('Carrito no reconocido vuelva a intentar (entrada/salida/merma): ')  # TODO: cambiar por reconocimiento de voz

        while True:
            peso_bascula = await recibir_peso()  # TODO: hcaer reconocimiento de peso
            confirmacion, cuadro_camara = await recibir_cuadro()  # TODO: incorporar resultado de reconocimiento
            # peso_bascula = 1.4  # Debug Only
            # confirmacion, cuadro_camara = True, 0  # Debug Only
            if peso_bascula != 0.0 and confirmacion == True:
                print('Se registra articulo...')

            elif peso_bascula != 0.0 and confirmacion == False:
                while cont_err_cam < 5:
                    print('Error de reconocimiento en camara intentando reconectar')
                    confirmacion, cuadro_camara = False, 0  # Debug Only
                    sleep(1)
                    cont_err_cam += 1
                if confirmacion == True:
                    continue
                else:
                    raise Exception('No fue posible conectar con la cámara') 
      
            elif peso_bascula == 0.0 and confirmacion == True:  # confirmacion es variable temporal, reconocimiento exitoso será la variable de control
                print('No se reconoce el peso, verifique báscula')

            elif peso_bascula == 0.0 and confirmacion == False:  # confirmacion es variable temporal, reconocimiento exitoso será la variable de control
                print('Coloque su artículo sobre la báscula')

            car_fin = input('Desea terminar el carrito? [Y/n]: ').lower()  # TODO: cambiar por reconocimiento de voz (esperar unos segundos, si no hay respuesta se toma como "n")

            if car_fin == 'y':
                conf = input('Confirmación de carrito? [Y/n]: ').lower()  # TODO: cambiar por reconocimiento de voz

                if conf == 'y':
                    print('Los datos se publican con etiqueta de: ', etiqueta)
                    break

                elif conf == 'n':
                    print('Los datos no se publican y se descarta carrito')
                    break

            elif car_fin == 'n':
                continue

    except Exception as ex:
            print("Sistema detenido: ", ex)
            sys.exit()
       