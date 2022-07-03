# Kanty Louange, Gakima, 20184109
# Jonathan, Metila, Matricule

import numpy as np
import random as rand


#c to remove : la classe colony est pr toutes les fourmies ("ants")
class Colony:
    class Ant:
        def __init__(self, colony):
            self.colony = colony
           
            self.pos = rand.randrange(self.colony.n)


            self.mem = np.zeros(self.colony.n)

            self.mem[self.pos] = 1

            self.path = [self.pos]
        
            self.cost = 0

        def reset(self, colony):
            self.__init__(colony)

        def __str__(self):
          return str(self.path)+ ', cost : ' + str(self.cost)

        def __lt__(self, other):
            return self.cost < other.cost

        # Returns city to be travelled to from current position
        def policy(self):
            if rand.random() < self.colony.q_0:
                row = adjMat[self.pos]
                rowCopy = np.copy(row)
                nextCity = np.where(row == np.min(row[np.nonzero(row)]))
                result = rand.choice(nextCity[0])
                if (self.mem[result]!= 1):
                    
                    return result   
                else:
                    #si le sommet est déjà visité, le coût de l'arête est mis à 0 dans la copie de
                    #la ligne pour chercher un autre minimum
                    #bug:ça marche juste pour 2 à 3 itérations
                    rowCopy[result] = 0
                    nextCity = np.where(rowCopy == np.min(rowCopy[np.nonzero(rowCopy)]))
                    result = rand.choice(nextCity[0])
                    return result
                #voir si le cas sommet visité fonctionne 

            else:
                #juste pour question de debuggage, la partie stochastique n'est pas résolue
                row = adjMat[self.pos]
                rowCopy = np.copy(row)
                nextCity = np.where(row == np.min(row[np.nonzero(row)]))
                result = rand.choice(nextCity[0])
                if (self.mem[result]!= 1):
                    return result   
                else:
                    #si le sommet est déjà visité, le coût de l'arête est mis à 0 dans la copie de
                    #la ligne pour chercher un autre minimum
                    rowCopy[result] = 0
                    nextCity = np.where(rowCopy == np.min(rowCopy[np.nonzero(rowCopy)]))
                    result = rand.choice(nextCity[0])
                
                    return result
                #voir si le cas sommet visité fonctionne 
                # Stochastic decision
                # TODO

        # Updates the local pheromones and position of ant
        # while keeping track of total cost and path
        def move(self):
            destination = self.policy()
            # local updating
            t0 = adjMat[self.pos][destination]
            #bug: self.cost reste à 0, à résoudre
            self.cost += t0
            #il faut changer le niveau de phéromones ici

            # Change position
            self.pos = destination
            self.mem[destination]= 1
            self.path.append(destination)
            

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
        self.ants = [self.Ant(self) for _ in range(m)]

        self.beta = beta
        self.alpha = 0.1
        self.q_0 =q_0

    def __str__(self):
        return ('Nearest Neighbor Heuristic Cost : '+ str(self.nearestNeighborHeuristic))

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
