from graph import Graph
from graph_utils import *

#criando grafo
graph = Graph()

#carregando o grafo de um arquivo de texto
graph.load('nodes.txt')

#criando amtriz de distancia
floyd_warshall(graph)

#mostrando informações sobre o grafo
print("Sumario:\n",summary(graph))
print("Sucessor de 1:\n",successor(graph,1))
print("predecessor:\n",predecessor(graph,1))
print("Grau de saida:\n",outdegree(graph,1))
print("Grau de entrada:\n",indegree(graph,1))
print("Excentricidade:\n",eccentricity(graph))
print("Raio:\n",radius(graph))
print("Diametro:\n",diameter(graph))
print("Centro:\n",center(graph))
print("Centroide:\n",centroid(graph))
print("Periferia:\n",periphery(graph))
