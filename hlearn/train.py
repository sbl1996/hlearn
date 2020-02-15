import math

from toolz import curry


@curry
def cosine_lr_decay(T_cur, base_lr, eta_min, T_0):
    mult = (1 + math.cos(math.pi * T_cur / T_0)) / 2
    lr = eta_min + (base_lr - eta_min) * mult
    return lr