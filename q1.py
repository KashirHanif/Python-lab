import random

campaigns = [
    {"impact": 40, "cost": 20},
    {"impact": 70, "cost": 60},
    {"impact": 60, "cost": 50},
    {"impact": 85, "cost": 90},
    {"impact": 55, "cost": 40},
    {"impact": 30, "cost": 15},
    {"impact": 75, "cost": 80},
    {"impact": 45, "cost": 35}
]

BUDGET = 180
CHROMOSOME_LENGTH = len(campaigns)
POP_SIZE = 20
MUTATION_RATE = 0.05
GENERATIONS = 50

def generate_individual():
    return [random.randint(0, 1) for _ in range(CHROMOSOME_LENGTH)]

def fitness(individual):
    total_impact = 0
    total_cost = 0
    for i in range(CHROMOSOME_LENGTH):
        if individual[i] == 1:
            total_impact += campaigns[i]["impact"]
            total_cost += campaigns[i]["cost"]
    return total_impact if total_cost <= BUDGET else 0

def roulette_wheel_selection(population):
    fitnesses = [fitness(ind) for ind in population]
    total_fitness = sum(fitnesses)
    if total_fitness == 0:
        return random.choice(population)
    pick = random.uniform(0, total_fitness)
    current = 0
    for ind, fit in zip(population, fitnesses):
        current += fit
        if current > pick:
            return ind

def uniform_crossover(parent1, parent2):
    return [
        parent1[i] if random.random() < 0.5 else parent2[i]
        for i in range(CHROMOSOME_LENGTH)
    ]

def mutate(individual):
    return [
        bit if random.random() > MUTATION_RATE else 1 - bit
        for bit in individual
    ]

def genetic_algorithm():
    population = [generate_individual() for _ in range(POP_SIZE)]
    best = max(population, key=fitness)

    for generation in range(GENERATIONS):
        new_population = []

        for _ in range(POP_SIZE):
            parent1 = roulette_wheel_selection(population)
            parent2 = roulette_wheel_selection(population)
            child = uniform_crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

        population = new_population
        best_candidate = max(population, key=fitness)
        if fitness(best_candidate) > fitness(best):
            best = best_candidate

        print(f"Generation {generation + 1}: Best Fitness = {fitness(best)}")

    return best

best_solution = genetic_algorithm()

print("\nBest Campaign Selection (binary):", best_solution)
total_impact = fitness(best_solution)
total_cost = sum(campaigns[i]["cost"] for i in range(CHROMOSOME_LENGTH) if best_solution[i] == 1)
print("Total Impact:", total_impact)
print("Total Cost:", total_cost)
print("Selected Campaigns:")
for i in range(CHROMOSOME_LENGTH):
    if best_solution[i] == 1:
        print(f"  Campaign C{i+1} → Impact: {campaigns[i]['impact']}, Cost: {campaigns[i]['cost']}")
