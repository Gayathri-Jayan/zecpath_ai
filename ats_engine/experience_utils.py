def calculate_total_experience(durations):

    total = 0

    for value, unit in durations:

        value = int(value)

        if "year" in unit:
            total += value

        elif "month" in unit:
            total += value / 12

    return round(total, 1)