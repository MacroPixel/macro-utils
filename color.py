from macro_utils.math import *

class Color:

    # Initializes it from a tuple by default
    def __init__( self, color = ( 0, 0, 0 ) ):

        # Colors can be created from 1-4 parameters
        # The base color can either be 1 value used for R, G, and B, or
        # 3 unique values in order
        # The opacity can either be present or absent (defaults to 1)
        try:
            if not ( 1 <= len( color ) <= 4 ):
                raise TypeError( 'Color must have 1, 2, 3, or 4 parameters' )
        except TypeError:
            raise TypeError( 'Color argument must be an iterable' )

        if ( len( color ) >= 3 ):
            self._color = [ i for i in color[ :3 ] ]
        else:
            self._color = [ color[0] for i in range( 3 ) ]

        self._opacity = 1 if ( len( color ) in [ 1, 3 ] ) else color[ len( color ) - 1 ]

        self._clamp()

    # Creates a color from a hex string
    def from_hex( self, hex_, opacity = 1 ):

        self._color = self.hex_to_rgb( hex_ )
        self._opacity = opacity
        self._clamp()

    # Used internally to convert hex string to RGB tuple
    @staticmethod
    def hex_to_rgb( hex_ ):

        return ( int( hex_[ :2 ], 16 ), int( hex_[ 2:4 ], 16 ), int( hex_[ 4:6 ], 16 ) )

    # Used internally to keep color arguments within their bounds
    def _clamp( self ):

        self._color = [ clamp( 0, 255, assert_type( i, int ) ) for i in self._color[ :3 ] ]
        self._opacity = clamp( 0, 1, assert_type( self._opacity, int ) )