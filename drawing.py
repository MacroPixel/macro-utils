from .vector import *
from .misc import *
from math import floor
import pygame

# General purpose function for drawing transformed surfaces
def draw_surface( dest, surf, pos, **kwargs ):

    # Check each transformation argument to see if sprite needs to be modified
    if ( 'scale' in kwargs ):
        surf = pygame.transform.scale( surf, V2( surf.get_size() ).mult( kwargs[ 'scale' ] ).list() )
    if ( 'flip' in kwargs ):
        surf = pygame.transform.flip( surf, kwargs[ 'flip' ].x == -1, kwargs[ 'flip' ].y == -1 )
    if ( 'rotation' in kwargs ):
        surf = pygame.transform.rotate( surf, kwargs[ 'rotation' ] )

    # Shift the position based off of the anchor
    anchor = kwargs.get( 'anchor', V2() )
    pos = pos.sub( anchor.mult( surf.get_size() ) )
    dest.blit( surf, pos.list() )

# 'radius_1': Half width of the rectangular part of the arrow (in pixels)
# 'length': Length of the rectangular part of the arrow
# 'radius_2': Half width of the side of the triangular part of the arrow that
# connects to the rectangular part
# Both widths should be half the width of the respective part
# Actual width is ( width * 2 ) + 1 so it has an odd center
# Rotation is in degrees / 90, points down by default
def make_arrow( radius_1, length, radius_2, color, rotation = 0 ):

    width_1 = radius_1 * 2 + 1
    width_2 = radius_2 * 2 + 1

    surf_dims = ( width_2, length + radius_2 + 1 )
    surf = pygame.Surface( surf_dims, pygame.SRCALPHA, 32 )
    surf.fill( ( 0, 0, 0, 0 ) )

    # If you want to figure out where these points are coming from,
    # just draw an arrow in GIMP and do measurements there
    points = (
        ( radius_2 - radius_1, 0 ),
        ( radius_2 - radius_1, length ),
        ( 0, length ),
        ( radius_2, length + radius_2 ),
        ( width_2 - 1, length ),
        ( radius_2 + radius_1, length ),
        ( radius_2 + radius_1, 0 )
    )

    pygame.draw.polygon( surf, color, points )
    surf = pygame.transform.rotate( surf, floor( rotation ) * 90 )
    return surf

# Replaces one color with another within a surface
# Modifies the original instead of returning a value
# (from reddit.com/r/pygame/comments/hprkpr/how_to_change_the_color_of_an_image_in_pygame/)
def replace_surface_color( surf, start_color, end_color ):

    surf_array = pygame.PixelArray( surf )
    surf_array.replace( start_color, end_color )
    del surf_array