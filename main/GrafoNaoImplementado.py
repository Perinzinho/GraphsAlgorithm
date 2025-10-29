def criar_grafo():
    graph = [()]
    return graph
    """
    Retorna um novo grafo vazio.
    Passos:
    1. Criar um dicionário vazio: {}
    2. Retornar o dicionário (representa o grafo)
    """
    pass


def inserir_vertice(grafo, vertice):
    """
    Insere um vértice no grafo, sem arestas iniciais.
    Passos:
    1. Verificar se 'vertice' já é chave em grafo.
    2. Se não for, criar entrada grafo[vertice] = []
    3. Se já existir, não fazer nada (ou avisar)
    """ 
    pass


def inserir_aresta(grafo, origem, destino, nao_direcionado=False):
    """
    Adiciona aresta entre origem e destino.
    Passos:
    1. Garantir que 'origem' e 'destino' existam no grafo (inserir se necessário).
    2. adicionar destino como vizinho de origem (append).
    3. Se for Nâo Direcionado, também:
         - adicionar origem como vizinho de destino
    """
    pass

def vizinhos(grafo, vertice): # Noah
    if vertice in grafo:
        return grafo[vertice]
    else:
        print(f"Vértice '{vertice}' não encontrado no grafo.")
        return []


def listar_vizinhos(grafo, vertice): # Noah
    if vertice not in grafo:
        print(f"O vértice '{vertice}' não existe no grafo.")
        return None

    vizinhos = grafo[vertice]

    if not vizinhos:
        print(f"O vértice '{vertice}' não possui vizinhos.")
    else:
        print(f"Vizinhos de '{vertice}': {vizinhos}")

    return vizinhos

def exibir_grafo(grafo): # Noah
    if not grafo:
        print("O grafo está vazio.")
        return

    for vertice in sorted(grafo.keys()):
        vizinhos = grafo[vertice]
        print(f"{vertice} -> {vizinhos if vizinhos else '∅'}")

def remover_aresta(grafo, origem, destino, nao_direcionado=False):
    """
    Remove a aresta entre origem e destino.
    Passos:
    1. Verificar se 'origem' existe; se não, terminar.
    2. Se destino estiver em grafo[origem], remover essa ocorrência.
    3. Se for não direcionado, também:
         - verificar se 'destino' existe e remover 'origem' de grafo[destino] se presente.
    """
    pass


def remover_vertice(grafo, vertice, nao_direcionado=True):
    """
    Remove um vértice e todas as arestas que o tocam.
    Passos:
    1. Verificar se 'vertice' existe em grafo; se não, terminar.
    2. Para cada outro vertice no grafo:
         - se 'vertice' estiver na lista de vizinhos, remover essa aresta.
    3. Remover o vertice do grafo
    4. Opcional: retornar confirmação/erro.
    """
    pass


def existe_aresta(grafo, origem, destino):
    """
    Verifica se existe aresta direta origem -> destino.
    Passos:
    1. Verificar se 'origem' é chave no grafo.
    2. Retornar True se 'destino' estiver em grafo[origem], caso contrário False.
    """
    pass

def grau_vertices(grafo):
    """
    Calcula e retorna o grau (out, in, total) de cada vértice.
    Passos:
    1. Inicializar um dict de graus vazia
    2. Para cada vertice, colocar no dict uma estrutura com in, out e total zerado
    3. Para cada u em grafo:
         - out_degree[u] = tamanho de vizinhos
         - para cada v em grafo:
            - verificar se u está na lista de vizinho de v,
            - caso esteja, adicionar +1 para o grau de entrada de u
    4. Calcular o grau total somando entrada + saida
    5. Retornar uma estrutura contendo out,in,total por vértice (ex: dict de tuplas).
    """
    pass


def percurso_valido(grafo, caminho):
    """
    Verifica se uma sequência específica de vértices (caminho) é válida:
    i.e., se existem arestas consecutivas entre os nós do caminho.
    Passos:
    1. Se caminho tiver tamanho < 2, retornar True (trivial).
    2. Para i de 0 até len(caminho)-2:
         - origem = caminho[i], destino = caminho[i+1]
         - se não existe_aresta(grafo, origem, destino): retornar False
    3. Se todas as arestas existirem, retornar True.
    """
    pass



def main():
    """
    Crie um menu onde seja possível escolher qual ação deseja realizar
    ex:
        1 - Mostrar o Grafo
        2 - inserir vertice
        3 - inserir aresta
        4 - remover vértice.
        ....
    """
    pass


if __name__ == "__main__":
    main()
