def is_ordinal(number):
    ordinal = ['...', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
    if 1 <= number <= 12:
        return ordinal[number]
    else:
        return ordinal[0]

num = 3

print(is_ordinal(num))