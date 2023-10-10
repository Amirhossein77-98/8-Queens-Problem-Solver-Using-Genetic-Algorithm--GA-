# Genetic Algorithm for Solving the 8-Queens Problem

This is a Python program that implements a genetic algorithm for solving the 8-queens problem.
The program uses some parameters and helper functions to create and evolve a population of individuals (potential solutions) until a solution is found or a maximum number of generations is reached. The program displays the solution as a board with queens.

## Requirements

- Python 3.x
- No external libraries or modules

## Usage

- Run the program as `python main.py`
- The program will print the initial population size, the initial best fitness score, and the generation number.
- The program will also print the solution found, the final best fitness score, and the final generation number.
- The program will display the solution as a board with queens using the emoji 👑.

## Operators Used

The program uses the following encoding, selection, crossover, and mutation operators to implement the genetic algorithm:

- Encoding: Each individual is encoded as a list of eight integers from 1 to 8 (Permutation Encoding). Each integer represents the position of a queen in a column. For example, [4,2,7,3,6,8,5,1] means that there is a queen in row 4 of column 1, a queen in row 2 of column 2, and so on.
- Selection: The program uses rank selection to choose two parents from the population. Rank selection sorts the population by fitness in descending order and assigns a rank to each individual based on its position in the sorted list. Then it calculates the probability of each individual based on its rank and chooses two parents randomly based on their probabilities.
- Crossover: The program uses partially mapped crossover (PMX) to create two children from the parents. PMX preserves the relative order of the elements in the parents and avoids creating duplicate elements in the offspring. PMX works by copying a segment from one parent to the child and then mapping the values outside the segment according to the other parent and child.
- Mutation: The program uses swap mutation with dynamic mutation rate to mutate an individual. Swap mutation swaps two random positions in the individual's list. Dynamic mutation rate decreases as the generation number increases, using a sigmoid function. This allows the algorithm to explore more of the search space in the early stages and exploit the best solutions in the later stages.

## Example Output

Initial population size: 500
Initial best fitness score: 23
Generation 0
Generation 1
Generation 2
Generation 3
Generation 4
Generation 5
Solution found in generation 20
Best solution:  [8, 4, 1, 3, 6, 2, 7, 5]
+---+---+---+---+---+---+---+---+
|   |   |👑 |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |👑 |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |👑 |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |👑 |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |👑 |
+---+---+---+---+---+---+---+---+
|   |   |   |   |👑 |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |👑 |   |
+---+---+---+---+---+---+---+---+
|👑 |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
