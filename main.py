import os
from classes.map import Map
from time import sleep

os.system('clear')

class App():
    def __init__(self) -> None:
        self.map = Map(8, 4)

        self.input = int(input("1: Single\n2: Loop\n$ "))

        if self.input == 1:
            os.system('clear')
            self.map.generateMap()
            self.map.print_map()
            
        elif self.input == 2:
            self.time = float(input("Loop delay: "))
            while True:
                os.system('clear')
                self.map.generateMap()
                self.map.print_map()
                sleep(self.time)

if __name__ == "__main__":
    app = App()