"""
This is a Python program that implements a genetic algorithm for solving the 8-queens problem.
The 8-queens problem is a classic puzzle that asks how to place eight queens on a chessboard
such that none of them can attack each other. A queen can attack another queen if they are on the
same row, column, or diagonal.

The program uses the following steps to find a solution:

1. Initialize a population of random individuals (potential solutions).
2. Evaluate the fitness of each individual based on the number of non-attacking pairs of queens.
3. Select two parents from the population using rank selection.
4. Create two children from the parents using partially mapped crossover (PMX) and avoid duplicates.
5. Mutate the children by swapping two random positions with a dynamic mutation rate.
6. Add the children to the population and keep only the best individuals (elites).
7. Repeat steps 2-6 until a solution is found or a maximum number of generations is reached.
8. Display the solution as a board with queens.

The program uses some parameters to control the behavior of the genetic algorithm, such as:

- POPULATION_SIZE: The number of individuals in the population.
- NUM_GENERATIONS: The maximum number of generations to run the algorithm.
- MUTATION_RATE: The initial probability of mutating an individual.
- ELITE_CHROMOSOMES: The number of best individuals to keep in each generation.

The program also uses some helper functions to implement the genetic algorithm, such as:

- init_population: Creates a random population of individuals.
- fitness: Calculates the fitness of an individual based on the number of non-attacking pairs of queens.
- selection: Chooses two parents from the population using rank selection.
- crossover: Creates two children from the parents using partially mapped crossover (PMX) and avoid duplicates.
- mutation: Mutates an individual by swapping two random positions with a dynamic mutation rate.
- create_board: Displays an individual as a board with queens.

The program requires Python 3.x to run and does not depend on any external libraries or modules.
"""

import random
import math

POPULATION_SIZE = 500  
NUM_GENERATIONS = 1000
MUTATION_RATE = 0.3 # Initial mutation rate
ELITE_CHROMOSOMES = 5

def init_population(pop_size):
  # Create a random population of individuals
  # Each individual is a list of eight integers from 1 to 8
  # Each integer represents the position of a queen in a column
  # For example, [4,2,7,3,6,8,5,1] means that there is a queen in row 4 of column 1,
  # a queen in row 2 of column 2, and so on
  population = [random.sample(range(1,9), 8) for i in range(pop_size)]
  return population

def fitness(chromosome):
  # Calculate the fitness of an individual based on the number of non-attacking pairs of queens
  # The maximum fitness value is 28, which means that none of the queens can attack each other
  non_attacking_pairs = 0
  for i in range(8):
    for j in range(i+1,8):
      if chromosome[i] != chromosome[j] and abs(chromosome[i] - chromosome[j]) != j-i:
        non_attacking_pairs += 1
  return non_attacking_pairs
        
def selection(population):
  # Rank selection
  # Sort the population by fitness in descending order
  population = sorted(population, key=fitness, reverse=True)
  # Assign a rank to each individual based on its position in the sorted list
  ranks = [i+1 for i in range(len(population))]
  # Calculate the total rank of the population
  total_rank = sum(ranks)
  # Calculate the probability of each individual based on its rank
  probabilities = [r/total_rank for r in ranks]
  # Choose two parents randomly based on their probabilities
  parent1 = random.choices(population, probabilities)[0]
  parent2 = random.choices(population, probabilities)[0]
  
  return parent1, parent2

def crossover(parent1, parent2):
  # PMX crossover
  
  # Select two random crossover points
  point1 = random.randint(0,7) 
  point2 = random.randint(0,7)
  
  # Make sure point1 is smaller than point2
  if point1 > point2:
    point1, point2 = point2, point1

  # Perform crossover between points to create children
  child1 = parent1[0:point1] + parent2[point1:point2+1] + parent1[point2+1:]
  child2 = parent2[0:point1] + parent1[point1:point2+1] + parent2[point2+1:]

  # Map values from parent1 to child2
  map1 = {parent1[i]:child1[i] for i in range(8)}
  for i in range(8):
    if i < point1 or i > point2:
      child2[i] = map1[child2[i]]

  # Map values from parent2 to child1    
  map2 = {parent2[i]:child2[i] for i in range(8)}
  for i in range(8):
    if i < point1 or i > point2:
      child1[i] = map2[child1[i]]

  return child1, child2


def mutation(chromosome, gen):
  # Swap mutation with dynamic mutation rate
  global MUTATION_RATE
  
  if random.random() < MUTATION_RATE:
    # Choose two random positions to swap
    index1 = random.randint(0,7)
    index2 = random.randint(0,7)
    chromosome[index1], chromosome[index2] = chromosome[index2], chromosome[index1]

  # Update the mutation rate based on a sigmoid function
  MUTATION_RATE = (math.exp(-gen/NUM_GENERATIONS) / (math.exp(-gen/NUM_GENERATIONS) + math.exp(-gen/NUM_GENERATIONS))) * (0.5 - MUTATION_RATE) + MUTATION_RATE
  
  return chromosome

def create_board(solution):
  # Display an individual as a board with queens
  print("+" + "---+" * 8)
  for i in range(8):
    print("|", end="")
    for j in range(8):
      if solution[j] == i+1:
        print("👑 |", end="")
      else:
        print("   |", end="")
    print()
    
    print("+" + "---+" * 8)


def main():
  # The main function that runs the genetic algorithm
  population = init_population(POPULATION_SIZE)
  print("Initial population size:", len(population))
  print("Initial best fitness score:", fitness(population[0]))
  
  gen = 0
  for generation in range(NUM_GENERATIONS):
    print("Generation", generation)
    parent1, parent2 = selection(population)
    
    child1, child2 = crossover(parent1, parent2)
    
    child1 = mutation(child1, generation) 
    child2 = mutation(child2, generation)

    population.append(child1)
    population.append(child2)

    population = sorted(population, key=fitness, reverse=True)[:ELITE_CHROMOSOMES + 2]
    solution = population[0]

    solution = population[0]

    if fitness(solution) == 28:
      # Print a success message and exit the loop
      print("Solution found in generation", generation)
      print("Best solution: ", solution)
      break
    
    gen = generation

  if gen == 999:
    solution = population[0]
    # Print a final message after finishing all generations or finding a solution
    print(f"Finished {NUM_GENERATIONS} generations")
    print(f"Best solution: {solution}")
    print(f"Solution Fitness: {fitness(solution)}")
    
  create_board(solution)

main()
