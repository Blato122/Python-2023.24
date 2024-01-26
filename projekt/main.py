from graph import Graph
from maze import Maze
import pickle

ROWS, COLS = 12, 12

load = False

if load:
    MST = pickle.load(open("save.p", "rb"))
else:
    MST = Graph(ROWS, COLS, generate=True).kruskal()

maze = Maze(MST)
maze.draw()
maze.show()
