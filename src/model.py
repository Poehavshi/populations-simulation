import math


def get_dn_dt(index, B, quantities, increases, time_importance, time):
    summa = 0
    for i in range(len(quantities)):
        summa += B[index][i] * quantities[index] * quantities[i]
    if time_importance != 0:
        return increases[index] * time_importance * math.sin(time)**2 * quantities[index] + summa
    return increases[index] * quantities[index] + summa


def simulate(B, quantities, increases, time_interval, time_step, time_importance):
    population_data = [[quantities[i]] for i in range(len(quantities))]
    start = 0
    while start <= time_interval:
        start += time_step
        for i in range(len(quantities)):
            dn_dt = get_dn_dt(i, B, quantities, increases, time_importance, start)
            quantities[i] += dn_dt
            population_data[i].append(quantities[i])
    return population_data
