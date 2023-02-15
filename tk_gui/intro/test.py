def simple():
    def action():
        print(spam)
    spam = 'ni'
    return action

# act = simple()
# act()

def weird():
    spam = 42
    return (lambda: spam * 2)

# act = weird()
# print(act())

# def odd():
#     funcs = []
#     for c in 'abcdefg':
#         funcs.append((lambda c=c: c))
#     return funcs

# for func in odd():
#     print(func(), end=' ')

funcs = []
for c in 'abcdefg':
    funcs.append((lambda c=c: c))
for func in funcs:
    print(func(), end=' ')