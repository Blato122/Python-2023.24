import numpy as np
from PIL import Image
import pickle

CELL_W = 20
WALL_W = 5

class Maze:
    def __init__(self, MST):
        self.horizontal = []
        self.vertical = []
        self.MST = MST

    def draw(self):
        maze_img = np.zeros((self.MST.rows * (WALL_W + CELL_W) + WALL_W,
                self.MST.cols * (WALL_W + CELL_W) + WALL_W), dtype=np.uint8)

        for edge in self.MST.G:
            # convert from cell indices to x, y coords
            from_x, from_y = edge.from_ % self.MST.cols, edge.from_ // self.MST.cols
            to_x, to_y = edge.to % self.MST.cols, edge.to // self.MST.cols

            min_x = min(from_x, to_x) * (WALL_W + CELL_W) + WALL_W
            max_x = max(from_x, to_x) * (WALL_W + CELL_W) + WALL_W
            min_y = min(from_y, to_y) * (WALL_W + CELL_W) + WALL_W
            max_y = max(from_y, to_y) * (WALL_W + CELL_W) + WALL_W

            maze_img[min_x : max_x + CELL_W, min_y : max_y + CELL_W] = 255

        self.maze_img = maze_img

    def show(self):
        img = Image.fromarray(self.maze_img)
        img.show()
        img.save(input("Save as: ")) # include extension! e.g. png
        pickle.dump(self.MST, open("save.p", "wb"))
        