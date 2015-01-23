import random
def rnd_seq(l,alphabet):

    return "".join([random.choice(alphabet) for _ in range(l)])



print rnd_seq(6,'acgt')






