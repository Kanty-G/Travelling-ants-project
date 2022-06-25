# Kanty Louange, Gakima, 20184109
# Jonathan, Metila, Matricule

import numpy as np
import random as rand

#c to remove : la classe colony est pr toutes les fourmies ("ants")
class Colony:
    class Ant:
        def __init__(self, colony):
            self.colony = colony
            #c to remove: self.pos = position actuelle de ant
            self.pos = rand.randrange(self.colony.n)

            self.mem = np.zeros(self.colony.n)
            
            #c to remove: self.mem is probably le niveau de phéromones
            self.mem[self.pos] = 1
            #c to remove: self.path is the path que ant a empreinté pour se rendre à pos
            self.path = [self.pos]
            #c to remove: self.cost = cost of the path from initial position
            self.cost = 0

        def reset(self, colony):
            self.__init__(colony)

        def __str__(self):
            return self.path + ', cost : ' + self.cost

        def __lt__(self, other):
            #TO DO
            pass

        # Returns city to be travelled to from current position
        def policy(self):
            if rand.random() < self.colony.q_0:
                # Deterministic decision
                print("remove errors")
                # TODO
            else:
                print("remove errors")
                # Stochastic decision
                # TODO

        # Updates the local pheromones and position of ant
        # while keeping track of total cost and path
        def move(self):
            destination = self.policy()

            # local updating
            # TODO

            # Change position
            # TODO


        # Updates the pheromone levels of ALL edges that form 
        # the minimum cost loop at each iteration
        def globalUpdate(self):
            # TODO

            print(self)

    def __init__(self, adjMat, m=10, beta=2, alpha=0.1, q_0=0.9):
        # Parameters: 
        # m => Number of ants
        # beta => Importance of heuristic function vs pheromone trail
        # alpha => Updating propensity
        # q_0 => Probability of making a non-stochastic decision
        # tau_0 => Initial pheromone level

        self.adjMat = adjMat
        self.n = len(adjMat)

        self.tau_0 = 1 / (self.n * self.nearestNeighborHeuristic())
        self.tau = [[self.tau_0 for _ in range(self.n)] for _ in range(self.n)]
        self.ants = [self.Ant(self) for _ in range(self.m)]

        self.beta = beta
        self.alpha = 0.1
        self.q_0 =q_0

    def __str__(self):
        # TODO 
        return 'Nearest Neighbor Heuristic Cost : '+ self.nearestNeighborHeuristic

    # Returns the cost of the solution produced by 
    # the nearest neighbor heuristix
    def nearestNeighborHeuristic(self):
        costs = np.zeros(self.n)

        # TODO

        return min(costs)

    # Heuristic function
    # Returns inverse of smallest distance between r and u
    def eta(self, r, u):
        # TODO
        pass

    def optimize(self, num_iter):
        for _ in range(num_iter):
            for _ in range(self.n-1):
                for ant in self.ants:
                    ant.move()

            min(self.ants).globalUpdate()

            for ant in self.ants:
                ant.reset(self)

if __name__ == "__main__":
    rand.seed(420)

    #file = open('d198')
    file = open('dantzig.csv')

    adjMat = np.loadtxt(file, delimiter=",")

    ant_colony = Colony(adjMat)

    ant_colony.optimize(1000)
