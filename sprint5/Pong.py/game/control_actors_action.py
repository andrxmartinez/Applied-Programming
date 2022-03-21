# Description: "This class  controls the different actors in the game. The responsibilit of this class is to translate user input into some kind of intet.


from game import constants
from game.action import Action

class ControlActorsAction(Action):
    """
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """

        direction = self._input_service.get_direction()
        robot = cast["paddle1"][0]
        segments1 = robot.get_all()
        robot2 = cast["paddle2"][0]
        segments2 = robot2.get_all()
       
        if direction.get_player() is "player1":
            for segment in segments1:
                segment.set_velocity(direction)

        elif direction.get_player() is "player2":
            for segment in segments2:
                segment.set_velocity(direction)

        elif direction.get_player() is "":
            for segment in segments1:
                segment.set_velocity(direction)
            for segment in segments2:
                segment.set_velocity(direction)


