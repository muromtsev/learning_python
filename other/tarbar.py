
def tarbar(text='Тарабарский язык. После каждой гласной буквы, ставит букву "c" и эту же гласную букву :)'):
    vowels = 'ауоыиэяюёеАУОЫИЭЯЮЁЕ'  
    return ''.join([letter + 'c' + letter.lower() if letter in vowels else letter for letter in text])

print(tarbar(text='''Вернись, лесной олень,
По моему хотенью,
Умчи меня, олень,
В свою страну оленью.
Где сосны рвутся в небо,
Где быль живёт и небыль,
Умчи меня туда, лесной олень.'''))


# перевод текстового файла
def create_tarbar_txt(text, filename=None):
    if filename:
        with open(filename, encoding='utf-8') as f:
            for line in f:
                with open('tarbar.txt', 'a', encoding='utf-8') as file:
                    file.write(tarbar(text=line))
    else:
        with open('txt.txt', 'w', encoding='utf-8') as file:
               file.write(tarbar(text=text))

# create_tarbar_txt(filename='txt.txt')