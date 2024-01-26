from disjoint_sets import DisjointSets
from collections import namedtuple
from multipledispatch import dispatch
import random

Edge = namedtuple("Edge", ["from_", "to"])

class Graph:
    def __init__(self, rows, cols, generate=False):
        self.rows = rows
        self.cols = cols
        self.size = self.rows * self.cols
        self.G = [] # graph
        if rows < 0 or cols < 0: raise SystemExit
        if generate: self.generate_edges()

    def generate_edges(self):
        # vertical edges:
        for i in range(self.size - self.cols): # for all cells but in the last row
            self.add_edge(i, i + self.cols)

        # horizontal edges:
        for i in range(self.size - 1): # for all cells but in the last col
            if (i + 1) % self.cols != 0: # no intercolumnar horizontal edges
                self.add_edge(i, i + 1)

    @dispatch(int, int)
    def add_edge(self, from_, to):
        self.G.append(Edge(from_, to))

    @dispatch(Edge)
    def add_edge(self, edge):
        self.G.append(edge)

    def kruskal(self):
        MST = Graph(self.rows, self.cols) # minimal spanning tree
        ds = DisjointSets(self.size)
        random.shuffle(self.G)

        for edge in self.G:
            u = ds.find(edge.from_)
            v = ds.find(edge.to)
            if u != v:
                MST.add_edge(edge)
                ds.join(u, v)

        return MST