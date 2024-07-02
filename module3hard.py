data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data_structure):
    summa = 0
    for current in data_structure:
        if isinstance(current, list):
            summa += calculate_structure_sum(current)
        elif isinstance(current, tuple):
            summa += calculate_structure_sum(current)
        elif isinstance(current, set):
            summa += calculate_structure_sum(current)
        elif isinstance(current, int):
            summa += current
        elif isinstance(current, str):
            summa += len(current)
        elif isinstance(current, dict):
            keys, values = current.keys(), current.values()
            summa += calculate_structure_sum(keys)
            summa += calculate_structure_sum(values)

    return summa

result = calculate_structure_sum(data_structure)
print(result)