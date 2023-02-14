
def tarbar(text='Тарабарский язык. После каждой гласной буквы, ставит букву "c" и эту же гласную букву :)'):
    vowels = 'ауоыиэяюёеАУОЫИЭЯЮЁЕ'  
    return ''.join([letter + 'c' + letter.lower() if letter in vowels else letter for letter in text])

# перевод текстового файла
def create_tarbar_txt(filename):
    with open(filename, encoding='utf-8') as f:
        for line in f:        
            with open('tarbar.txt', 'a', encoding='utf-8') as file:
                file.write(tarbar(text=line))
    
create_tarbar_txt('txt.txt')