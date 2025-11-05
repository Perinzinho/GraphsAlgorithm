def criar_grafo():
    vertices = []
    arestas = []
    return vertices, arestas


def inserir_vertice(vertices, vertice):
    if vertice not in vertices:
        vertices.append(vertice)
        print(f"Vértice '{vertice}' adicionado.")
    else:
        print(f"O vértice '{vertice}' já existe.")


def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
    if origem not in vertices:
        inserir_vertice(vertices, origem)
    if destino not in vertices:
        inserir_vertice(vertices, destino)

    if [origem, destino] not in arestas:
        arestas.append([origem, destino])

    if nao_direcionado and [destino, origem] not in arestas:
        arestas.append([destino, origem])

    print(f"Aresta '{origem} -> {destino}' adicionada.")


def remover_aresta(arestas, origem, destino, nao_direcionado=False):
    if [origem, destino] in arestas:
        arestas.remove([origem, destino])

    if nao_direcionado and [destino, origem] in arestas:
        arestas.remove([destino, origem])

    print(f"Aresta '{origem} -> {destino}' removida.")


def remover_vertice(vertices, arestas, vertice):
    if vertice not in vertices:
        print("Vértice não encontrado.")
        return

    vertices.remove(vertice)

    arestas[:] = [a for a in arestas if a[0] != vertice and a[1] != vertice]

    print(f"Vértice '{vertice}' e suas arestas foram removidos.")


def existe_aresta(arestas, origem, destino):
    return [origem, destino] in arestas


def vizinhos(vertices, arestas, vertice):
    if vertice not in vertices:
        return []

    lista = []
    for (o, d) in arestas:
        if o == vertice:
            lista.append(d)
    return lista


def listar_vizinhos(vertices, arestas, vertice):
    v = vizinhos(vertices, arestas, vertice)
    print(f"Vizinhos de {vertice}: {v}")


def grau_vertices(vertices, arestas):
    print("\n--- GRAU DOS VÉRTICES ---")
    for v in vertices:
        entrada = sum(1 for (o, d) in arestas if d == v)
        saida = sum(1 for (o, d) in arestas if o == v)
        total = entrada + saida
        print(f"{v}: entrada={entrada}, saída={saida}, total={total}")
    print("-------------------------\n")


def percurso_valido(arestas, caminho):
    for i in range(len(caminho) - 1):
        if not existe_aresta(arestas, caminho[i], caminho[i+1]):
            return False
    return True


def exibir_grafo(vertices, arestas):
    print("\nVértices:", vertices)
    print("Arestas:")
    for origem, destino in arestas:
        print(f"{origem} -> {destino}")
    print()


def main():
    vertices, arestas = criar_grafo()

    while True:
        print("""
--- MENU (Lista de Arestas) ---
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
            exibir_grafo(vertices, arestas)

        elif op == "2":
            v = input("Nome do vértice: ")
            inserir_vertice(vertices, v)

        elif op == "3":
            o = input("Origem: ")
            d = input("Destino: ")
            tipo = input("Não direcionado? (s/n): ")
            inserir_aresta(vertices, arestas, o, d, tipo.lower() == "s")

        elif op == "4":
            v = input("Vértice: ")
            remover_vertice(vertices, arestas, v)

        elif op == "5":
            o = input("Origem: ")
            d = input("Destino: ")
            tipo = input("Não direcionado? (s/n): ")
            remover_aresta(arestas, o, d, tipo.lower() == "s")

        elif op == "6":
            v = input("Vértice: ")
            listar_vizinhos(vertices, arestas, v)

        elif op == "7":
            o = input("Origem: ")
            d = input("Destino: ")
            print("Existe aresta?", existe_aresta(arestas, o, d))

        elif op == "8":
            grau_vertices(vertices, arestas)

        elif op == "9":
            caminho = input("Caminho (separado por espaço): ").split()
            print("Percurso válido?", percurso_valido(arestas, caminho))

        elif op == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()