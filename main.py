def input_error(func):
    """ Errors handler """
    def wrapper(*args):
        try:
            return func(*args)
        except KeyError as error:
            print(f'Wrong command, KeyRrror: {error}')
        except IndexError as error:
            print(f'Wrong command, IndexError: {error}')
        except ValueError as error:
            print(f'Wrong command, ValueError: {error}')
    return wrapper


def hello():
    print(f'How can I help you?')


def goodbye():
    print(f'Good bye!')
    quit()


def add():
    """
    "add ...". За цією командою бот зберігає у пам'яті (у словнику, наприклад) новий контакт.
    Замість ... користувач вводить ім'я та номер телефону, обов'язково через пробіл.
    """
    pass


def change():
    """
    "change ..." За цією командою бот зберігає в пам'яті новий номер телефону існуючого контакту.
    Замість ... користувач вводить ім'я та номер телефону, обов'язково через пробіл.
    """
    pass


def phone():
    """
    "phone ...." За цією командою бот виводить у консоль номер телефону для зазначеного контакту.
    Замість ... користувач вводить ім'я контакту, чий номер треба показати.
    """
    pass


def showall():
    """
    "show all". За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль.
    """
    pass


def main():
    """ Main function - all interaction with user """
    pass


if __name__ == '__main__':
    main()
