def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()


try:
    test_function()
    inner_function()
except NameError:
    print('inner_function не определена в глобальной области видимости')
