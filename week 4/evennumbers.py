def even_numbers(first, last):
    return [x for x in range(first, last) if x % 2 == 0]

print(even_numbers(0, 10))