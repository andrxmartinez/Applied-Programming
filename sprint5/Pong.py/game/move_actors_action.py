
# Description: "This class  controls the different actors in the game. The responsibility of this class is to translate user input into some kind of intet.


from game import constants
from game.action import Action
from game.point import Point

class MoveActorsAction(Action):
    """A code template for moving actors. The responsibility of this class of
    objects is move any actor that has a velocity more than zero.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}. """
    
        """for group in cast.values():
            for actor in group:
                    self._move_actor(actor)"""


        ball = cast["ball"][0]
        self._move_actor(ball)

        paddle1 = cast["paddle1"][0]
        segment = paddle1.get_all()
        for group in segment:
            self._move_actor(group)

        paddle2 = cast["paddle2"][0]
        segment = paddle2.get_all()
        for group in segment:
            self._move_actor(group)
        



    def _move_actor(self, actor):
        """Moves the given actor to its next position according to its 
        velocity. Will wrap the position from one side of the screen to the 
        other when it reaches the edge in either direction.
        
        Args:
            actor (Actor): The actor to move.
        """
        position = actor.get_position()
        velocity = actor.get_velocity()
        x1 = position.get_x()
        y1 = position.get_y()
        x2 = velocity.get_x()
        y2 = velocity.get_y()
        x = 1 + (x1 + x2 - 1) % (constants.MAX_X - 1)
        y = 1 + (y1 + y2 - 1) % (constants.MAX_Y - 1)
        position = Point(x, y)
        actor.set_position(position)