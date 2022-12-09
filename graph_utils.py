from graph import Graph
import numpy as np

def summary(graph:Graph)->dict:
    n = len(graph.nodes)
    m = graph.edge_number
    return dict({
        'Numero de Vertices':n,
        'Numero de Arestas':m,
        'Densidade':(2 * m)/(n * (n - 1))
    })

def __make_pretty__(graph:Graph,position,values)->list:
    if position in graph.nodes:
        value = []
        for i in values:
            value.append({
                "Node":i[0].indice,
                "Value":i[1]
            })
        return value
    return []

def successor(graph:Graph,position) -> list:
    return __make_pretty__(graph,position,graph.nodes[position].child)

def predecessor(graph:Graph,position) -> list:
    return __make_pretty__(graph,position,graph.nodes[position].parents)

def floyd_warshall(graph:Graph):
    # gerando matriz de distancia
    size = len(graph.nodes)
    distances = np.ones((size,size))*np.Infinity
    for i in range(size):
        distances[i][i] = 0
    for i in graph.nodes:
        node = graph.nodes[i]
        for j in node.child:
            distances[node.indice][j[0].indice] = j[1]

    #funcao recursiva do algoritmo
    def calculate(distances,k = 0):
        if k == size:
            return distances
            return
        m = np.zeros((size,size))
        for i in range(size):
            m[i][k] = distances[i][k]
            m[k][i] = distances[k][i]
        
        for i in range(size):
            for j in range(size):
                n = distances[i][k]+distances[k][j]
                if n < distances[i][j]:
                    m[i][j] = n
                else:
                    m[i][j] = distances[i][j]
        return calculate(m,k+1)

    #executando o algoritmo
    graph.distances = calculate(distances)

def eccentricity(graph:Graph):
    ecc = {}
    for i in graph.nodes:
        ecc[i] = np.max(graph.distances[i])
    return ecc
        
def __circunference__(graph:Graph,f,signal):
    distance = np.Infinity*signal
    for i in graph.nodes:
        distance = f([distance,np.max(graph.distances[i])])
    return distance

def radius(graph:Graph):
    return __circunference__(graph,np.min,1)

def diameter(graph:Graph):
    return __circunference__(graph,np.max,-1)

def __extremes__(graph:Graph,value):
    nodes = []
    ecc = eccentricity(graph)
    for i in ecc:
        if ecc[i] == value:
            nodes.append(i)
    return nodes

def center(graph:Graph):
    return __extremes__(graph,radius(graph))

def periphery(graph:Graph):
    return __extremes__(graph,diameter(graph))    

def centroid(graph:Graph):
    less = np.Infinity
    size = len(graph.nodes)
    centroid = []
    for i in range(size):
        sum = np.sum(graph.distances[i])
        if sum < less:
            centroid = [i,]
            less = sum
        elif sum == less:
            centroid.append(i)
    return centroid

def outdegree(graph:Graph,position) -> int:
    if position in graph.nodes:
        return len(graph.nodes[position].child)
    return None

def indegree(graph:Graph,position) -> int:
    if position in graph.nodes:
        return len(graph.nodes[position].parents)
    return None

__all__ = [
    'summary',
    'successor',
    'predecessor',
    'floyd_warshall',
    'eccentricity',
    'radius',
    'diameter',
    'center',
    'periphery',
    'centroid',
    'outdegree',
    'indegree'
]