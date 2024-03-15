
# Makes sure a value is an integer or float
def assert_numeric( value ):

    if ( not is_numeric( value ) ):
        raise RuntimeError( f'Type mismatch: { type( value ) } is not an int or float' )

# Checks numbers for a range and a datatype
# Leave type_ as None to allow int and float
def assert_range( value, min_, max_, type_ = None ):

    if ( type_ is not None ):
        assert_type( value, type_ )
    if not ( ( min_ is None or value >= min_ ) and ( max_ is None or value <= max_ ) ):
        raise RuntimeError( f'Range error: Value { value } should be in range [{ min_ }, { max_ }]' )

# Makes sure a value is of a given datatype
def assert_type( value, type_ ):

    if ( not isinstance( value, type_ ) ):
        raise RuntimeError( f'Type mismatch: { type( value ) } != { type_ }' )
    return value

# Places a value in a list if not in one already
def ensure_in_list( value ):

    if ( isinstance( value, list ) ):
        return value
    return [ value ]

# Similar to assert_numeric, but returns a boolean rather
# than raising an error
def is_numeric( value ):
    
    return ( isinstance( value, int ) or isinstance( value, float ) )

# Indexes a list, wrapping around if out of bounds
def wrap_index( list_, index ):

    return list_[ index % len( list_ ) ]