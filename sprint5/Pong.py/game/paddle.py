# Description: an actor of the game. The responsibility of Paddle is to keep track of its appearance, position and velocity.


from game import constants
from game.actor import Actor
from game.point import Point

class Paddle:
    """
        Stereotype:
        Structurer, Information Holder

    Attributes:
        _text (string): The textual representation of the actor.
        _position (Point): The actor's position in 2d space.
        _velocity (Point): The actor's speed and direction. 
        """

    def __init__(self, position: Point(0,0)):
        """The class constructor.   
        Args:
            self (Paddle): An instance of paddle.
        """
        super().__init__()
        self._segments = []
        self._start_position = position
        self._prepare_paddle()
        
        
    def get_all(self):
        """Gets all the paddle's segments.
        
        Args:
            self (Paddle): An instance of paddle.
        Returns:
            list: The paddle's segments.
        """
        return self._segments

    def get_body(self):
        """Gets the paddle's body.
        
        Args:
            self (Paddle: An instance of paddle.
        Returns:
            list: The paddle's body.
        """
        return self._segments[1:]

    def get_head(self):
        """Gets the paddle's head.
        
        Args:
            self (Paddle): An instance of paddle.
        Returns:
            Actor: The paddle's head.
        """
        return self._segments[0]

    def _add_segment(self, text, position, velocity):
        """Adds a new segment to the paddle using the given text, position and velocity.
        Args:
            self (paddle): An instance of paddle.
            text (string): The segment's text.
            position (Point): The segment's position.
            velocity (Point): The segment's velocity.
        """
        segment = Actor()
        segment.set_text(text)
        segment.set_position(position)
        segment.set_velocity(velocity)
        self._segments.append(segment)

    def set_start_position(self,position):

        self._start_position = position


    def _prepare_paddle(self):

        x = self._start_position.get_x()
        y = int(constants.MAX_Y / 2)
        for n in range(constants.PADDLE_LENGTH):
            text = "|"
            position = Point(x, y - n)
            velocity = Point(1, 0)
            self._add_segment(text, position, velocity)
            
    def set_velocity(self, velocity):
        for segment in self._segments:
            segment.set_velocity(velocity)



