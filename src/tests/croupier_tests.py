import unittest

from pycroupier import *


class CroupierTests(unittest.TestCase):
    def test_fair(self):
        counter = {}
        croupier = fair()
        data = list(range(20))
        times = 100000
        for i in range(times):
            item = croupier.select_one(data)
            counter[item] = counter.get(item, 0) + 1

        for value in data:
            print(f"fair select {value} items {counter.get(value, 0)}")

        self.assertEqual(sum(counter.values()), times)

    def test_damping(self):
        counter = {}
        croupier = damping()
        data = list(range(20))

        times = 100000
        for i in range(times):
            item = croupier.select_one(data)
            counter[item] = counter.get(item, 0) + 1

        for value in data:
            print(f"damping select {value} items {counter.get(value, 0)}")

        self.assertEqual(sum(counter.values()), times)

    def test_invert(self):
        counter = {}
        croupier = invert()
        data = list(range(20))

        times = 100000
        for i in range(times):
            item = croupier.select_one(data)
            counter[item] = counter.get(item, 0) + 1

        for value in data:
            print(f"invert select item {value}  {counter.get(value, 0)}")

        self.assertEqual(sum(counter.values()), times)

    def test_ranked(self):
        def rank(item):
            return item[1]

        counter = {}
        croupier = ranked(rank)
        data = [(i, random.randint(0, 10)) for i in range(20)]

        times = 100000
        for i in range(times):
            item = croupier.select_one(data)
            counter[item[0]] = (item[1], counter.get(item[0], (item[1], 0))[1] + 1)

        for item in data:
            print(f"ranked select item {item[0]} weight {item[1]} times {counter.get(item[0], (item[1], 0))}")

        self.assertEqual(sum(item[1] for item in counter.values()), times)

    def test_binary_ranked(self):
        def rank(item):
            return item[1]

        counter = {}
        croupier = binary_ranked(rank)
        data = [(i, random.randint(0, 10)) for i in range(20)]

        times = 100000
        for i in range(times):
            item = croupier.select_one(data)
            counter[item[0]] = (item[1], counter.get(item[0], (item[1], 0))[1] + 1)

        for item in data:
            print(f"ranked select item {item[0]} weight {item[1]} times {counter.get(item[0], (item[1], 0))}")

        self.assertEqual(sum(item[1] for item in counter.values()), times)