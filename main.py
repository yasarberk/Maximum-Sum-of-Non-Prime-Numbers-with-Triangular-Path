def checkPrimeNumber(number):
    if (type(number) != int):
        return "Number is not in range! Number must be integer!"
    elif number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    else:
        if number == 1 or number == 0:
            return False
        else:
            return "Number is negative"


def primePathChecker(number1, number2):
    path1 = checkPrimeNumber(number1)
    path2 = checkPrimeNumber(number2)

    if (path1 == False and path2 == False):

        return 0  # situation zero

    elif (path1 == False and path2 == True):

        return 1  # situation one

    elif (path1 == True and path2 == False):

        return 2  # situation two

    else:

        return 3  # situation three


def maxPathSumTriangle(arr):

    for row in range(len(arr)-2, -1, -1):
        for col in range(len(arr[row])):
            situation = primePathChecker(
                defaultArray[row+1][col], defaultArray[row+1][col+1])

            if (situation == 0):
                # situation zero (both numbers are not prime. You have to go with maximum number.)
                arr[row][col] += max(arr[row+1][col], arr[row+1][col+1])

            elif (situation == 1):
                # situation two (only path1 is prime. You have to go with path2.)
                arr[row][col] += arr[row+1][col]

            elif (situation == 2):  # situation three(Both numbers are prime)
                arr[row][col] += arr[row+1][col+1]

            elif (situation == 3):  # situation three(Both numbers are prime)
                # Both numbers are prime!!
                pass

            else:
                print("Something get wrong! Check your code")
                break
    return f"Answer: {arr[0][0]}"


with open("values.txt") as f:
    arr = []
    for line in f:
        arr.append(list(map(int, line.split(" "))))
    # default array for checking prime numbers
    defaultArray = [row[:] for row in arr]
    print(maxPathSumTriangle(arr))
