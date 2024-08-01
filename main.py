import bot.actions as actions
from bot.helpers import load_data, parse_input, invalid_command


def main():
    book = load_data()
    print("Welcome to the assistant bot!")

    command_handlers = {
        "hello": lambda args: actions.hello(),
        "add": lambda args: actions.add_contact(args, book),
        "change": lambda args: actions.change_contact(args, book),
        "phone": lambda args: actions.show_phone(args, book),
        "all": lambda args: actions.show_all(book),
        "add-birthday": lambda args: actions.add_birthday(args, book),
        "show-birthday": lambda args: actions.show_birthday(args, book),
        "birthdays": lambda args: actions.birthdays(args, book),
        "exit": lambda args: actions.exit_bot(book),
        "close": lambda args: actions.exit_bot(book),
    }

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        handler = command_handlers.get(command, lambda args: invalid_command())
        result = handler(args)
        if result:
            print(result)

if __name__ == "__main__":
    main()