import random
# Tamano del tablero
N = 6
# Crear el tablero del jugador
tablero_jugador = []
for fila in range(N):
    tablero_jugador.append(["~"] * N)

# Crear el tablero de la maquina
tablero_maquina = []

for fila in range(N):
    tablero_maquina.append(["~"] * N)

# Mostrar el tablero del jugador
for fila in tablero_jugador:
    print(fila)

def mostrar_tablero(tablero):
    print("  0 1 2 3 4 5")

    for i in range(N):
        print(i, end=" ")

        for j in range(N):
            print(tablero[i][j], end=" ")

        print()
        
mostrar_tablero(tablero_jugador);

#colocar los barcos
def colocar_barco(tablero, tamano):
    colocado = False

    while not colocado:
        fila = random.randint(0, N - 1)
        columna = random.randint(0, N - 1)

        direccion = random.choice(["H", "V"])

        if direccion == "H":
            if columna + tamano <= N:
                libre = True

                for j in range(columna, columna + tamano):
                    if tablero[fila][j] != "~":
                        libre = False

                if libre:
                    for j in range(columna, columna + tamano):
                        tablero[fila][j] = "B"

                    colocado = True

        else:
            if fila + tamano <= N:
                libre = True

                for i in range(fila, fila + tamano):
                    if tablero[i][columna] != "~":
                        libre = False

                if libre:
                    for i in range(fila, fila + tamano):
                        tablero[i][columna] = "B"

                    colocado = True
barcos = [1, 1, 2, 2, 3, 4]
for tamano in barcos:
    colocar_barco(tablero_jugador, tamano)

for tamano in barcos:
    colocar_barco(tablero_maquina, tamano)
print("Tablero del jugador:")
mostrar_tablero(tablero_jugador)

print("Tablero de la maquina:")
mostrar_tablero(tablero_maquina)