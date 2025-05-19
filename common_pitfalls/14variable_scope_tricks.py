# Common pitfall with closures capturing variables
def create_multipliers():
    return [lambda x: i * x for i in range(5)]

multipliers = create_multipliers()
print([m(2) for m in multipliers])  # Output: [8, 8, 8, 8, 8] (all use last i=4)

# Fix using default argument trick
def create_multipliers_fixed():
    return [lambda x, i=i: i * x for i in range(5)]

multipliers_fixed = create_multipliers_fixed()
print([m(2) for m in multipliers_fixed])  # Output: [0, 2, 4, 6, 8]
