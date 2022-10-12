def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    count = 0
    if type(target_time) != int:
        return None
    for studant in permanence_period:
        entrada = studant[0]
        saida = studant[1]
        if type(entrada) != int or type(saida) != int:
            return None
        if entrada <= int(target_time) <= saida:
            count += 1
    return count
