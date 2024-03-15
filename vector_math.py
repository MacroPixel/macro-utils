from .vector import *

# Returns whether a value is within a rectangle
# Requries vectors
def contains_point( start, size, point ):

    return ( point.vec_fn( lambda a, b: 0 if a < b else 1, start ) == V2( 1 ) and
        point.vec_fn( lambda a, b: 0 if a > b else 1, start.add( size ) ) == V2( 1 ) )

# Calculates the overlap between two rectangle positions
# Assumes pos_a and pos_b lie at the top-left of the rectangles
# The first position is the position the resultant vector should
# be applied to
# Returns None if there is no overlap
def get_overlap( pos_a, size_a, pos_b, size_b, epsilon = 0 ):

    pos_a = pos_a.add( size_a.div( 2 ) )
    pos_b = pos_b.add( size_b.div( 2 ) )

    distance = pos_a.sub( pos_b ).fn( lambda a: abs( a ) )
    min_distance = size_a.add( size_b ).div( 2 )
    overlap = min_distance.sub( distance )

    if ( overlap.x <= epsilon or overlap.y <= epsilon ):
        return None

    # The shift direction depends on the center of the first box
    # relative to the center of the second
    if ( pos_a.x < pos_b.x ):
        overlap.x *= -1
    if ( pos_a.y < pos_b.y ):
        overlap.y *= -1

    # print( pos_a, size_a, pos_b, size_b, overlap )

    return overlap

def vclamp( vec, min_vec, max_vec ):

    return V2( min( max( vec.x, min_vec.x ), max_vec.x ), min( max( vec.y, min_vec.y ), max_vec.y ) )

def vmin( v1, v2 ):

    return V2( min( v1.x, v2.x ), min( v1.y, v2.y ) )

def vmax( v1, v2 ):

    return V2( max( v1.x, v2.x ), max( v1.y, v2.y ) )