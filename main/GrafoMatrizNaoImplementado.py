from numba.cuda.printimpl import print_item


def criar_grafo():
    matriz = [()]
    vertice = [()]
    return matriz, vertice
pass


def inserir_vertice(matriz, vertices, vertice):
    if vertice in vertices:
        print(f"O vertice {vertice} ja existe no grafo.")
        return matriz, vertices

    vertices.append(vertice)

    for linha in matriz:
        linha.append(0)

    nova_linha = [0] * len(vertices)
    matriz.append(nova_linha)
    print(f"vertice {vertice} adicionado")
    return matriz, vertices

    """
    Adiciona um novo vértice ao grafo.

    Passos:
    1. Verificar se o vértice já existe em 'vertices'.
    2. Caso não exista:
        - Adicionar o vértice à lista 'vertices'.
        - Aumentar o tamanho da matriz:
            a) Para cada linha existente, adicionar um valor 0 no final (nova coluna).
            b) Adicionar uma nova linha com zeros do tamanho atualizado.
    """
    pass


def inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    """
    Adiciona uma aresta entre dois vértices.

    Passos:
    1. Garantir que 'origem' e 'destino' existam em 'vertices':
        - Se não existirem, chamar 'inserir_vertice' para adicioná-los.
    2. Localizar o índice da origem (i) e do destino (j).
    3. Marcar a conexão na matriz: matriz[i][j] = 1.
    4. Se nao_direcionado=True, também marcar a conexão inversa matriz[j][i] = 1.
    """
    pass


def remover_vertice(matriz, vertices, vertice):
    """
    Remove um vértice e todas as arestas associadas.

    Passos:
    1. Verificar se o vértice existe em 'vertices'.
    2. Caso exista:
        - Descobrir o índice correspondente (usando vertices.index(vertice)).
        - Remover a linha da matriz na posição desse índice.
        - Remover a coluna (mesmo índice) de todas as outras linhas.
        - Remover o vértice da lista 'vertices'.
    """
    pass

def remover_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    """
    Remove uma aresta entre dois vértices.

    Passos:
    1. Verificar se ambos os vértices existem.
    2. Localizar os índices (i e j).
    3. Remover a aresta: matriz[i][j] = 0.
    4. Se nao_direcionado=True, também remover a inversa: matriz[j][i] = 0.
    """
    pass


def existe_aresta(matriz, vertices, origem, destino):
    """
    Verifica se existe uma aresta direta entre dois vértices.

    Passos:
    1. Verificar se ambos os vértices existem em 'vertices'.
    2. Obter os índices (i, j).
    3. Retornar True se matriz[i][j] == 1, caso contrário False.
    """
    pass


def vizinhos(matriz, vertices, vertice):
    """
    Retorna a lista de vizinhos (vértices alcançáveis a partir de 'vertice').

    Passos:
    1. Verificar se 'vertice' existe em 'vertices'.
    2. Obter o índice 'i' correspondente.
    3. Criar uma lista de vizinhos vazia
    4. Para cada item da linha matriz[i], verificar se == 1
        - Adicionar o vértice correspondente na lista de vizinhos
    5. Retornar essa lista.
    """
    pass


def grau_vertices(matriz, vertices):
    """
    Calcula o grau de entrada, saída e total de cada vértice.

    Passos:
    1. Criar um dicionário vazio 'graus'.
    2. Para cada vértice i:
        - Se o grafo for direcionado:
            - Grau de saída: somar os valores da linha i.
            - Grau de entrada: somar os valores da coluna i.
            - Grau total = entrada + saída.
        - Se não:
            - calcular apenas o grau de saida ou entrada
    3. Armazenar no dicionário no formato:
        graus[vértice] = {"saida": x, "entrada": y, "total": z} ou graus[vértice] = x.
    4. Retornar 'graus'.
    """
    pass


def percurso_valido(matriz, vertices, caminho):
    """
    Verifica se um percurso (sequência de vértices) é possível no grafo.

    Passos:
    1. Percorrer a lista 'caminho' de forma sequencial (de 0 até len-2).
    2. Para cada par consecutivo (u, v):
        - Verificar se existe_aresta(matriz, vertices, u, v) é True.
        - Se alguma não existir, retornar False.
    3. Se todas existirem, retornar True.
    """
    pass


def listar_vizinhos(matriz, vertices, vertice):
    """
    Exibe (ou retorna) os vizinhos de um vértice.

    Passos:
    1. Verificar se o vértice existe.
    2. Chamar a função vizinhos() para obter a lista.
    3. Exibir a lista formatada (ex: print(f"Vizinhos de {v}: {lista}")).
    """
    pass


def exibir_grafo(matriz, vertices):
    """
    Exibe o grafo em formato de matriz de adjacência.

    Passos:
    1. Exibir cabeçalho com o nome dos vértices.
    2. Para cada linha i:
        - Mostrar o nome do vértice.
        - Mostrar os valores da linha (0 ou 1) separados por espaço.
    """
    pass


def main():

    pass


if __name__ == "__main__":
    main()
