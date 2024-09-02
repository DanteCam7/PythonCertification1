
def change_letters(type):
    def uppercase(text):
        print(text.upper())

    def lowercase(text):
        print(text.lower())

    if type == 'may':
        return uppercase
    elif type == 'min':
        return lowercase


my_operation = change_letters('may')

my_operation('python')


def a_function(function):
    return function


#a_function(uppercase('trying'))


def decorate_greet(function):

    def other_function(word):
        print('hello')
        function(word)
        print('goodbye')
    return other_function

@decorate_greet
def uppercase(text):
    print(text.upper())

@decorate_greet
def lowercase(text):
    print(text.lower())


uppercase_decorated = decorate_greet(uppercase)


uppercase_decorated('dante')


uppercase('wololo')
