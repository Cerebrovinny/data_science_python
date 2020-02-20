enter_command = ""
started = False
while enter_command.lower() != "quit":
    enter_command = input("> ").lower()
    if enter_command == 'start':
        if started:
            print('The car is already started')
        else:
            started = True
            print('starting car...')
    elif enter_command == "stop":
        if not started:
            print('The car is already stoped')
        else:
            started = False
            print('stoping car')
    elif enter_command == "help":
        print("""
        start - to start car
        stop - to stop the car
        quit - to quit
        """)
    elif enter_command == 'quit':
        break
    else:
        print("Sorry i don't understand that")

while started:
    print('the car is already started')

