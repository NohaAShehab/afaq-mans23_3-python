

def askforInt(message):
    while True:
        num = input(message)
        if num.isdigit():
            return int(num)

        print("--- please enter valid number ")