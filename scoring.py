#!/usr/bin/python
# -*- coding: utf-8 -*- #
from utils import available, Point


def score(car_assignments: list, rides: list, max_time: int, bonus: int) -> int:
    """
    Calculates the final score for the assignments
    Sample data:
    :param car_assignments: [[0], [2, 1]]
    :param rides: [Ride(0, 0, 1, 3, 2, 9), Ride(1, 2, 1, 0, 0, 9), Ride(2, 0, 2, 2, 0, 9)]
    :param max_time: 10
    :param bonus: 2
    :return: score(6 + 2 + 2)
    """
    # Checking correctness
    if sorted(sum(car_assignments, [])) != list(range(len(rides))):
        raise ValueError('Awful assignments!')

    result = 0
    for assignments in car_assignments:
        local_time = 0
        position = Point(0, 0)
        for assignment in assignments:
            ride = rides[assignment]
            if available(position, local_time, ride.start, ride.t1):
                result += bonus
            ride_len = len(ride)
            local_time = max(ride.t1, local_time + len(ride.start - position))
            position = ride.end
            local_time += ride_len
            if local_time < max_time:
                result += ride_len
            else:
                break

    return result
