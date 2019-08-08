# Write a funcion name collatz()
def collatz(number):
    if (number % 2) == 0:
        # print(number // 2)
        return (number // 2)
    else: 
        # print(3 * number + 1)
        return (3 * number + 1)
while True:
    try:
        print("Enter number:")
        number = int(input())
        break
    except (ValueError, NameError):
        print('Error: Invalid argument. Please enter an Integer.')
    
while True:
    if number != 1:
        number = collatz(number)
        print(number)
    else:
        break
