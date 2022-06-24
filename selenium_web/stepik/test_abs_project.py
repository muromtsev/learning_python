def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"

if __name__ == "__main__":
    test_abs1()
    test_abs2()
    print("Everything passed")


    """
    Можно выделить три основных тестовых фреймворка для Python: unittest, PyTest и nose. Модуль unittest является встроенным инструментом Python — и это его большой плюс. PyTest и nose устанавливаются дополнительно, они позволяют получить расширенные возможности по сравнению с unittest. 
    Еще один плюс использования PyTest в том, что для него существует большое количество плагинов, которые позволяют решить практически любую проблему, связанную с запуском автотестов.
    """