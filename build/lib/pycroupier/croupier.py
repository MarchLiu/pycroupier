import math
import random
from typing import List


class Croupier():
    def __init__(self, poker):
        self.poker = poker

    def rand_index(self, cards):
        return self.poker(cards)

    def select_one(self, cards):
        if cards is None or len(cards) == 0:
            return None
        if len(cards) == 1:
            return cards[0]

        idx = self.poker.select(cards)
        return cards[idx]

    def select(self, cards, size):
        if cards is None or len(cards) == 0:
            return []
        if len(cards) == 1 and size > 0:
            return cards[:]

        buffer = cards[:]
        return self.draw(buffer, size)

    def draw_one(self, cards: List):
        if cards is None or len(cards) == 0:
            return None
        if len(cards) == 1:
            result = cards[0]
            del cards[0]
            return result

        idx = self.poker.select(cards)
        result = cards[idx]
        cards.remove(result)
        return result

    def draw(self, cards, size):
        if cards is None or len(cards) == 0:
            return []
        if len(cards) == 1 and size > 0:
            result = cards[:]
            del cards[0]
            return result

        result = []
        while len(result) < size and len(cards) > 0:
            result.append(self.draw_one(cards))

        return result


class Poker():
    def __init__(self, rand):
        self.rand = rand

    def select(self, cards):
        pass


class Fair(Poker):
    def __init__(self, rand):
        super().__init__(rand)

    def select(self, cards):
        if cards is None or len(cards) == 0:
            return None
        if len(cards) == 1:
            return 0
        return self.rand.randint(0, len(cards) - 1)


class Damping(Poker):
    def __init__(self, rand):
        super().__init__(rand)

    def select(self, cards):
        if cards is None or len(cards) == 0:
            return None
        if len(cards) == 1:
            return 0

        top = math.log(len(cards) + 1)
        score = self.rand.random() * top
        return int(math.floor(math.exp(score) - 1))


class Invert(Poker):
    def __init__(self, rand):
        super().__init__(rand)

    def select(self, cards):
        if cards is None or len(cards) == 0:
            return None
        if len(cards) == 1:
            return 0

        top = math.log(len(cards) + 1)
        score = self.rand.random() * top
        return len(cards) - int(math.floor(math.exp(score)))


class Ranked(Poker):
    def __init__(self, rank, rand):
        super().__init__(rand)
        self.rank = rank

    def select(self, cards):
        if cards is None or len(cards) == 0:
            return None
        if len(cards) == 1:
            return 0

        weights = [self.rank(card) for card in cards]
        steps = [0]
        for weight in weights:
            last = steps[len(steps) - 1]
            steps.append(last + weight)

        top = steps[len(steps) - 1]
        score = self.rand.random() * top
        for idx in range(len(steps)):
            if steps[idx] <= score < steps[idx + 1]:
                return idx
        else:
            return None


class BinaryRanked(Poker):
    def __init__(self, rank, rand):
        super().__init__(rand)
        self.rank = rank

    def select(self, cards):
        if cards is None or len(cards) == 0:
            return None
        if len(cards) == 1:
            return 0

        weights = [self.rank(card) for card in cards]
        steps = [0]
        for weight in weights:
            last = steps[len(steps) - 1]
            steps.append(last + weight)

        top = steps[len(steps) - 1]
        score = self.rand.random() * top

        low = 0
        high = len(cards)
        idx = int(high / 2)
        while high - low > 1:
            if steps[idx] <= score < steps[idx + 1]:
                return idx
            elif score < steps[idx]:
                high = idx
                idx = int(low + (high - low) / 2)
            else:
                low = idx
                idx = int(low + (high - low) / 2)
        else:
            return idx


class LiteRanked(Poker):
    def __init__(self, rank, rand):
        super().__init__(rand)
        self.rank = rank

    def select(self, cards):
        if cards is None or len(cards) == 0:
            return None
        if len(cards) == 1:
            return 0

        steps = []
        for idx in range(len(cards)):
            for x in range(self.rank(cards[idx])):
                steps.append(idx)

        top = len(steps) - 1
        score = self.rand.randint(top)
        return steps[score]


class ZipRanked(Poker):
    """rand select use Zip buffer.
The rank function should be returns int or any discrete number type, Otherwise, there is any performance.
    """

    def __init__(self, rank, rand):
        super().__init__(rand)
        self.rank = rank

    def select(self, cards):
        if cards is None or len(cards) == 0:
            return None
        if len(cards) == 1:
            return 0

        buffer = {}
        for idx, card in enumerate(cards):
            w = self.rank(card)
            positions = buffer.get(w, [])
            positions.append(idx)

        weights = list(buffer.keys())

        steps = [0]
        for weight in weights:
            last = steps[len(steps) - 1]
            steps.append(last + weight)

        top = steps[len(steps) - 1]
        score = self.rand.random() * top
        weight_index = 0
        for idx in range(len(steps)):
            if steps[idx] <= score < steps[idx + 1]:
                weight_index = idx
                break

        weight = weights[weight_index]

        positions = buffer[weight]
        pos_index = self.rand.randint(len(positions))
        return positions[pos_index]
