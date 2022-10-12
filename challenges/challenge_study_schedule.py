def study_schedule(permanence_period, target_time):
    count = 0
    if type(target_time) != int:
        return None
    for studant in permanence_period:
        entrada, saida = studant
        if type(entrada) != int or type(saida) != int:
            return None
        if entrada <= target_time <= saida:
            count += 1
    return count
