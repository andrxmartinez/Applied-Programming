import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.control_actors_action import ControlActorsAction 
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from asciimatics.screen import Screen 
from game.paddle import Paddle

def main(screen):

    # create the cast {key: tag, value: list}
    cast = {}
    
    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y / 2)
    position = Point(x, y)
    velocity = Point(1, -1)

    ball = Actor()
    ball.set_text("@")
    ball.set_position(position)
    ball.set_velocity(velocity)
    cast["ball"] = [ball]

    paddle1 = Paddle(Point(10,0))
    cast["paddle1"] = [paddle1]
    paddle2 = Paddle(Point(70,0))
    cast["paddle2"] = [paddle2]
    

    
    # create the script {key: tag, value: list}
    script = {}

    input_service = InputService(screen)
    output_service = OutputService(screen)
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_acition = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)
    
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_acition]
    script["output"] = [draw_actors_action]

    # start the game
    director = Director(cast, script)
    director.start_game()

Screen.wrapper(main)