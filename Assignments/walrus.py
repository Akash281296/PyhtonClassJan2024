values = [45, 88, 0, 100, 218, 999, 7, 218]
stats = {
    "length": (
        values_length := len(values)
    ),  # Here we are initializing and using both at the same time
    "sum": (values_sum := sum(values)),
    "mean": values_sum / values_length,
}
print(stats)  # {'length': 8, 'sum': 1675, 'mean': 209.375}