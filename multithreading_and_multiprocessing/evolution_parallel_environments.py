"""
A model of population evolution in parallel environments.
Each organism is processed as a separate object in a process pool.
"""
import multiprocessing
import random
import functools
import time
from typing import List, Dict, Any, Callable, Generator


def log_evolution(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator to log mutations during the life cycle."""
    @functools.wraps(func)
    def wrapper(self: 'Organism', *args: Any, **kwargs: Any) -> Any:
        old_genome = self.genome
        result = func(self, *args, **kwargs)

        if result and result.get('mutated'):
            print(f"[MUTATION] Організм {result['id']}: {old_genome} -> {result['genome']}")
        return result

    return wrapper


class Organism:
    """Represents a single organism in the simulation."""

    DNA_BASES: str = "ACTG"

    def __init__(self, org_id: int, fitness: float, genome: str) -> None:
        self.org_id = org_id
        self.fitness = fitness
        self.genome = genome

    def get_info(self) -> str:
        """
        Public method to get organism's status.
        Fixed R0903: Adding a second public method.
        """
        return f"ID: {self.org_id} | Genome: {self.genome} | Fitness: {self.fitness:.2f}"

    def _mutate_genome(self) -> str:
        """Helper method to mutate one character in the genome."""
        genome_list = list(self.genome)
        idx = random.randint(0, len(genome_list) - 1)
        new_base = random.choice(self.DNA_BASES)
        genome_list[idx] = new_base

        return "".join(genome_list)

    @log_evolution
    def simulate_life_cycle(self, env_difficulty: float) -> Dict[str, Any]:
        """Simulation of one life cycle in a separate process."""
        survival_chance = random.random() * self.fitness
        mutated = False

        if survival_chance < env_difficulty:
            self.genome = self._mutate_genome()
            self.fitness += random.uniform(0.05, 0.2)
            mutated = True

        return {
            "id": self.org_id,
            "fitness": round(self.fitness, 2),
            "genome": self.genome,
            "mutated": mutated,
            "alive": survival_chance > (env_difficulty * 0.4)
        }


class EvolutionEnv:
    """Environment that manages the population and evolution process."""
    def __init__(self, population_size: int) -> None:
        self.population = [
            Organism(i, random.uniform(0.6, 1.0), "AAAA")
            for i in range(population_size)
        ]
        self.generation = 0

    def get_population_gen(self) -> Generator[Organism, None, None]:
        """Generator for traversing the entire population."""
        yield from self.population

    def run_generation(self) -> None:
        """Run one generation in parallel."""
        self.generation += 1
        difficulty = random.uniform(0.4, 0.6)

        print(f"\n--- Покоління {self.generation} (Складність: {difficulty:.2f}) ---")

        with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
            results = pool.map(
                functools.partial(self._process_wrapper, diff=difficulty),
                self.get_population_gen()
            )

        survivors = [r for r in results if r['alive']]
        print(f"Вижило: {len(survivors)} із {len(self.population)}")

        if survivors:
            best = max(survivors, key=lambda x: x['fitness'])
            print(f"Кращий геном покоління: {best['genome']} (Fitness: {best['fitness']})")

        self._repopulate(survivors)

    @staticmethod
    def _process_wrapper(org: Organism, diff: float) -> Dict[str, Any]:
        """A static wrapper method for working inside a process."""
        return org.simulate_life_cycle(diff)

    def _repopulate(self, survivors: List[Dict[str, Any]]) -> None:
        """Restoration of population size."""
        if not survivors:
            print("Популяція вимерла!")
            return

        new_population = []
        for i in range(len(self.population)):
            parent = random.choice(survivors)
            child = Organism(i, parent['fitness'], parent['genome'])
            new_population.append(child)
        self.population = new_population


if __name__ == "__main__":

    world = EvolutionEnv(population_size=15)

    for _ in range(10):
        world.run_generation()
        time.sleep(1)
