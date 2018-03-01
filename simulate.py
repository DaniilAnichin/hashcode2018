#!/usr/bin/python
# -*- coding: utf-8 -*- #
# from scoring import score  # flake8: noqa
from utils import get_current_ride, move_car


def draw(car_positions: list) -> None:
    pass


def simulate_cars(car_assignments: list, rides: list, max_time: int) -> None:
    car_positions = [(0, 0) for car_assignments in car_assignments]
    for time in range(max_time):
        for i, (assignments, position) in enumerate(zip(car_assignments, car_positions)):
            ride = get_current_ride([rides[assignment] for assignment in assignments], time)
            car_positions[i] = move_car(position, ride)
        draw(car_positions)
