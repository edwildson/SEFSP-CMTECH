def inverter_diagonais(matriz):
    for linha in matriz:
        # Verifico se o tamanho de cada linha é do tamanho da "altura" da matriz
        if not len(linha) == len(matriz):
            raise ValueError("Esta matriz não é quadrada")

    tamanho = len(matriz)

    for i in range(tamanho // 2):
        # Inverte a diagonal principal usando atribuição múltipla para não utilizar variáveis auxiliares
        matriz[i][i], matriz[tamanho - i - 1][tamanho - i - 1] = matriz[tamanho - i - 1][tamanho - i - 1], matriz[i][i]

    for i in range(tamanho // 2):
        # Inverte a diagonal principal usando atribuição múltipla para não utilizar variáveis auxiliares
        matriz[i][tamanho - i - 1], matriz[tamanho - i - 1][i] = matriz[tamanho - i - 1][i], matriz[i][tamanho - i - 1]

    return matriz

def criar_matriz_quadrada(tamanho):
    matriz = []
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            elemento = int(input(f"Digite o elemento [{i}, {j}]: "))
            linha.append(elemento)
        matriz.append(linha)
        print("")

    return matriz

def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)

def matriz():
    try:
        while True:
            tamanho = int(input("Digite o tamanho da matriz quadrada:\nType 0 to exit\n"))

            if tamanho == 0:
                return
            
            matriz = criar_matriz_quadrada(tamanho)

            print("Matriz antes de inverter as diagonais: ")
            imprimir_matriz(matriz)


            print("Matriz após inverter as diagonais: ")
            imprimir_matriz(inverter_diagonais(matriz))
           
            
    except ValueError:
        print("\nEntrada inválida. Por favor insira apenas números inteiros\n")
        matriz()

if __name__ == "__main__":
    matriz()
