def mediana(lst):
    lst.sort()
    return print(f"Mediana: {lst[1]}")

list_of_numbers = [int(input()) for number in range(3)]

mediana(list_of_numbers)