import time

def countdown(number):
    x = number
    while x > 0:
        print(f'{x} SECOND(S)!')
        x -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(number):
    x = number
    while x > 0:
        print(f'{x} SECOND(S)!')
        x -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")