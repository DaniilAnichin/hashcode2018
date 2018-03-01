#!/usr/bin/python
# -*- coding: utf-8 -*- #
from consts import START, END


def cmp(a: int, b: int) -> int:
    return (a > b) - (a < b)


def length(ride: tuple) -> int:
    a, b = ride[START]
    x, y = ride[END]
    return abs(x - a) + abs(y - b)


def get_current_ride(rides: list, time: int) -> tuple:
    for ride in rides:
        ride_len = length(ride)
        time -= ride_len
        if time < 0:
            return ride
    return rides[-1]


def move_car(position: tuple, ride: tuple) -> tuple:
    """
    Firstly moving by x, then - y
    """
    a, b = position
    x, y = ride[END]
    if a != x:
        a += cmp(a, x)
    elif b != y:
        b += cmp(a, x)
    return a, b
