PHONEBOOK = {}


def input_error(wrap):
    def inner(*args):
        try:
            return wrap(*args)
        except IndexError:
            return "Please, input name and phone"
        except ValueError:
            return "Please, input the information"
        except KeyError:
            return "Please, input the name from phonebook"

    return inner


@input_error
def add_handler(data):
    name = data[0].title()
    phone = data[1]
    PHONEBOOK[name] = phone
    return f"Contact {name}, phone {phone}"


@input_error
def change_handler(data):
    name = data[0].title()
    phone_new = data[1]
    if name in PHONEBOOK:
        PHONEBOOK[name] = phone_new
        return f"Contact {name}, NEW phone {phone_new}"


@input_error
def number_by_name_handler(data):
    name = data[0].title()
    return PHONEBOOK[name]


@input_error
def show_all_handler(*args):
    print(PHONEBOOK)


@input_error
def exit_handler(*args):
    return "Good Bye"


@input_error
def hello_handler(*args):
    return "Hello"


def command_parser(raw_str: str):
    element = raw_str.split()

    for key, value in COMMANDR_1.items():
        if element[0].lower() in value:
            return key, element[1:]
        elif " ".join(element[:2]).lower() in value:
            return key, element[2:]

    return (
        None,
        "Unknown command, please, input applicable command",
    )


COMMANDR_1 = {
    add_handler: ["add", "+"],
    exit_handler: ["close", "exit", "good buy"],
    hello_handler: ["hello"],
    change_handler: ["change"],
    number_by_name_handler: ["phone"],
    show_all_handler: ["show all"],
}


def main():
    while True:
        user_input = input(">>>")
        if not user_input:
            continue
        func, data = command_parser(user_input)
        if func:
            result = func(data)
        else:
            result = data

        print(result)

        if func == exit_handler:
            break


if __name__ == "__main__":
    main()
