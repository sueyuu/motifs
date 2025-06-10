import math
import numpy as np
from tslearn.metrics import dtw


def calculate_g_xt(x_t):
    if x_t <= 0:
        raise ValueError("x_t should be positive number!")
    if x_t == 1:
        return -5.381
    return math.pow(math.log(x_t), 1.084) - 5.381


def calculate_g_x(x):
    return [(calculate_g_xt(x_t)) for x_t in x]


def calculate_f_jk(dp_j, dp_k):
    """
    calculate_g_xt的部分可以針對全部dp在一開始就平行運算好存起來
    不用一直重複call
    """
    dp_j = [(calculate_g_xt(g_j)) for g_j in dp_j]
    dp_k = [(calculate_g_xt(g_k)) for g_k in dp_k]
    return dtw(dp_j, dp_k)
