"""

    Created on 29-Nov-2022
    Author: Kiril Zelenkovski (@zelenkastiot)

"""
from functools import cache
from datetime import datetime



@cache
def collatz_chain(x):
    if x == 1:
        return 1

    elif x % 2 == 0:
        n = int(x / 2) 

    else:
        n  = x * 3 + 1

    return collatz_chain(n) + 1


if __name__ == "__main__":

    start_time = datetime.now()
    
    print(max(range(1, 1_000_000), key=collatz_chain))
    
    # do your work here
    end_time = datetime.now()
    
    print('Duration: {}'.format(end_time - start_time))