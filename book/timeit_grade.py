"""
    Использование модуля timeit  для оценки быстродействия
"""
# import time
# from timeit import timeit

# startTime = time.time()

# for i in range(1_000_000):
#     a, b = 42, 101
#     a = a ^ b
#     b = a ^ b
#     a = a ^ b
# print(time.time() - startTime, 'seconds')

# print(timeit('a, b = 24, 101; a = a ^ b; b = a ^ b; a = a ^ b'))
# print(timeit('a, b = 42, 101; temp = a; a = b; b = temp'))
# print('-' * 10)
# print(timeit('a, b = 42, 101; a, b = b, a'))

# print(timeit('random.randint(1, 100)', 'import random', number=10_000_000))