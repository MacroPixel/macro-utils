
# Returns -1, 0, or 1 depending on a value's sign
def sign( value ):

    if ( value < 0 ):
        return -1
    if ( value > 0 ):
        return 1
    return 0

# Linearly interpolates between two values
# Unlike most lerp functions, this also allows a 'd' parameter
# that allows you to only perform a lerp to a certain extent
# This is mostly useful when you want to make a lerp calculation
# consistent with a 'delta_time' variable
def lerp( a, b, x, d = 1 ):

    return ( b + ( a - b ) * ( ( 1 - x ) ** d ) )

# Returns a value between 'min' and 'max'
def clamp( value, min_, max_ ):

    return max( min( value, max_ ), min_ )