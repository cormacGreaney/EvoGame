import random
#Choose to import the AmericanBoard for a standard 8x8 draughts game whihc is the same as Irish or English draughts
from draughts import AmericanBoard

# Possible moves, simplified for this example as I need to inlude double jumps and multi-jumps
# In a real implementation, moves would be generated based on the current board state
MOVES = ["forward-left", "forward-right", "jump-left", "jump-right"]

def generate_strategy(length=5):
    """Generate a random strategy as a list of moves"""
    return [random.choice(MOVES) for _ in range(length)]

def evaluate_strategy(strategy):
    """Return a score for a strategy based on captured opponent pieces this is a placeholder function as actual evaluation would require simulating the game"""
    board = AmericanBoard()
    score = 0
    for move in strategy:
        if "jump" in move:
            score += 1
    return score

def mutate_strategy(strategy, mutation_rate=0.2):
    """Randomly change some moves in the strategy"""
    new_strategy = strategy[:]
    for i in range(len(new_strategy)):
        if random.random() < mutation_rate:
            new_strategy[i] = random.choice(MOVES)
    return new_strategy

def crossover_strategy(parent1, parent2):
    """Combine two strategies"""
    point = random.randint(1, len(parent1) - 1)
    child = parent1[:point] + parent2[point:]
    return child

def main():
    population_size = 10
    generations = 5
    strategy_length = 5

    # Initialize population
    population = [generate_strategy(strategy_length) for _ in range(population_size)]

    print(population)

    for gen in range(generations):
        # Evaluate fitness
        fitness_scores = [evaluate_strategy(s) for s in population]

        # Print best strategy of this generation
        best_index = fitness_scores.index(max(fitness_scores))
        print(f"Generation {gen+1}: Best strategy = {population[best_index]}, Fitness = {fitness_scores[best_index]}")

        # Select top 50% strategies
        sorted_population = [s for _, s in sorted(zip(fitness_scores, population), key=lambda x: x[0], reverse=True)]
        survivors = sorted_population[:population_size // 2]

        # Reproduce
        new_population = survivors[:]
        
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(survivors, 2)
            child = crossover_strategy(parent1, parent2)
            child = mutate_strategy(child)
            new_population.append(child)

        population = new_population

if __name__ == "__main__":
    main()
