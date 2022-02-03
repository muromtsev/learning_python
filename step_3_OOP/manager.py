from person_start import Person

class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager') # явный вызов метода суперкласса, чтобы установить поле 'job' автоматически
    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self, percent + bonus) # вызов метода суперкласса и явная передача self

if __name__ == '__main__':
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    print(tom.lastName())
    tom.giveRaise(.20)
    print(tom.pay)
    print('-' * 10)
    # Person.__str__() - отформатированная строка для отображения объектов целиком - выглядит лучше, чем по умолчанию
    print(tom)