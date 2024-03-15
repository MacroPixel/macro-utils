# Compact vector class
# Doesn't actually work like standard linear-algebra vectors
# Instead, it provides an easy way to run an operation on both
# X and Y (using either 1 or 2 numbers)

# Since each vector operation returns a copy of itself,
# operations can easily be chained
class V2:

    def __init__( self, a = None, b = None ):

        if ( isinstance( a, V2 ) ):
            self.set( a.x, a.y )
        elif ( type( a ) == list or type( a ) == tuple ):
            self.set( a[0], a[1] )
        elif ( a is None and b is None ):
            self.set( 0, 0 )
        elif ( b is None ):
            self.set( a, a )
        else:
            self.set( a, b )

    # These two functions help to reduce repetitive code within the operation functions
    def _operation( self, current, value, op, *, vec_fn ):

        if ( op == '+' ):
            return current + value
        elif ( op == '-' ):
            return current - value
        elif ( op == '*' ):
            return current * value
        elif ( op == '/' ):
            return current / value
        elif ( op == 'fn' ):
            return value( current )
        elif ( op == 'vec_fn' ):
            return vec_fn( current, value )

    def _resolve_operation( self, a, b, op, *, vec_fn = None ):

        if ( isinstance( a, V2 ) ):
            return V2( self._operation( self.x, a.x, op, vec_fn = vec_fn ), self._operation( self.y, a.y, op, vec_fn = vec_fn ) )
        elif ( type( a ) == list or type( a ) == tuple ):
            return V2( self._operation( self.x, a[0], op, vec_fn = vec_fn ), self._operation( self.y, a[1], op, vec_fn = vec_fn ) )
        else:
            return V2( self._operation( self.x, a, op, vec_fn = vec_fn ), self._operation( self.y, a if b is None else b, op, vec_fn = vec_fn ) )

    # Update
    def set( self, a = 0, b = 0 ):

        self.x = a
        self.y = b
        return self

    # Add
    def add( self, a, b = None ):
        return self._resolve_operation( a, b, '+' )

    # Subtract
    def sub( self, a, b = None ):
        return self._resolve_operation( a, b, '-' )

    # Multiply
    def mult( self, a, b = None ):
        return self._resolve_operation( a, b, '*' )

    # Divide
    def div( self, a, b = None ):
        return self._resolve_operation( a, b, '/' )

    # Custom function
    def fn( self, a, b = None ):
        return self._resolve_operation( a, b, 'fn' )

    # Custom function on another vector
    def vec_fn( self, fn, a, b = None ):
        return self._resolve_operation( a, b, 'vec_fn', vec_fn = fn )
        
    # Return a list
    def list( self ):
        return [ self.x, self.y ]

    # Return a copy
    def copy( self ):
        return V2( self.x, self.y )

    # Return a string
    def __str__( self ):
        return f'({ self.x }, { self.y })'

    def __repr__( self ):
        return f'[{ self.x }, { self.y }]'

    # Allows using as key in dictionary
    # Simply hashes a tuple representation of the vector
    def __hash__( self ):
        return hash( ( self.x, self.y ) )

    # Compares two vectors
    def __eq__( self, other ):
        if isinstance( other, V2 ):
            return self.x == other.x and self.y == other.y
        return False

    # Creates a vector from a string
    @staticmethod
    def int_from_string( string ):

        x, y = string[ 1:-1 ].split( ', ' )
        return V2( int( x ), int( y ) )

    @staticmethod
    def float_from_string( string ):

        x, y = string[ 1:-1 ].split( ', ' )
        return V2( float( x ), float( y ) )