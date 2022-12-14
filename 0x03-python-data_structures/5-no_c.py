#!/usr/bin/python3

def no_c(my_string):
    '''
        function to exclude all 'c' and 'C'
    '''
    x = my_string.copy()
    for i in x:
        if i != 'c' and i != 'C':
            return(x)
