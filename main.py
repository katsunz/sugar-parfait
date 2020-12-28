#!/bin/env python3

"""
An attempt at implementing FIPS202 in Python 3.

This will stick as close as possible to the relevant style guides but
no promises made...
"""

def string_to_state(bit_string, state):
    """Convert string to state array as in 3.1.2 of FIPS202"""

    pointer = 0
    for y in range(5):
        for x in range(5):
            for z in range(64):
                print(x, y, z)
                state[x][y][z] = test_string[pointer]
                pointer += 1
    
    return state

if __name__ == "__main__":
    state_a = [[[0 for h in range(64)] for i in range(5)] for j in range(5)]

    test_string = [q for q in range(1600)]
    state_a = string_to_state(test_string, state_a)            
    print("A[4,2,63] is " + str(state_a[4][2][63]))
    print("A[0,1,2] is " + str(state_a[0][1][2]))
