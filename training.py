import os
from canvas import Canvas
from racetrack import Track
from network import Network
from evolution import Evolution
from storage import Storage

car_image_paths = [os.path.join("images", f"car{i}.png") for i in range(5)]
canvas = Canvas(Track(3), car_image_paths)

# Network and genetic algorithm configuration
network_dimensions = 5, 4, 2  # input neurons, hidden layer neurons, output neurons
population_count = 40
max_generation_iterations = 50
keep_count = 4

networks = [Network(network_dimensions) for _ in range(population_count)]
evolution = Evolution(population_count, keep_count)
storage = Storage("brain.js")

best_chromosomes = storage.load()
for c, n in zip(best_chromosomes, networks):
    n.deserialize(c)


simulation_round = 1
while simulation_round <= max_generation_iterations and canvas.is_simulating:
    print(f"=== Round: {simulation_round} ===")
    canvas.simulate_generation(networks, simulation_round)
    simulation_round += 1
    if canvas.is_simulating:
        print(f"-- Average checkpoint reached: {sum(n.highest_checkpoint for n in networks) / len(networks):.2f}")
        print(f"-- Cars reached goal: {sum(n.has_reached_goal for n in networks)} of population {population_count}.")

        serialized = [network.serialize() for network in networks]
        offspring = evolution.execute(serialized)
        storage.save(offspring[:keep_count])  # save the best chromosomes

        # create networks from offspring
        networks = []
        for chromosome in offspring:
            network = Network(network_dimensions)
            network.deserialize(chromosome)
            networks.append(network)

