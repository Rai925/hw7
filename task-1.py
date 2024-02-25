def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").split()
        command, args = user_input[0], user_input[1:]

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        if command == "hello":
            print("How can I help you?")
            continue

        if command == "add":
            if len(args) != 2:
                print("Invalid format. Please use: add [name] [phone]")
            else:
                name, phone = args
                try:
                    record = Record(Name(name))
                    record.add_phone(phone)
                    book.add_record(record)
                    print("Contact added.")
                    print(book.data)  # Доданий рядок для виведення змісту book.data
                except ValueError as e:
                    print(e)

        if command == "change":
            if len(args) != 3:
                print("Invalid format. Please use: change [name] [old phone] [new phone]")
            else:
                name, old_phone, new_phone = args
                record = book.find(name)
                if record:
                    try:
                        record.edit_phone(old_phone, new_phone)
                        print("Phone number updated.")
                    except ValueError as e:
                        print(e)
                else:
                    print("Contact not found.")

        if command == "phone":
            if len(args) != 1:
                print("Invalid format. Please use: phone [name]")
            else:
                name = args[0]
                record = book.find(name)
                if record:
                    print(record)
                else:
                    print("Contact not found.")

        if command == "add-birthday":
            if len(args) != 2:
                print("Invalid format. Please use: add-birthday [name] [birthday (DD.MM.YYYY)]")
            else:
                name, birthday = args
                record = book.find(name)
                if record:
                    try:
                        record.add_birthday(birthday)
                        print("Birthday added.")
                    except ValueError as e:
                        print(e)
                else:
                    print("Contact not found.")

        elif command == "birthdays":
            upcoming_birthdays = book.get_upcoming_birthdays()
            if not upcoming_birthdays:
                print("No upcoming birthdays in the next week.")
            else:
                print("Upcoming birthdays:")
                for record in upcoming_birthdays:
                    print(f"{record.name}'s birthday is on {record.birthday.value}.")

        elif command == "all":
            if not book.data:
                print("No contacts found.")
            else:
                headers = ["Name", "Phones", "Birthday"]
                table_data = []
                for record in book.data.values():
                    phone_numbers = '; '.join(str(phone) for phone in record.phones)
                    birthday = str(record.birthday) if record.birthday else "N/A"
                    table_data.append([record.name.value, phone_numbers, birthday])
                print(tabulate(table_data, headers=headers, tablefmt="grid"))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
