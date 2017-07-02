import random
import datetime
import sys
import time
import statistics

def _generate_parent(length, geneSet, get_fitness):
    """ generate a random string from a geneSet"""
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    # genes = ''.join(genes)
    fitness = get_fitness(genes)
    return Chromosome(genes, fitness, "avorton")


def _mutate(parent, geneSet, get_fitness):
    """ change one random character from the string """
    childGenes = parent.Genes[:]
    index = random.randrange(0, len(parent.Genes))
    newGene, alternate = random.sample(geneSet, 2)
    childGenes[index] = alternate if newGene == childGenes[index] else newGene
    fitness = get_fitness(childGenes)
    return Chromosome(childGenes, fitness, "avorton")


def get_best(get_fitness, targetLen, optimalFitness, geneSet, display):
    random.seed()
    bestParent = _generate_parent(targetLen, geneSet, get_fitness)
    display(bestParent)

    if bestParent.Fitness >= optimalFitness:
        return bestParent

    while True:
        child = _mutate(bestParent, geneSet, get_fitness)
        
        if bestParent.Fitness >= child.Fitness:
            continue
        child.ChildType = "Fetus"

        display(child)
        if child.Fitness >= optimalFitness:
            return child
        bestParent = child

class Chromosome:
    def __init__(self, genes, fitness, childType):
        self.Genes = genes
        self.Fitness = fitness
        self.ChildType = childType

class Benchmark:
    @staticmethod
    def run(function):
        timings = []
        stdout = sys.stdout
        for i in range(100):
            sys.stdout = NullWriter()
            startTime = time.time()
            function()
            seconds = time.time() - startTime
            sys.stdout = stdout
            timings.append(seconds)
            mean = statistics.mean(timings)
            if i < 10 or i % 10 == 9:
                print("{}\t{}\t{}".format(1+i, mean, (statistics.stdev(timings, mean) if i > 0 else 0)))


class NullWriter():
    def write(self, s):
        pass
