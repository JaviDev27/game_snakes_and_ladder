import random


class Escaleras_Serpientes:

    def __init__(self):
        pass

    def generar_tablero(self, numero_jugadores):
        self.jugadores = {} ''' key> value   pepe:3 , javier: 4, luis:100'''

        for i in range(numero_jugadores):  # 4   desde 0 hasta 3
            # ingresde el nombre dle jugador 1 0 hasta 3
            nombre = input('Ingrese nombre del jugador {} :'.format(i+1))
            self.jugadores[nombre] = 0

        self.posiciones_tablero = []
        self.posiciones_escaleras_serpientes = []

        # Genero las escaleras y serpientes
        numero_escaleras = 0
        numero_serpientes = 0
        escaleras_inicio = []  # 3 pero te llega hasta 10
        escaleras_final = []
        serpientes_inicio = []
        serpientes_final = []

        while True:
            posicion_inicial_escalera = random.randint(11, 90)
            posicion_inicial_serpiente = random.randint(11, 99)

            posicion_final_escalera = random.randint(21, 99)
            posicion_final_serpiente = random.randint(2, 90)

            if (posicion_inicial_escalera < posicion_final_escalera) and numero_escaleras < 4:
                if numero_escaleras == 0:
                    escaleras_inicio.append(posicion_inicial_escalera)
                    escaleras_final.append(posicion_final_escalera)
                    numero_escaleras += 1
                elif (posicion_inicial_escalera not in escaleras_inicio) and (posicion_final_escalera not in escaleras_inicio) and (posicion_final_escalera not in serpientes_final) and (posicion_inicial_escalera not in serpientes_final):
                    escaleras_inicio.append(posicion_inicial_escalera)
                    escaleras_final.append(posicion_final_escalera)
                    numero_escaleras += 1

            if (posicion_inicial_serpiente > posicion_final_serpiente) and numero_serpientes < 4:
                if numero_serpientes == 0:
                    serpientes_inicio.append(posicion_inicial_serpiente)
                    serpientes_final.append(posicion_final_serpiente)
                    numero_serpientes += 1
                elif (posicion_inicial_serpiente not in serpientes_inicio) and (posicion_final_serpiente not in serpientes_inicio) and (posicion_final_serpiente not in escaleras_final) and (posicion_inicial_serpiente not in escaleras_inicio):
                    serpientes_inicio.append(posicion_inicial_serpiente)
                    serpientes_final.append(posicion_final_serpiente)
                    numero_serpientes += 1

            if (numero_escaleras == 4) and (numero_serpientes == 4):
                """print('Escaleras')
                print('inicio : ', escaleras_inicio)
                print('final : ', escaleras_final)
                print('serpientes')
                print('inicio : ', serpientes_inicio)
                print('final : ', serpientes_final)"""
                break

        # Genero el tablero de ceros
        for i in range(1, 101):
            # self.posiciones_tablero.append('P{0}'.format(i))
            self.posiciones_tablero.append('--'.format(i))

        for i in range(4):
            self.posiciones_tablero[escaleras_inicio[i]-1] = escaleras_final[i]
            self.posiciones_tablero[serpientes_inicio[i] -
                                    1] = serpientes_final[i]

    def imprimir_tablero(self):
        '''
        1 2 3 4


        ... 100 
        100

        4321

         '''
        for filas in range(9, -1, -1):  # 9 8 7 (inicio, final, el paso )
            for columnas in range(0, 10):
                print('|{}|'.format(
                    self.posiciones_tablero[(filas*10)+columnas]), end='')
            print()
        self.copy_tablero = self.posiciones_tablero.copy()  # hago una copia del tablero

    def lanzar_dado(self):
        return random.randint(1, 6)

    def update_tablero(self, posicion_anterior, posicion_nueva, id_jugador):
        self.posiciones_tablero = self.copy_tablero.copy()
        # Borra la ficha de la posicion anterior
        self.posiciones_tablero[posicion_anterior] = '--'.format(
            id_jugador + 1)

        if posicion_nueva < 100:

            # verifica si no existe escaleras o serpientes
            escalera_serpiente = self.posiciones_tablero[posicion_nueva]

            #print('debug: ', escalera_serpiente)

            if escalera_serpiente == '--':
                self.posiciones_tablero[posicion_nueva] = '*J{}'.format(
                    id_jugador + 1)
            elif 'J' in str(escalera_serpiente):
                self.posiciones_tablero[posicion_nueva] += '-J{}'.format(
                    id_jugador + 1)
            else:
                self.posiciones_tablero[escalera_serpiente - 1] = '*J{}'.format(
                    id_jugador + 1)
                self.jugadores[list(self.jugadores)[id_jugador]
                               ] = escalera_serpiente - 1

        else:
            self.posiciones_tablero[99] = 'J{}'.format(
                id_jugador + 1)
            self.jugadores[list(self.jugadores)[id_jugador]
                           ] = 99

        self.imprimir_tablero()

    def start(self):
        while True:
            try:
                jugadores = int(input('Ingrese el número de jugadores: '))
                break
            except:
                print('!Ingrese valores numéricos por favor')
                continue

        self.generar_tablero(jugadores)

        print('--'*10, 'SE INICIA EL JUEGO', '--'*10)

        if jugadores > 1:
            print('Tienes {} jugadores'.format(jugadores), end='\n\n')
        else:
            print('Un solo jugador', end='\n\n')

        print(list(self.jugadores), end='\n\n')

        self.imprimir_tablero()

        cambio_jugador = 0

        while True:
            print('===========================', end='\n\n')
            key = input('Lanza los dados Jugador-{0} {1}: (Presiona ENTER) ó escribe "salir" para finalizar el juego :'.format(
                (cambio_jugador + 1), list(self.jugadores)[cambio_jugador]))

            # Obtengo la posición anterior
            posicion_anterior = self.jugadores[list(self.jugadores)[
                cambio_jugador]]

            if key == "":
                valor_dado = self.lanzar_dado()
                if valor_dado > 1:
                    print('Avanza {} espacios'.format(valor_dado))
                else:
                    print('Avanza {} espacio'.format(valor_dado))

            elif key == 'salir':
                break

            # Voy actualizando la posicion del jugador en turno
            # obtengo la poscicion actual
            self.jugadores[list(self.jugadores)[cambio_jugador]] += valor_dado

            self.update_tablero(posicion_anterior,
                                self.jugadores[list(self.jugadores)[
                                    cambio_jugador]],
                                cambio_jugador)

            # Imprime las pociciones actuales decada jugador
            for jugador in self.jugadores:
                print('{0} POSICIÓN {1}'.format(
                    jugador, self.jugadores[jugador] + 1))

            # Verifico si ha llegado a la posicion 100 si es verdadero finaliza el juego.
            if self.jugadores[list(self.jugadores)[cambio_jugador]] == 99:
                print('-'*20, 'Ha ganado {}'.format(list(self.jugadores)
                                                    [cambio_jugador]), '-'*10)
                break

            if cambio_jugador < len(self.jugadores) - 1:
                cambio_jugador += 1
            else:
                cambio_jugador = 0


if __name__ == "__main__":
    juego = Escaleras_Serpientes()
    juego.start()  # no afecta

''' ññlñlñl '''
''' 

clase = molde
objeto es 
un carro
atributos 
1. numero llantas
2. color
3. marca
metodos 
hacia delante
hacia atras
frenar


 '''
