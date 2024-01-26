class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.rank = 0

class DisjointSets:
    def __init__(self, size):
        self.tab = [Node(i) for i in range(size)]
        
    def join(self, x, y):
        x_root, y_root = self.find(x), self.find(y)

        if (self.tab[x_root].rank > self.tab[y_root].rank):
            self.tab[y_root].parent = x_root
        elif (self.tab[x_root].rank < self.tab[y_root].rank):
            self.tab[x_root].parent = y_root
            

    def find(self, x):
        if (self.tab[x].parent == None): return x
        
        self.tab[x].parent = self.find(self.tab[x].parent)
        return self.tab[x].parent