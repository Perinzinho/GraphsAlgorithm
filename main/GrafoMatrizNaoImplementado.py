def criar_grafo():
    matriz = []
    vertices = []
    return matriz, vertices


def inserir_vertice(matriz, vertices, vertice): #Noah
    if vertice in vertices:
        print(f"O vértice '{vertice}' já existe.")
        return matriz, vertices

    vertices.append(vertice)

    # Adiciona uma nova coluna (0) para cada linha existente
    for linha in matriz:
        linha.append(0)

    # Cria a nova linha com zeros
    nova_linha = [0] * len(vertices)
    matriz.append(nova_linha)

    print(f"Vértice '{vertice}' adicionado.")
    return matriz, vertices


def inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=False): #Noah
    if origem not in vertices:
        inserir_vertice(matriz, vertices, origem)
    if destino not in vertices:
        inserir_vertice(matriz, vertices, destino)

    i = vertices.index(origem)
    j = vertices.index(destino)

    matriz[i][j] = 1

    if nao_direcionado:
        matriz[j][i] = 1

    print(f"Aresta adicionada: {origem} -> {destino}")


def remover_vertice(matriz, vertices, vertice): #Leo
    if vertice not in vertices:
        print("Vértice não existe.")
        return matriz, vertices

    idx = vertices.index(vertice)

    # Remove linha
    matriz.pop(idx)
    # Remove coluna
    for linha in matriz:
        linha.pop(idx)

    vertices.remove(vertice)

    print(f"Vértice '{vertice}' removido.")
    return matriz, vertices


def remover_aresta(matriz, vertices, origem, destino, nao_direcionado=False): #Leo
    if origem not in vertices or destino not in vertices:
        print("Um dos vértices não existe.")
        return

    i = vertices.index(origem)
    j = vertices.index(destino)

    matriz[i][j] = 0

    if nao_direcionado:
        matriz[j][i] = 0

    print(f"Aresta removida: {origem} -> {destino}")


def existe_aresta(matriz, vertices, origem, destino): #Gustavo
    if origem not in vertices or destino not in vertices:
        return False

    i = vertices.index(origem)
    j = vertices.index(destino)

    return matriz[i][j] == 1


def vizinhos(matriz, vertices, vertice): #Gustavo
    if vertice not in vertices:
        return []

    i = vertices.index(vertice)
    lista = []

    for j in range(len(vertices)):
        if matriz[i][j] == 1:
            lista.append(vertices[j])

    return lista


def listar_vizinhos(matriz, vertices, vertice): #Joaquim
    if vertice not in vertices:
        print("Vértice não encontrado.")
        return

    print(f"Vizinhos de {vertice}: {vizinhos(matriz, vertices, vertice)}")


def grau_vertices(matriz, vertices): #Joaquim
    print("\n--- GRAU DOS VÉRTICES ---")
    for v in vertices:
        i = vertices.index(v)
        saida = sum(matriz[i])                 # soma da linha
        entrada = sum(linha[i] for linha in matriz)  # soma da coluna
        total = entrada + saida
        print(f"{v}: entrada={entrada}, saída={saida}, total={total}")
    print("-------------------------\n")


def percurso_valido(matriz, vertices, caminho):#Gustavo
    for i in range(len(caminho)-1):
        if not existe_aresta(matriz, vertices, caminho[i], caminho[i+1]):
            return False
    return True


def exibir_grafo(matriz, vertices): #Gustavo
    print("\n   ", "  ".join(vertices))
    for i in range(len(matriz)):
        print(vertices[i], matriz[i])
    print()


def main(): #Noah
    matriz, vertices = criar_grafo()

    while True:
        print("""
--- MENU (Matriz de Adjacência) ---
1 - Exibir Grafo
2 - Inserir Vértice
3 - Inserir Aresta
4 - Remover Vértice
5 - Remover Aresta
6 - Listar Vizinhos
7 - Verificar Aresta
8 - Exibir Grau
9 - Verificar Percurso
0 - Sair
""")
        op = input("Escolha: ")

        if op == "1":
            exibir_grafo(matriz, vertices)

        elif op == "2":
            v = input("Nome do vértice: ")
            inserir_vertice(matriz, vertices, v)

        elif op == "3":
            o = input("Origem: ")
            d = input("Destino: ")
            tipo = input("Não direcionado? (s/n): ")
            inserir_aresta(matriz, vertices, o, d, tipo.lower() == "s")

        elif op == "4":
            v = input("Vértice: ")
            remover_vertice(matriz, vertices, v)

        elif op == "5":
            o = input("Origem: ")
            d = input("Destino: ")
            tipo = input("Não direcionado? (s/n): ")
            remover_aresta(matriz, vertices, o, d, tipo.lower() == "s")

        elif op == "6":
            v = input("Vértice: ")
            listar_vizinhos(matriz, vertices, v)

        elif op == "7":
            o = input("Origem: ")
            d = input("Destino: ")
            print("Existe aresta?", existe_aresta(matriz, vertices, o, d))

        elif op == "8":
            grau_vertices(matriz, vertices)

        elif op == "9":
            caminho = input("Caminho separado por espaço: ").split()
            print("Percurso válido?", percurso_valido(matriz, vertices, caminho))

        elif op == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
