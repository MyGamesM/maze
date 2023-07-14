from .tile_types import tileTypes

class Tile():
    def __init__(self, tile_type: int) -> None:
        self.type = tile_type
        self.dirs = tileTypes[self.type]['options']
        self.sprite = tileTypes[self.type]['sprite']

    def getOptions(self) -> dict:
        return self.dirs

    def getSprite(self) -> str:
        return self.sprite