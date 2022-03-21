# Description: "This class  controls the moves of  in the game. The responsibility of this class is to translate user input into some kind of intet.

from game.point import Point

class PlayerMove(Point):

    def __init__ (self, x, y, player):

        super().__init__(x, y)
        self._player = player
    

    def get_player(self):
            return self._player