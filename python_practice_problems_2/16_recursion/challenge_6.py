#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 15:08:57 2023

@author: johnmorgan
"""

import graph as g

def topo_recurse(myGraph, result):
    if len(result) == myGraph.vertices:
        return result
    edges_in = [0] * myGraph.vertices
    for index in range(myGraph.vertices):
        for later_task in myGraph.graph[index]:
            edges_in[later_task] += 1
    zero_in = None
    for index in range(len(edges_in) - 1, -1, -1):
        if zero_in == None and edges_in[index] == 0 and index not in result:
            zero_in = index
    if zero_in == None:
        return "Not a DAG!"
    else:
        result.append(zero_in)
        myGraph.graph[zero_in] = []
        return topo_recurse(myGraph, result)
    
def topologicalSort(myGraph):
    result = []
    return topo_recurse(myGraph, result)

# Course solution

def helperFunction(myGraph, currentNode, visited, result) :
  visited[currentNode] = True
  for i in myGraph.graph[currentNode] :
    if visited[i] == False :
      helperFunction(myGraph, i, visited, result)
  result.insert(0, currentNode)

def topologicalSort(myGraph) :
  visited = [False] * myGraph.vertices
  result = []
  for currentNode in range(myGraph.vertices) :
    if visited[currentNode] == False :
      helperFunction(myGraph, currentNode, visited, result)
  return(result)

graph = g.Graph(5)
graph.addEdge(0, 1)
graph.addEdge(0, 3)
graph.addEdge(1, 2)
graph.addEdge(2, 3)
graph.addEdge(2, 4)
graph.addEdge(3, 4)
print(topologicalSort(graph))

graph = g.Graph(6)
graph.addEdge(5, 2)
graph.addEdge(5, 0)
graph.addEdge(4, 0)
graph.addEdge(4, 1)
graph.addEdge(2, 3)
graph.addEdge(3, 1)
print(topologicalSort(graph))