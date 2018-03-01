
from munkres import Munkres, print_matrix
import sys

# Input:
# ridesByHoroshest -
#          Car 0    Car 1  ....
# Ride 0    a00      a01
# Ride 1    a10      a11
def get_optimal_rideByCar_combo(goodnessByCarByRide):
    cost_matrix = []
    for row in goodnessByCarByRide:
        cost_row = []
        for col in row:
            cost_row += [sys.maxsize - col]
        cost_matrix += [cost_row]


    m = Munkres()
    indexes = m.compute(cost_matrix)
    total = 0
    
#    for row, column in indexes:
#        value = goodnessByCarByRide[row][column]
#        total += value
#        print('(%d, %d) -> %d' % (row, column, value))

    return indexes

