from .tile import Tile
from random import choice

class TileGenerator():
    def __init__(self) -> None:
        pass

    def GenerateTileEdge(self, tile: Tile, *args) -> Tile:
        args = args[0]
        return Tile(choice(args) if len(args) > 0 else 4)

    def GenerateTileMiddle(self, tile: Tile, *args) -> Tile:
        if len(args[1]) == 4: args = args[0]
        else: args = args[0] + args[1]
        args = list(dict.fromkeys(args))
        return Tile(choice(args) if len(args) > 0 else 4)