#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
#Once 'done' is entered, print out the largest and smallest of the numbers.
#If the user enters anything other than a valid number catch it with a try/except and
#put out an appropriate message and ignore the input. Enter the numbers from the book for problem
#5.1 and Match the desired output as shown.


largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    if len(inp) < 1 : break   #check for empty line which lets user continue without writing done.
    try:
        value = int(num)
    except ValueError, ex:
        print 'Invalid input'
        continue

    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    if largest is None:
        largest = smallest
    elif value > smallest:
        largest = value


print 'Maximum is', largest
print 'Minimum is', smallest