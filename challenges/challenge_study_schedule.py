def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    count = 0
    for studant in permanence_period:
        try:
            entrada = int(studant[0])
            saida = int(studant[1])
            if entrada <= int(target_time) <= saida:
                count += 1
        except (TypeError, ValueError):
            return None
    return count

