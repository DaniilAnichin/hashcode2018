#!/usr/bin/python
# -*- coding: utf-8 -*- #
from utils import Ride
from shuffle import count_shuffle


if __name__ == '__main__':
    R, C, F, N, B, T = list(map(int, input().split(' ')))

    rides = []
    for i in range(N):
        a, b, x, y, s, f = list(map(int, input().split(' ')))
        ride = Ride(a, b, x, y, s, f)
        rides.append(ride)
    print('That\'s all, folks')
    print(count_shuffle(rides, F, T, B))
