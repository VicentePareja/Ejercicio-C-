import random

class Metro:
    def __init__(self, posicion, direccion):
        self.posicion = posicion
        self.direccion = direccion  # 'derecha' o 'izquierda'
        self.pasajeros = []  # Lista de destinos de los pasajeros en el metro

    def avanzar(self, estaciones):
        # Si el metro está en una estación, no avanza este turno.
        if estaciones[self.posicion] == 1:
            return

        # Avanzar de acuerdo a la dirección
        if self.direccion == 'derecha':
            self.posicion += 1
        elif self.direccion == 'izquierda':
            self.posicion -= 1

        # Cambiar la dirección si alcanza el final o el inicio de la línea
        if self.posicion == 0 or self.posicion == len(estaciones) - 1:
            self.cambiar_direccion()

    def cambiar_direccion(self):
        if self.direccion == 'derecha':
            self.direccion = 'izquierda'
        else:
            self.direccion = 'derecha'

    def subir_pasajeros(self, lista_espera):
    # Suben pasajeros que quieren ir en la dirección actual del metro
    # NOTA: Se modifica para usar las estaciones destino de los pasajeros correctamente
        if self.direccion == 'derecha':
            for pasajero in list(lista_espera[self.posicion]):
                if pasajero.estacion_destino > self.posicion:
                    self.pasajeros.append(pasajero.estacion_destino)  # Añade solo la estación destino
                    lista_espera[self.posicion].remove(pasajero)
        else:  # direccion == 'izquierda'
            for pasajero in list(lista_espera[self.posicion]):
                if pasajero.estacion_destino < self.posicion:
                    self.pasajeros.append(pasajero.estacion_destino)  # Añade solo la estación destino
                    lista_espera[self.posicion].remove(pasajero)


    def bajar_pasajeros(self):
        # Bajan los pasajeros cuyo destino es la posición actual del metro
        self.pasajeros = [destino for destino in self.pasajeros if destino != self.posicion]

    def esta_en_estacion(self, estaciones):
        return estaciones[self.posicion] == 1
    
import random

class Pasajero:
    def __init__(self, estacion_actual, destino):
       
        """
        Inicializa un nuevo pasajero.
        - estacion_actual: la estación donde el pasajero está actualmente.
        - estaciones: lista de todas las estaciones en la línea, para elegir un destino.
        """
        self.estacion_actual = estacion_actual
        self.estacion_destino = destino
        self.tiempo_espera = 0  # Tiempo que ha esperado desde que llegó a la estación


    def incrementar_tiempo_espera(self):
        """
        Incrementa el tiempo de espera del pasajero en 1 minuto.
        """
        self.tiempo_espera += 1

def generar_pasajeros(estaciones):
    # Genera una lista de objetos Pasajero con destinos aleatorios (excepto su posición actual)
    nuevos_pasajeros = []
    for i in range(len(estaciones)):
        if estaciones[i] == 1:  # Solo en las estaciones
            for _ in range(random.randint(0, 10)):  # Entre 0 y 10 nuevos pasajeros
                destino = i
                while destino == i:  # Asegurar que el destino sea diferente a la posición actual
                    destino = random.choice([j for j, estacion in enumerate(estaciones) if estacion == 1])
                nuevos_pasajeros.append(Pasajero(i, destino))
    return nuevos_pasajeros

def main(n, estaciones):
    # Inicializar metros
    metros = [
        Metro(0, 'derecha'),
        Metro(16, 'derecha'),
        Metro(32, 'derecha'),
        Metro(16, 'izquierda'),
        Metro(32, 'izquierda'),
        Metro(47, 'izquierda')
    ]

    # Lista para mantener a los pasajeros que esperan en cada estación
    lista_espera = {i: [] for i, estacion in enumerate(estaciones) if estacion == 1}

    # Ejecutar la simulación durante n turnos
    for turno in range(n):
        print(f"\nTurno {turno + 1}/{n}")

        # Imprimir la posición inicial de todos los metros
        for i, metro in enumerate(metros):
            print(f"Metro {i + 1} posición inicial: {metro.posicion}, dirección: {metro.direccion}")

        # Generar y añadir nuevos pasajeros a la lista de espera
        nuevos_pasajeros = generar_pasajeros(estaciones)
        for pasajero in nuevos_pasajeros:
            lista_espera[pasajero.estacion_actual].append(pasajero)

        # Mover los metros y gestionar el embarque y desembarque de pasajeros
        for i, metro in enumerate(metros):
            print(f"Metro {i + 1} en posición {metro.posicion} moviéndose hacia la {metro.direccion}")
            if metro.esta_en_estacion(estaciones):
                print(f"Metro {i + 1} en la estación {metro.posicion} dejando y recogiendo pasajeros")
                metro.bajar_pasajeros()
                print(f"Pasajeros después de bajar en Metro {i + 1}: {len(metro.pasajeros)} en el metro")
                metro.subir_pasajeros(lista_espera)
                print(f"Pasajeros después de subir en Metro {i + 1}: {len(metro.pasajeros)} en el metro")
            else:
                metro.avanzar(estaciones)
                print(f"Metro {i + 1} ahora en posición {metro.posicion}")

        # Imprimir la posición final de todos los metros después de avanzar
        for i, metro in enumerate(metros):
            print(f"Metro {i + 1} posición final: {metro.posicion}, dirección: {metro.direccion}")

# Definir la línea del metro (por ejemplo, la proporcionada en la pregunta)
estaciones = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0,
              0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]

# Ejecutar la función main para una cierta cantidad de turnos, p.ej., 120 (equivale a 2 horas si cada turno es un minuto)
main(120, estaciones)