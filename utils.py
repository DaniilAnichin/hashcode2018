#!/usr/bin/python
# -*- coding: utf-8 -*- #


def cmp(a: int, b: int) -> int:
    return (a > b) - (a < b)


class Point(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __rsub__(self, other):
        return Point(other.x - self.x, other.y - self.y)

    def __len__(self):
        return self.__abs__()

    def __abs__(self):
        return abs(self.x) + abs(self.y)


class Ride(object):
    def __init__(self, x1, y1, x2, y2, t1, t2):
        self.start = Point(x1, y1)
        self.end = Point(x2, y2)
        self.t1 = t1
        self.t2 = t2

    def __len__(self):
        return self.__abs__()

    def __abs__(self):
        return len(self.end - self.start)


def length(start: Point, end: Point) -> int:
    return abs(end - start)


def ride_length(ride: Ride) -> int:
    return abs(ride.end - ride.start)


def available(start: Point, start_time: int, end: Point, end_time: int):
    return abs(start - end) <= end_time - start_time


def get_current_ride(rides: list, time: int) -> tuple:
    for ride in rides:
        ride_len = len(ride)
        time -= ride_len
        if time < 0:
            return ride
    return rides[-1]


def move_car(position: Point, ride: Ride) -> Point:
    """
    Firstly moving by x, then - y
    """
    if position.x != ride.end.x:
        position -= Point(cmp(position.x, ride.end.x), 0)
    elif position.y != ride.end.y:
        position -= Point(0, cmp(position.y, ride.end.y))
    return position


def get_horosh0(ride: Ride, bonus: int, t: int, pos: Point):
    points = ride_length(ride)
    dfn = length(ride.start, pos)
    if dfn + t + points > ride.t2:
        return 0
    punish = 0
    if dfn + t <= ride.t1:
        points += bonus
        punish = ride.t1 - (dfn + t)
    horosh_val = points / float(points + dfn + punish)
    return horosh_val


def find_closest(rides: list, p: Point, t):
    s_rides = rides.sort(key=lambda ride: -(len(p - ride.start) + (ride.t1 - (len(ride.start - p) + t))
                                            if((ride.t1 - (len(ride.start - p) + t)) > 0) else
                                            0 / (ride.t2 - len(ride) > len(ride.start - p) + t)))
    return s_rides[:20]


def get_horosh1(ride: Ride, rides: list, t, pos: Point):
    cr = find_closest()
    points = ride_length(ride)
    dfn = length(ride.start, pos)
    if dfn + t + points > ride.t2:
        return 0
    punish = 0
    if dfn + t <= ride.t1:
        points += b
        punish = ride.t1 - (dfn + t)
    horosh_val = points / float(points + dfn + punish)

    return horosh_val
