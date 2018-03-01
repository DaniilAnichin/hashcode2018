#!/usr/bin/python
# -*- coding: utf-8 -*- #
from random import shuffle, randint
from scoring import score


def chunk_shuffle(ride_number: int, car_number: int) -> list:
    chunks = [[] for i in range(car_number)]
    shuffled = list(range(ride_number))
    shuffle(shuffled)
    for i in shuffled:
        chunks[randint(0, car_number - 1)].append(i)
    return chunks


def count_shuffle(rides: list, car_number: int, final_time: int, bonus: int, iterations: int=100) -> tuple:
    best_score = 0
    best_result = None
    for i in range(iterations):
        car_assignments = chunk_shuffle(len(rides), car_number)
        local_score = score(car_assignments, rides, final_time, bonus)
        if local_score > best_score:
            best_result = car_assignments
            best_score = local_score
    return best_score, best_result
