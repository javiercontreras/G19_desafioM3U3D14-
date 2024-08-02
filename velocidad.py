velocidad = [25, 12, 19, 16, 11, 11, 24, 1,
14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

def media(velocidades): 
    promedio = 0
    for i in range(len(velocidades)):
        promedio += velocidad[i]
    promedio = promedio / len(velocidades)
    return promedio

def posiciones_criticas(velocidades, promedio):
    posicion = []
    for i in range(len(velocidades)):
        if velocidades[i] > promedio:
            posicion.append([i,(velocidades[i] - promedio)])
    return posicion

def mostrar_cliente(correas_veloces):
    print(correas_veloces)
    for i in range(len(correas_veloces)):
         print(f"Correar numero #{correas_veloces[i][0] + 1} sobre el promedio en {correas_veloces[i][1]:.2f} m/s")

media_correas = media(velocidad)
correas_veloces = posiciones_criticas(velocidad, media_correas)
mostrar_cliente(correas_veloces)