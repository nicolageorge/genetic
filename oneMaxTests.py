import unittest
import datetime
import genetic

def get_fitness(genes):
    return genes.count(1)

class OneMaxTests(unittest.TestCase):
    def test(self, length=100):
        geneset = [0, 1]
