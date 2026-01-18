def average_valid_measurements(values):
    total = 0
    count = 0

    if not values:
        return 0

    for v in values:
        if v is not None:
            try:
                # Attempt to convert to float only if it's not None
                val = float(v)
                total += val
                count += 1
            except (ValueError, TypeError):
                # Skip values that cannot be converted to a number
                continue

    if count == 0:
        return 0

    return total / count
