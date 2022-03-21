# Description: "Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.


import sys
from game.point import Point
from game.player_move import PlayerMove
from asciimatics.event import KeyboardEvent


class InputService:
    """
    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
        _keys (list): Points for up, dn, lt, rt.
    """

    def __init__(self, screen):
        """The class constructor."""
        self._screen = screen
        self._keys = {}
        self._keys[ord("w")] = PlayerMove(0, -3,"player1") # w
        self._keys[ord("s")] = PlayerMove(0, 3, "player1") # s
        self._keys[ord("i")] = PlayerMove(0, -3, "player2") # i
        self._keys[ord("j")] = PlayerMove(0, 3, "player2") # j

    def get_direction(self):
        """Gets the selected direction for the given player.

        Returns:
            Point: The selected direction.
        """
        direction = PlayerMove(0, 0, "")
        event = self._screen.get_event()
        if isinstance(event, KeyboardEvent):
            if event.key_code == 27 or event.key_code == -1:
                sys.exit()
            direction = self._keys.get(event.key_code, PlayerMove(0, 0, ""))
        return direction