# coding: utf8
# created by victor p - 12/12/2018

class DuplicatedActiveStationException(Exception):
    """ More than one active routes for a line. """
    def __init__(self, *args, **kwargs): # real signature unknown
        super().__init__('Error: The same location is already present in the route')
