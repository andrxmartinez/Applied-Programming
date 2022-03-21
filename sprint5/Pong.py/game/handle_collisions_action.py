import random
from game import constants
from game.action import Action
from game.point import Point
import sys

# Description: "A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.

class HandleCollisionsAction(Action):
    """
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0] # there's only one
        paddle1 = cast["paddle1"][0]
        segments1 = paddle1.get_all()
        paddle2 = cast["paddle2"][0]
        segments2 = paddle2.get_all()

        
        for count, segments in enumerate(segments1):
            if ball.get_position().equals(segments.get_position()):
                
                self.change_y_direction(ball)
                self.change_x_direction(ball)

        paddle_position = paddle1.get_head().get_position()
        paddle_x = paddle_position.get_x()
        paddle_y = paddle_position.get_y()

        for count, segments in enumerate(segments2):
            if ball.get_position().equals(segments.get_position()):
                
                self.change_y_direction(ball)
                self.change_x_direction(ball)

        paddle_position = paddle2.get_head().get_position()
        paddle_x = paddle_position.get_x()
        paddle_y = paddle_position.get_y()

    
        
        if ball.get_position().get_x() == 1 or ball.get_position().get_x() == constants.MAX_X-1:
            self.change_x_direction(ball)

        if ball.get_position().get_y() == 1 or ball.get_position().get_y() == 19:
            self.change_y_direction(ball)
        
    def change_y_direction(self, ball):
        velocity = ball.get_velocity()
        x = velocity.get_x()
        y = velocity.get_y()
        ball.set_velocity(Point(x, -y))

    def change_x_direction(self, ball):
        velocity = ball.get_velocity()
        x = velocity.get_x()
        y = velocity.get_y()
        ball.set_velocity(Point(-x, y))