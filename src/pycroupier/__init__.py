from pycroupier.croupier import Croupier, Fair, Damping, Invert, Ranked, BinaryRanked, LiteRanked, ZipRanked
import random


def fair():
    rand = random.Random()
    poker = Fair(rand)
    return Croupier(poker)


def fair_with_rand(rand):
    poker = Fair(rand)
    return Croupier(poker)


def fair_with_seed(seed):
    rand = random.Random(seed)
    poker = Fair(rand)
    return Croupier(poker)


def damping():
    rand = random.Random()
    poker = Damping(rand)
    return Croupier(poker)


def damping_with_rand(rand):
    poker = Damping(rand)
    return Croupier(poker)


def damping_with_seed(seed):
    rand = random.Random(seed)
    poker = Damping(rand)
    return Croupier(poker)


def invert():
    rand = random.Random()
    poker = Invert(rand)
    return Croupier(poker)


def invert_with_rand(rand):
    poker = Invert(rand)
    return Croupier(poker)


def invert_with_seed(seed):
    rand = random.Random(seed)
    poker = Invert(rand)
    return Croupier(poker)


def ranked(rank):
    rand = random.Random()
    poker = Ranked(rank, rand)
    return Croupier(poker)


def ranked_with_rand(rank, rand):
    poker = Ranked(rank, rand)
    return Croupier(poker)


def ranked_with_seed(rank, seed):
    rand = random.Random(seed)
    poker = Ranked(rank, rand)
    return Croupier(poker)


def lite_ranked(rank):
    rand = random.Random()
    poker = LiteRanked(rank, rand)
    return Croupier(poker)


def lite_ranked_with_rand(rank, rand):
    poker = Ranked(rank, rand)
    return Croupier(poker)


def lite_ranked_with_seed(rank, seed):
    rand = random.Random(seed)
    poker = LiteRanked(rank, rand)
    return Croupier(poker)


def binary_ranked(rank):
    rand = random.Random()
    poker = BinaryRanked(rank, rand)
    return Croupier(poker)


def binary_ranked_with_rand(rank, rand):
    poker = BinaryRanked(rank, rand)
    return Croupier(poker)


def binary_ranked_with_seed(rank, seed):
    rand = random.Random(seed)
    poker = BinaryRanked(rank, rand)
    return Croupier(poker)


def zip_ranked(rank):
    rand = random.Random()
    poker = ZipRanked(rank, rand)
    return Croupier(poker)


def zip_ranked_with_rand(rank, rand):
    poker = ZipRanked(rank, rand)
    return Croupier(poker)


def zip_ranked_with_seed(rank, seed):
    rand = random.Random(seed)
    poker = ZipRanked(rank, rand)
    return Croupier(poker)
