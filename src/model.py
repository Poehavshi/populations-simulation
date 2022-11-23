def get_dn_dt(index, B, quantities, increases):
    if index == 0:
        return increases[index] * quantities[index] + B[index][index + 1] * quantities[index] * quantities[index + 1]
    elif index == 1:
        return increases[index] * quantities[index] + B[index][index - 1] * quantities[index - 1] * quantities[index]
    return 0


def simulate(B, quantities, increases, time_interval, time_step):
    first_population_data = [quantities[0]]
    second_population_data = [quantities[1]]
    start = 0
    while start <= time_interval:
        start += time_step
        dn_dt_0 = get_dn_dt(0, B, quantities, increases)
        dn_dt_1 = get_dn_dt(1, B, quantities, increases)
        quantities[0] += dn_dt_0
        quantities[1] += dn_dt_1
        first_population_data.append(quantities[0])
        second_population_data.append(quantities[1])
    return first_population_data, second_population_data
