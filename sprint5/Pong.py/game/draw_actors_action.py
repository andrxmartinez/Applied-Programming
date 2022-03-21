# Description: "The responsibility of this class is to draw the actions from a particular actor in the game.

from game.action import Action

class DrawActorsAction(Action):

    def __init__(self,output_service):

        self._output_service = output_service

    def execute(self, cast):
        
        self._output_service.clear_screen()
        self._output_service.draw_actor(cast['ball'][0])
        self._output_service.draw_actors(cast['paddle1'][0].get_all())
        self._output_service.draw_actors(cast['paddle2'][0].get_all())

        self._output_service.flush_buffer()