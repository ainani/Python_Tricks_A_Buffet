#!/usr/bin/python

def print_vector(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))

if __name__ == "__main__":
    print_vector(1,0,1)
    
    tuple_vector=(1,0,1)
    print tuple_vector
    
    list_vector=[1,0,1]
    print list_vector
    
    print "\n Without Unpacking, passing arguments one by one"
    print_vector(tuple_vector[0],
          tuple_vector[1],
          tuple_vector[2])

    print "\nSingle * in Tuple"
    print_vector(*tuple_vector)
    
    print "\nSingle * in List"
    print_vector(*list_vector)
    
    print "\nGenerator Expression:"
    genexpr = (x * x for x in range(3))
    print_vector(*genexpr)

    dict_vector = {'y': 0, 'z': 1, 'x': 1}
    print "\nDouble ** in Dictionary:"
    print_vector(**dict_vector)
    
    print "\nSingle * in dict will returns keys:"
    print_vector(*dict_vector)
