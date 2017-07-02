# -*- coding: utf-8 -*-

import genetic
import datetime
import unittest
import random


def get_fitness(guess, target):
    return sum(1 for expected, actual in zip(target, guess) if expected == actual)

def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    if isinstance(candidate, genetic.Chromosome):
        # print("{}\t{}\t{}\t{}".format(''.join(candidate.Genes), candidate.Fitness, timeDiff, candidate.ChildType))
        # import pdb; pdb.set_trace()
        print("{}\t{}\t{}".format( ''.join(candidate.Genes), candidate.ChildType, timeDiff))
    else:
        raise ValueError("Wrong object to display")


class GuessPasswordTests(unittest.TestCase):
    geneset = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.123!@#"

    # def test_Hello_World(self):
    #     target = "Hello World!"
    #     self.guess_password(target)
    #
    # def test_do_Random(self):
    #     length = 60
    #     target = ''.join( random.choice(self.geneset) for _ in range(length) )
    #     self.guess_password(target)

    # def test_Geneset(self):
    #     self.guess_password(self.geneset)

    def guess_password(self, target):
        startTime = datetime.datetime.now()

        def fnGetFitness(genes):
            return get_fitness(genes, target)

        def fnDisplay(candidate):
            return display(candidate, startTime)

        optimalFitness = len(target)

        best = genetic.get_best(fnGetFitness, len(target), optimalFitness, self.geneset, fnDisplay)
        self.assertEqual(''.join(best.Genes), target)


    def test_Benchmark(self):
        genetic.Benchmark.run(self.three_letters)

    # def test_Salut_Vlad(self):
    #     target = "Salut Vlad!"
    #     self.guess_password(target)

    def three_letters(self):
        target = "asd#@!"
        self.guess_password(target)


if __name__ == '__main__':
    unittest.main()
