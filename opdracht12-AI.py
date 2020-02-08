
for numbers in range(1, 101, 1):
    output = ''
    if (numbers % 3) == 0: output += 'Fizz'
    if (numbers % 5) == 0: output += 'Buzz'
    if output == '': output = numbers
    print(output)
