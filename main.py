contacts = {"John": "+380661234567",
            "Nik": "+380951234567",
            "Ann": "0672345678",
            "Bill": "0504567890",
            "Corey": "(0973456780)",
            "Kevin": "0999875645",
            }


def input_error(func):
    """ Errors handler """
    def wrapper(*args):
        try:
            return func(*args)
        except KeyError as error:
            return f'No name in contacts. Error: {error}'
        except IndexError as error:
            return f'Sorry, not enough params for command. Error: {error}'
        except ValueError as error:
            return f'Give me name and phone, please. Error: {error}'
        except TypeError as error:
            return f'Not enough arguments. Error: {error}'
    return wrapper


def hello() -> str:
    return f'How can I help you?'


def goodbye():
    print(f'Good bye!')
    quit()


@input_error
def add(*args) -> str:
    """
    "add ...". За цією командою бот зберігає у пам'яті (у словнику, наприклад) новий контакт.
    Замість ... користувач вводить ім'я та номер телефону, обов'язково через пробіл.
    """

    name, number, *_ = args
    if name in contacts:
        return f'This contact already exist'
    contacts.update({name: number})
    return f'Contact add successfully'


@input_error
def change(*args) -> str:
    """
    "change ..." За цією командою бот зберігає в пам'яті новий номер телефону існуючого контакту.
    Замість ... користувач вводить ім'я та номер телефону, обов'язково через пробіл.
    """

    name, number, *_ = args
    if name in contacts:
        contacts.update({name: number})
    else:
        return f'No contact "{name}"'
    return f'Contact change successfully'


@input_error
def phone(*args) -> str:
    """
    "phone ...." За цією командою бот виводить у консоль номер телефону для зазначеного контакту.
    Замість ... користувач вводить ім'я контакту, чий номер треба показати.
    """

    name = args[0]
    if contacts.get(name):
        return '\t{:>20} : {:<12} '.format(name, contacts.get(name))
    else:
        return f'No contact "{name}"'


@input_error
def show_all() -> str:
    """
    "show all". За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль.
    """

    result = []
    for name, numbers in contacts.items():
        result.append('\t{:>20} : {:<12} '.format(name, numbers))
    if len(result) < 1:
        return f'Contact list is empty'
    return '\n'.join(result)


def hlp(*args) -> str:
    return f'Known commands: hello, help, add, change, phone, show all, good bye, close, exit.'


def parser(msg: str):
    """ Parser and handler AIO """
    command = None
    params = []

    operations = {
        'hello': hello,
        'h': hlp,
        'help': hlp,
        'add': add,
        'change': change,
        'phone': phone,
        'show all': show_all,
        'good bye': goodbye,
        'close': goodbye,
        'exit': goodbye,
    }

    for key in operations:
        if msg.lower().startswith(key):
            command = operations[key]
            msg = msg.lstrip(key)
            for item in filter(lambda x: x != '', msg.split(' ')):
                params.append(item)
            return command, params
    return command, params



def main():
    """ Main function - all interaction with user """
    print(hello())
    while True:
        msg = input("Input command: ")
        command, params = parser(msg)
        if command:
            print(command(*params))
        else:
            print(f'Sorry, unknown command, try again. Type "h" for help.')


if __name__ == '__main__':
    main()
