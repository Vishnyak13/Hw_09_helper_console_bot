def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Please enter the contact in the format:\nName: phone number"
        except ValueError:
            return "Incorrectly entered command!"
        except KeyError:
            return "Contact not found"

    return inner


def unknown_command(*args):
    return "Unknown command, try again or write 'help'!"


def greeting(*args):
    return "Hello! How can I help you?"


def to_exit(*args):
    return "Good bye!"


contact_dict = {"Olya": "0955521545",
                "Andriy": "0687985644",
                "Katya": "0509876543"}


@input_error
def add_contact(*args):
    contact_dict.update({str(args[0].title()): int(args[1])})
    return f"Contact {args[0].title()} with phone {args[1]} successfully added!"


@input_error
def change_phone(*args):
    contact_dict[args[0]] = args[1]
    return f"Contact {args[0]} successfully updated!"


@input_error
def remove_contact(*args):
    del contact_dict[args[0]]
    return f"Contact {args[0].title()} successfully remove!"


@input_error
def find_phone(*args):
    return contact_dict[args[0]]


def show_all(*args):
    return "\n".join([f"{key.title()}: {value}" for key, value in contact_dict.items()]) if len(
        contact_dict) > 0 else 'Contacts are empty'


def help(*args):
    return """
Enter "hello", "hi" for greeting
Enter "add", "new" for add new contact
Enter "change", "replace" for change phone
Enter "phone", "number", "find" for find phone
Enter "show all", "show" for show all contacts
Enter "good bye", "close", "exit", ".", "bye", "stop" for exit exit the program
Enter "del", "delete", "remove" for delete contact
Enter "help" to open a list of all commands
"""


commands = {
    greeting: ["hello", "hi"],
    add_contact: ["add", "new"],
    change_phone: ["change", "replace"],
    find_phone: ["phone", "number", "find"],
    show_all: ["show all", "show"],
    to_exit: ["good bye", "close", "exit", ".", "bye", "stop"],
    remove_contact: ["del", "delete", "remove"],
    help: ["help"]
}


def input_parser(user_input):
    for key, values in commands.items():
        for i in values:
            if user_input.lower().startswith(i.lower()):
                return key, user_input[len(i):].strip().split()
    else:
        return unknown_command, []


def main():
    while True:
        user_input = input('Waiting your command:>>> ')
        command, parser_data = input_parser(user_input)
        print(command(*parser_data))
        if command is to_exit:
            break


if __name__ == "__main__":
    main()
