import string

ABC = string.ascii_lowercase
print(ABC)
# ABC = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
# txt = 'Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd'
# step = 1

def encryption(step, txt):
    ABC_WITH_STEP = ABC[step:] + ABC[:step]
    
    list_index_txt = []
    for i in txt:
        for k, j in enumerate(ABC):
            if i == j:
                list_index_txt.append(k)

    
    new_list_index = []
    for i in list_index_txt:
        for k, j in enumerate(ABC_WITH_STEP):
            if i == k:
                new_list_index.append(j)
    
    
    return ''.join(new_list_index)

# print(encryption(step, txt))

def decoding(step, txt):
    ABC_WITH_STEP = ABC[step:] + ABC[:step]
    list_txt_index = []
    for i in txt:
        for k, j in enumerate(ABC_WITH_STEP):
            if i == j:
                list_txt_index.append(k)

    list_txt = []
    for i in list_txt_index:
        for k, j in enumerate(ABC):
            if i == k:
                list_txt.append(j)
    
    return ''.join(list_txt)

s = decoding(3, 'Hawnj pk swhg xabkna ukq nqj')
print(s)
print('LEARN BEFORE YOU WORK'.lower())