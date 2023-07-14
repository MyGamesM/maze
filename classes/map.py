from .tile import Tile
from .tile_types import tileTypes
from .tile_generator import TileGenerator

class Map():
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.tg = TileGenerator()

        self.map = [[Tile(4) for _ in range(width)] for _ in range(height)]
        self.setTile(0, 0, Tile(1))

    def getTile(self, x: int, y: int) -> Tile:
        return self.map[y][x]

    def setTile(self, x: int, y: int, tile: Tile) -> None:
        self.map[y][x] = tile

    def generateMap(self) -> None:
        for y, row in enumerate(self.map):
            for x, tile in enumerate(row):
                if tile == None: continue

                if y == 0:
                    if x == 0: continue
                    self.setTile(x, y, self.tg.GenerateTileEdge(tile, self.getTile(x - 1, y).getOptions()['left']))
                else:
                    if x == 0:
                        self.setTile(x, y, self.tg.GenerateTileEdge(tile, self.getTile(x, y - 1).getOptions()['down']))
                    else:
                        self.setTile(x, y, self.tg.GenerateTileMiddle(tile, self.getTile(x - 1, y).getOptions()['left'], self.getTile(x, y - 1).getOptions()['down']))

    def print_map(self) -> None:
        out = []

        out.append("+" + ("-+-+" * self.width))

        for i in range(self.height):
            for k in range(3):
                x = "|"
                for j in range(self.width):
                    x += self.getTile(j, i).getSprite()[k] + "|"
                
                out.append(x)
            out.append("+" + ("-+-+" * self.width))


        for i in range(len(out)):
            print(out[i])