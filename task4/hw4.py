
#розбиратиме введений користувачем рядок на команду та її аргументи. Команди та аргументи мають бути розпізнані незалежно від регістру введення.
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

#додати контакт
def add_contact(args, contacts):
    if len(args)<2 or len(args)>2:
        return "Input 2 parameters"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

#показати телефон
def show_phone(args, contacts):
    if len(args)<1 or len(args)>1:
        return "Input 1 parameters"
    name=args[0]
    if name in contacts:
        return contacts[name]
    return 'Not found'

#змінити контакт    
def change_contact(args, contacts):
    if len(args)<2 or len(args)>2:
        return "Input 2 parameters"
    name, phone = args
    if not name in contacts:
        return "Name is not found."
    contacts[name] = phone
    return "Contact updated."

#надрукувати всі контакти
def show_all(args, contacts):
    if len(args)!=0:
        return "Function don't take parameters"
    return contacts

# головна програма
def main():
    contacts = {'John':"123", 'Jane':"234", 'Steve':"555"}  #    [{'name':'John Doe', 'phone':'+380988858880'},
                        #{'name':'Alice Cooper', 'phone':'+48880884215'}]
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input) #розбиратиме введений користувачем рядок на команду та її аргументи.

        if command in ["close", "exit"]: #вихід із програми
            print("Good bye!")
            break
        elif command == "hello": #вітання
            print("How can I help you?")
        elif command == "add": #додати контакт
            print(add_contact(args, contacts))
        elif command == "phone": #показати телефон по імені
            print(show_phone(args, contacts))
        elif command == "change": #змінити телефон по імені
            print(change_contact(args, contacts))
        elif command == "all": #роздрукувати телефонну книгу
            print(show_all(args, contacts))   
        else:
            print("Invalid command.") #невідома команда

if __name__ == "__main__": 
    main()