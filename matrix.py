def checar_se_matriz_maior_contem_menor(matriz_maior, matriz_menor):
    tamanho_maior = len(matriz_maior)
    tamanho_menor = len(matriz_menor)

    for i in range(tamanho_maior - tamanho_menor + 1): 
        for j in range(tamanho_maior - tamanho_menor + 1):
            # A ideia aqui é percorrer a matriz maior então em `matriz_maior[i:i+tamanho_menor]` a gente está delimitando a altura da matriz para que seja igual a da menor e em `linha[j:j+tamanho_menor]` estamos delimitando o tamanho da linha para que seja igual ao da menor, assim percorremos a matriz fazendo uma varredura do inicio (topo esquerdo para o topo direito) até o final (percorrendo de cima para baixo e da esquerda para direita, similar a uma Maquina De Datilografia)
            submatriz = [linha[j:j+tamanho_menor] for linha in matriz_maior[i:i+tamanho_menor]]

            print(f"\nTentando encontrar submatriz: \n {submatriz}\n")

            if submatriz == matriz_menor:
                return True

    return False

def criar_matriz(qtd_linhas, qtd_colunas):
    matriz = []

    for i in range(qtd_linhas):
        linha = []
        for j in range(qtd_colunas):
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
            qtd_linhas_maior = int(input("\nDigite a quantidade de linhas da matriz maior:\n"))
            qtd_colunas_maior = int(input("Digite a quantidade de colunas da matriz maior:\n"))

            qtd_linhas_menor = int(input("Digite a quantidade de linhas da matriz menor:\n"))
            qtd_colunas_menor = int(input("Digite a quantidade de colunas da matriz menor:\n"))

            if 0 in [qtd_linhas_maior, qtd_colunas_maior, qtd_linhas_menor, qtd_colunas_menor]:
                print("Insira um tamanho válido para as matrizes")
            
            matriz_maior = criar_matriz(qtd_linhas_maior, qtd_colunas_maior)
            matriz_menor = criar_matriz(qtd_linhas_menor, qtd_colunas_menor)

            print("Matriz maior: ")
            imprimir_matriz(matriz_maior)

            print("Matriz menor: ")
            imprimir_matriz(matriz_menor)

            print("Checando se Matriz maior contém a Matriz menor: \n")
            encontrou = checar_se_matriz_maior_contem_menor(matriz_maior, matriz_menor)

            if encontrou:
                print("\nA matriz maior contém a matriz menor!")
                if input("Para sair digite sair, para continuar tecle enter\n") == "sair":
                    return
                continue

            print("A matriz maior não contém a matriz menor!\n")

            if input("Para sair digite sair, para continuar tecle enter\n") == "sair":
                return

    except ValueError:
        print("\nEntrada inválida. Por favor, insira apenas números inteiros\n")
        matriz()

if __name__ == "__main__":
    matriz()
