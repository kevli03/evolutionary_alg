# genetic algorithm for optimizing performance of a robot picking up trash

import random
import copy

size = 10
runs = 100

class Robot:
    def __init__(self):
        self.moves = {
            '000':'pick up trash',
            '001':'move right',
            '010':'move left',
            '011':'move up',
            '100':'move down',
            '101':'do nothing',
            '111':'do nothing'
        }
        self.place = [0,0]
        self.generation = 0
        self.alg = ''          # '000001010...'
        self.collected = 0
        self.fitness = 0       # (self.collected ** 2) / len(self.alg)

class Board:
    def __init__(self, size):
        self.tiles = [['0'] * size for x in range(size)]

        area = size * size
        trash = random.sample(range(area), k=size)

        for r in range(size):
            for c in range(size):
                place = (r * size) + c
                if place in trash:
                    self.tiles[r][c] = '1'

def compare_fitness(best_robots, robot):
    fitnesses = [best_robots[0].fitness, best_robots[1].fitness]
    curr_min = min(fitnesses)
    if robot.fitness > curr_min:
        index_min = fitnesses.index(curr_min)
        del best_robots[index_min]
        best_robots.append(robot)
    return

def collect(robot, board):
    return

def recombinator(s1, s2, size):
    """
    receives the 2 "strongest" algorithms and produces daughter algs through recombination
    recombination strategies: (double) crossing over, point mutation, insertion, deletion,
        duplication, inversion, translocation
    daughter algs: 2 orig, 12 mutated single crossing, 6 mutated double crossing (20 total)
    """

    recomb_probs = {
        'point mutation':size ** 2,
        'insertion':size ** 3,
        'deletion':size ** 3,
        'duplication':size ** 4,
        'inversion':size ** 4,
        'translocation':size ** 5,
    }

    algs = []       # list of 20 daughter algorithms

    return algs

def main():
    master_board = Board(size)
    best_robots = [Robot(), Robot()]

    for i in range(size ** 2):      # initial run
        board = copy.deepcopy(master_board)
        robot = Robot()

        compare_fitness(best_robots, robot)

    return