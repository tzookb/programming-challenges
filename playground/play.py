x = 2
y = 2
n = 10
print ([
    [ i, j] for i in range( x + 1) for j in range( y + 1) if ( ( i + j ) != n )
])