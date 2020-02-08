num1 = 9473


def smallest(input):
    list = []
    list = [int(x) for x in str(input)]
    numbers_sorted = sorted(list)
    #print(numbers_sorted)
    smallout = int(''.join(map(str,numbers_sorted)))
    return smallout

def largest(input):
    list = []
    list = [int(x) for x in str(input)]
    numbers_sorted = sorted(list, reverse=True)
    #print(numbers_sorted)
    largeout = int(''.join(map(str,numbers_sorted)))
    return largeout

print("starting number is " + str(num1))

res = largest(num1) - smallest(num1)
counter = 0
while res != 6174:
    res = largest(res) - smallest(res)
    counter += 1
    print("after " + str(counter) + " interations the answer is: " + str(res))
