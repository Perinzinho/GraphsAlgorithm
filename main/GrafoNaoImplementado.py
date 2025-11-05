def criar_grafo():  # Perin
    """Retorna um novo grafo vazio."""
    graph = {}
    return graph


def inserir_vertice(grafo, vertice):  # Perin
    """Insere um vértice no grafo, sem arestas iniciais."""
    if vertice in grafo:
        print("Vértice já existe.")
        return
    grafo[vertice] = []
    print(f"Vértice '{vertice}' inserido com sucesso!")


def inserir_aresta(grafo, origem, destino, nao_direcionado=False):  # Perin
    """Adiciona uma aresta entre origem e destino."""
    if origem not in grafo:
        grafo[origem] = []
    if destino not in grafo:
        grafo[destino] = []

    if destino not in grafo[origem]:
        grafo[origem].append(destino)

    if nao_direcionado and origem not in grafo[destino]:
        grafo[destino].append(origem)

    print(f"Aresta de '{origem}' para '{destino}' inserida com sucesso!")
    if nao_direcionado:
        print("(Aresta não-direcionada adicionada nos dois sentidos)")


def vizinhos(grafo, vertice):  # Noah
    if vertice in grafo:
        return grafo[vertice]
    else:
        print(f"Vértice '{vertice}' não encontrado no grafo.")
        return []


def listar_vizinhos(grafo, vertice):  # Noah
    if vertice not in grafo:
        print(f"O vértice '{vertice}' não existe no grafo.")
        return None

    viz = grafo[vertice]
    if not viz:
        print(f"O vértice '{vertice}' não possui vizinhos.")
    else:
        print(f"Vizinhos de '{vertice}': {viz}")

    return viz


def exibir_grafo(grafo):  # Noah
    if not grafo:
        print("O grafo está vazio.")
        return

    print("\n=== Estrutura do Grafo ===")
    for vertice in sorted(grafo.keys()):
        viz = grafo[vertice]
        print(f"{vertice} -> {viz if viz else '∅'}")
    print("==========================\n")


def remover_aresta(grafo, origem, destino, nao_direcionado=False):  # Gustavo
    if origem not in grafo:
        print(f"Origem '{origem}' não existe no grafo.")
        return

    if destino in grafo[origem]:
        grafo[origem].remove(destino)
        print(f"Aresta de '{origem}' para '{destino}' removida.")
    else:
        print(f"Não existe aresta de '{origem}' para '{destino}'.")

    if nao_direcionado and destino in grafo and origem in grafo[destino]:
        grafo[destino].remove(origem)
        print("(Aresta não-direcionada removida nos dois sentidos)")


def remover_vertice(grafo, vertice):  # Gustavo
    if vertice not in grafo:
        print(f"Vértice '{vertice}' não existe no grafo.")
        return

    for v in grafo:
        if vertice in grafo[v]:
            grafo[v].remove(vertice)
    del grafo[vertice]

    print(f"Vértice '{vertice}' removido com sucesso.")


def existe_aresta(grafo, origem, destino):  # Gustavo
    if origem not in grafo:
        return False
    return destino in grafo[origem]


def grau_vertices(grafo):  # Completo
    graus = {}

    for v in grafo:
        graus[v] = {"in": 0, "out": len(grafo[v]), "total": 0}

    for u in grafo:
        for v in grafo[u]:
            if v in graus:
                graus[v]["in"] += 1

    for v in graus:
        graus[v]["total"] = graus[v]["in"] + graus[v]["out"]

    print("\n=== Grau dos vértices ===")
    for v, g in graus.items():
        print(f"{v}: entrada={g['in']} | saída={g['out']} | total={g['total']}")
    print("==========================\n")

    return graus


def percurso_valido(grafo, caminho):  # Completo
    if len(caminho) < 2:
        return True

    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i + 1]
        if not existe_aresta(grafo, origem, destino):
            print(f"Percurso inválido: não existe aresta de '{origem}' para '{destino}'.")
            return False

    print("Percurso válido!")
    return True


def main():  # Perin
    grafo = {}
    while True:
        print("\n===== MENU =====")
        print("1 - Criar Grafo")
        print("2 - Inserir vértice")
        print("3 - Inserir aresta")
        print("4 - Remover vértice")
        print("5 - Remover aresta")
        print("6 - Vizinhos")
        print("7 - Listar vizinhos")
        print("8 - Existe aresta")
        print("9 - Grau dos vértices")
        print("10 - Exibir grafo")
        print("11 - Percurso válido")
        print("0 - Sair")

        try:
            opt = int(input("Selecione uma ação: "))
        except ValueError:
            print("Opção inválida, digite um número.")
            continue

        match opt:
            case 1:
                grafo = criar_grafo()
                print("Grafo criado com sucesso.")
            case 2:
                vertice = input("Digite o nome do vértice: ")
                inserir_vertice(grafo, vertice)
            case 3:
                origem = input("Origem: ")
                destino = input("Destino: ")
                nd = input("Não-direcionado? (s/n): ").lower() == 's'
                inserir_aresta(grafo, origem, destino, nd)
            case 4:
                vertice = input("Digite o vértice a remover: ")
                remover_vertice(grafo, vertice)
            case 5:
                origem = input("Origem: ")
                destino = input("Destino: ")
                nd = input("Não-direcionado? (s/n): ").lower() == 's'
                remover_aresta(grafo, origem, destino, nd)
            case 6:
                vertice = input("Digite o vértice: ")
                print("Vizinhos:", vizinhos(grafo, vertice))
            case 7:
                vertice = input("Digite o vértice: ")
                listar_vizinhos(grafo, vertice)
            case 8:
                origem = input("Origem: ")
                destino = input("Destino: ")
                print("Existe aresta?", existe_aresta(grafo, origem, destino))
            case 9:
                grau_vertices(grafo)
            case 10:
                exibir_grafo(grafo)
            case 11:
                caminho = input("Digite o caminho (ex: A,B,C): ").split(',')
                percurso_valido(grafo, caminho)
            case 0:
                print("Encerrando programa...")
                break
            case _:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
